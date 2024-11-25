from TreeTableApp import TreeTableApp
from textual import *
import json

if __name__ == "__main__":
    file_name = "ExampleJsonShort.json"
    with open(f"json_files_for_testing/{file_name}", "r") as file:
        data = json.load(file)
    app = TreeTableApp()
    app.drawTreeTable(data,['value'])




