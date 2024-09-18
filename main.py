from textual.app import App
from textual.containers import Container
from textual.widgets import Tree, DataTable
from textual.reactive import reactive
from textual.widgets.tree import TreeNode
from textual.binding import Binding


class TreeTableApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        Binding("enter", "select_cursor", "Select"),
        Binding("space", "toggle_node", "Toggle"),
        Binding("up", "cursor_up", "Cursor Up"),
        Binding("down", "cursor_down", "Cursor Down"),
    ]

    ROWS = [
        ("lane", "swimmer", "country", "time"),
        (4, "Joseph Schooling", "Singapore", 50.39),
        (2, "Michael Phelps", "United States", 51.14),
        (5, "Chad le Clos", "South Africa", 51.14),
        (6, "László Cseh", "Hungary", 51.14),
        (3, "Li Zhuhao", "China", 51.26),
        (8, "Mehdy Metella", "France", 51.58),
        (7, "Tom Shields", "United States", 51.73),
        (1, "Aleksandr Sadovnikov", "Russia", 51.84),
        (10, "Darren Burns", "Scotland", 51.84),
    ]

    selected_swimmer = reactive(None)

    def compose(self):
        with Container(id="container"):
            tree: Tree[dict] = Tree("Contestant Data")
            tree.root.expand()
            characters_root = tree.root.add("Swimmers")
            for row in self.ROWS[1:]:
                node = characters_root.add(f"Lane {row[0]}")
                leaf = node.add_leaf(
                    row[1],
                    data=row[1],
                    before=None,
                    after=None,
                )
                leaf.data = row  # Store row data in the node
            yield tree
            yield DataTable()

    async def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self.ROWS[0])  # Add the header
        await self.update_table(self.ROWS[1])  # Initially display the first row

    async def update_table(self, row):
        """Update the table to show the selected swimmer's data."""
        table = self.query_one(DataTable)
        table.clear()  # Clear any existing rows
        table.add_row(*map(str, row))  # Add the selected row

    async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Handle tree node selection event."""
        selected_node: TreeNode = event.node
        if selected_node.data:
            selected_row = selected_node.data  # Get the data associated with the node
            await self.update_table(selected_row)


if __name__ == "__main__":
    app = TreeTableApp()
    app.run()
