from textual.app import App
from textual.containers import Container
from textual.widgets import Tree, DataTable
from textual.widgets.tree import TreeNode
from textual.binding import Binding
from textual import log
from textual.widgets import DataTable
from multipledispatch import dispatch


class TreeTableApp(App):
    # Specify the path to the CSS file for styling the app
    CSS_PATH = "styles/style.tcss"
    
    # Define keyboard bindings for navigation and interaction
    BINDINGS = [
        Binding("enter", "select_cursor", "Select"),
        Binding("space", "toggle_node", "Toggle"),
        Binding("up", "cursor_up", "Cursor Up"),
        Binding("down", "cursor_down", "Cursor Down"),
    ]

    # Variables to hold the tree data and the columns to display
    DATA_TREE = ''  # JSON-like tree data
    collumns_to_display = None  # List of columns to filter

    def __init__(self):
        # Initialize the app
        super().__init__()

    def compose(self):
        """Compose the layout of the application."""
        with Container(id="container"):
            # Create a Tree widget and build its structure based on the JSON data
            tree: Tree[dict] = Tree("Data Tree", id='tree')
            self.build_tree(tree.root, self.DATA_TREE["Data Tree"])
            yield tree

            # Create a DataTable widget and build its rows and columns
            table = DataTable(id='table')
            yield table
            self.build_table(table, self.DATA_TREE["Data Tree"])
            self.is_scrollable = False

    def build_tree(self, root_node: TreeNode, node_data: dict):
        """
        Recursively build the Tree widget structure.

        Args:
            root_node (TreeNode): The root node of the Tree widget.
            node_data (dict): JSON-like dictionary representing the tree structure.
        """
        if node_data.get("open"):
            root_node.expand()
        else:
            root_node.collapse()

        children = node_data.get("children", {})
        if len(children.items()) == 0:
            root_node.allow_expand = False
        for child_name, child_data in children.items():
            if child_name == "open":
                continue

            # Add a child node and recursively build its structure
            child_node = root_node.add(child_name)
            if "children" in child_data and isinstance(child_data["children"], dict):
                self.build_tree(child_node, child_data)

    def build_table(self, table: DataTable, node_data: dict):
        """
        Build the table structure and populate its data.

        Args:
            table (DataTable): The DataTable widget.
            node_data (dict): JSON-like dictionary representing the tree structure.
        """
        columns = {}
        if self.collumns_to_display is None:  # Show all columns if no filter is applied
            self.collect_columns(node_data, columns, table)
        else:  # Use the filtered column list
            self.collect_columns_filtered(node_data, columns, table)

        self.populate_table_rows(table, node_data)

    def collect_columns_filtered(self, node_data: dict, columns: dict, table: DataTable):
        """
        Collect and add only the filtered columns to the DataTable.

        Args:
            node_data (dict): JSON-like dictionary representing the tree structure.
            columns (dict): Tracks already added columns.
            table (DataTable): The DataTable widget.
        """
        if "data" in node_data:
            for key in node_data["data"].keys():
                self.log.debug(self.collumns_to_display)
                self.log.debug(f"ENTERED FOR {key}")
                if key in self.collumns_to_display:
                    if key not in columns:
                        column_key = table.add_column(label=key, key=key)
                        columns[key] = column_key

        children = node_data.get("children", {})
        for child_data in children.values():
            self.collect_columns_filtered(child_data, columns, table)

    def collect_columns(self, node_data: dict, columns: dict, table: DataTable):
        """
        Collect and add all unique columns to the DataTable.

        Args:
            node_data (dict): JSON-like dictionary representing the tree structure.
            columns (dict): Tracks already added columns.
            table (DataTable): The DataTable widget.
        """
        if "data" in node_data:
            for key in node_data["data"].keys():
                if key not in columns:
                    column_key = table.add_column(label=key, key=key)
                    columns[key] = column_key

        children = node_data.get("children", {})
        for child_data in children.values():
            self.collect_columns(child_data, columns, table)

    def populate_table_rows(self, table: DataTable, node_data: dict, parent_key=""):
        """
        Populate the rows of the DataTable with tree data.

        Args:
            table (DataTable): The DataTable widget.
            node_data (dict): JSON-like dictionary representing the tree structure.
            parent_key (str): Unique key representing the parent node.
        """
        if "data" in node_data:
            row_key = f"{parent_key}_row" if parent_key else "root_row"
            row = []
            for column in table.columns.keys():
                value = node_data["data"].get(column, "")
                row.append(str(value))
            table.add_row(*row, key=row_key)

        if node_data.get("open", False):
            children = node_data.get("children", {})
            for child_name, child_data in children.items():
                child_key = f"{parent_key}/{child_name}" if parent_key else child_name
                self.populate_table_rows(table, child_data, parent_key=child_key)

    def find_node(self, obj: dict, key: str):
        """
        Find a specific node in the tree.

        Args:
            obj (dict): JSON-like dictionary representing the tree structure.
            key (str): The key of the node to find.

        Returns:
            dict: The found node, or None if not found.
        """
        if key in obj:
            return obj[key]
        for k, v in obj.items():
            if isinstance(v, dict):
                item = self.find_node(v, key)
                if item is not None:
                    return item

    def update_ui(self):
        """
        Update the DataTable based on the current state of the tree.
        """
        table: DataTable = self.query_one("#table")
        table.clear(columns=True)
        self.build_table(table, self.DATA_TREE["Data Tree"])

    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        """
        Handle the event when a tree node is expanded.

        Args:
            event (Tree.NodeExpanded): The expansion event.
        """
        node = event.node
        node_name = node.label
        items_in_node = self.find_node(self.DATA_TREE, str(node_name))
        items_in_node['open'] = True
        self.update_ui()

    def on_tree_node_collapsed(self, event: Tree.NodeCollapsed) -> None:
        """
        Handle the event when a tree node is collapsed.

        Args:
            event (Tree.NodeCollapsed): The collapse event.
        """
        node = event.node
        node_name = node.label
        items_in_node = self.find_node(self.DATA_TREE, str(node_name))
        items_in_node['open'] = False
        self.update_ui()

    def drawTreeTable(self, data: dict, cols: list = None):
        """
        Render the tree table with the given data and optional column filter.

        Args:
            data (dict): JSON-like dictionary representing the tree structure.
            cols (list): List of column names to display. If None, display all columns.
        """
        if cols is not None:
            self.collumns_to_display = cols.copy()
        self.DATA_TREE = data
        self.run()
