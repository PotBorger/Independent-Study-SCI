from textual.app import App
from textual.containers import Container
from textual.widgets import Tree, DataTable
from textual.widgets.tree import TreeNode
from textual.binding import Binding
from textual import log
from textual.widgets import DataTable
from multipledispatch import dispatch



class TreeTableApp(App):
    CSS_PATH = "styles/style.tcss"
    BINDINGS = [
        Binding("enter", "select_cursor", "Select"),
        Binding("space", "toggle_node", "Toggle"),
        Binding("up", "cursor_up", "Cursor Up"),
        Binding("down", "cursor_down", "Cursor Down"),
    ]

    DATA_TREE = ''
    collumns_to_display = None
    
    def __init__(self):
        super().__init__()

    def compose(self):
        with Container(id="container"):
            # Create a tree widget 
            tree: Tree[dict] = Tree("Data Tree",id='tree')
            self.build_tree(tree.root, self.DATA_TREE["Data Tree"])
            yield tree

            # Create a DataTable widget
            table = DataTable(id='table')
            yield table
            # Build the table columns and rows
            self.build_table(table, self.DATA_TREE["Data Tree"])
            self.is_scrollable = False
            
            # table.scrollbars_enabled = (False, False)
            


    def build_tree(self, root_node: TreeNode, node_data: dict):
    # Set the expansion state based on the 'open' field
        if node_data.get("open"):
            root_node.expand()
        else:
            root_node.collapse()

        # Iterate over the children nodes

        children = node_data.get("children", {})
        if len(children.items()) == 0:
            root_node.allow_expand = False
        for child_name, child_data in children.items():
            if child_name == "open":
                continue

            # Add the child node
            child_node = root_node.add(child_name)
            # Add data as a leaf
            # if "data" in child_data:
            #     for key, value in child_data["data"].items():
            #         child_node.add_leaf(f"{key}: {value}")

            # Recursively build the tree for the child nodes
            if "children" in child_data and isinstance(child_data["children"], dict):
                self.build_tree(child_node, child_data)
            

    
    def build_table(self, table: DataTable, node_data: dict):
        # Collect all unique keys from the data properties of all nodes
        columns = {}
        if self.collumns_to_display == None:  # Show all columns if no specific columns are specified
            self.collect_columns(node_data, columns, table)
        else:  # Filter columns if specific ones are provided
            self.collect_columns_filtered(node_data, columns, table)
        # Populate the DataTable with rows based on the data in each node
        self.populate_table_rows(table, node_data)
    
    def collect_columns_filtered(self, node_data: dict, columns: dict, table: DataTable):
        """Recursively collect all unique column keys from the data properties and add columns to the table."""
        if "data" in node_data:
            for key in node_data["data"].keys():
                    self.log.debug(self.collumns_to_display)
                    self.log.debug(f"ENTERED FOR {key}")
                    if key in self.collumns_to_display:
                        if key not in columns:
                            # Add a new column to the table and store its ColumnKey with a unique key
                            column_key = table.add_column(label=key, key=key)
                            columns[key] = column_key

        children = node_data.get("children", {})
        for child_data in children.values():
            self.collect_columns_filtered(child_data, columns, table)

    def collect_columns(self, node_data: dict, columns: dict, table: DataTable):
        self.log.debug(str(self.collumns_to_display))
        """Recursively collect all unique column keys from the data properties and add columns to the table."""
        self.log.debug("SAI ROI")
        if "data" in node_data:
            for key in node_data["data"].keys():
                    if key not in columns:
                        # Add a new column to the table and store its ColumnKey with a unique key
                        column_key = table.add_column(label=key, key=key)
                        columns[key] = column_key

        children = node_data.get("children", {})
        for child_data in children.values():
            self.collect_columns(child_data, columns, table)

    
    def populate_table_rows(self, table: DataTable, node_data: dict, parent_key=""):
        """Recursively populate the table rows based on the data properties."""
        if "data" in node_data:
            # Create a unique key for each row based on the hierarchy in the data tree
            row_key = f"{parent_key}_row" if parent_key else "root_row"

            # Prepare a row with values in the same order as the columns
            row = []
            for column in table.columns.keys():
                value = node_data["data"].get(column, "")
                row.append(str(value))

            # Add the row to the table with a unique key
            table.add_row(*row, key=row_key)

        # Only populate rows from open children
        if node_data.get("open", False):
            children = node_data.get("children", {})
            for child_name, child_data in children.items():
                # Recursively add rows for children nodes
                child_key = f"{parent_key}/{child_name}" if parent_key else child_name
                self.populate_table_rows(table, child_data, parent_key=child_key)



    def find_node(self,obj:dict, key):
        if key in obj: return obj[key]
        for k, v in obj.items():
            if isinstance(v,dict):
                item = self.find_node(v, key)
                if item is not None:
                    return item
            
    def update_ui(self):
        # Access the table widget by its ID
        table: DataTable = self.query_one("#table")

        # Clear the existing table data
        table.clear(columns=True)

        # Rebuild the table with the updated DATA_TREE
        self.build_table(table, self.DATA_TREE["Data Tree"])
    
    # Event handler for node expansion
    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        node = event.node
        node_name = node.label
        items_in_node = self.find_node(self.DATA_TREE,str(node_name))
        items_in_node['open'] = True
        current_state_of_node = items_in_node['open']
        self.log.debug(str(self.DATA_TREE))
        # self.log.debug("node:" + str(node.label)+ "is open or not: " + str(current_state_of_node))
        self.update_ui()
        
    def on_tree_node_collapsed(self, event: Tree.NodeCollapsed) -> None:
        node = event.node
        node_name = node.label
        items_in_node = self.find_node(self.DATA_TREE,str(node_name))
        items_in_node['open'] = False
        current_state_of_node = items_in_node['open']
        # self.log.debug("node:" + str(node.label)+ "is open or not: " + str(current_state_of_node))
        self.update_ui()

    def drawTreeTable(self, data : str, cols:list = None):
        if cols!=None:
            self.collumns_to_display = cols.copy()
        self.DATA_TREE = data
        self.run()