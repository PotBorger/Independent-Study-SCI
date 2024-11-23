from TreeTableApp import TreeTableApp
import json

if __name__ == "__main__":
    
    with open("json_files_for_testing/ExampleJsonShort.json", "r") as file:
        data = json.load(file)
    app = TreeTableApp()
    app.drawTreeTable(data,['value'])




