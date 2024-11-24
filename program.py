from TreeTableApp import TreeTableApp
from textual import *
import json

if __name__ == "__main__":
    
    with open("json_files_for_testing/example1.json", "r") as file:
        data = json.load(file)
    app = TreeTableApp()
    app.drawTreeTable(data)




