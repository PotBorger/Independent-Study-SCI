from textual.app import App, ComposeResult
from textual.widgets import Tree, DataTable
from textual.containers import Container

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



class TreeTableApp(App):
    CSS_PATH = "style.tcss"
    def compose(self) -> ComposeResult:
        with Container(id="container"):
            tree: Tree[dict] = Tree("Dune")
            tree.root.expand()
            characters = tree.root.add("Characters")
            characters.add_leaf("Paul")
            characters.add_leaf("Jessica")
            characters.add_leaf("Chani")
            tree.root.expand()
            chapters = tree.root.add("Chapters")
            chap1 = chapters.add("Chapter 1")
            chap1.add_leaf("Part 1")
            chap1.add_leaf("Part 2")
            chapters.add_leaf("Chapter 2")
            chapters.add_leaf("Chapter 3")

            yield tree
            yield DataTable()


    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])



if __name__ == "__main__":
    app = TreeTableApp()
    app.run()