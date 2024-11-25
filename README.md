# 📦 TreeTableApp

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Framework](https://img.shields.io/badge/framework-Textual-orange)

> *TreeTableApp aims to provide an interactive and user-friendly way to visualize hierarchical data.*

---

## 🌟 Highlights

- Dynamically visualize hierarchical JSON data in a **Tree** structure with expandable/collapsible nodes.
- Associated data for each node is displayed in a **Table** view.
- Customizable table columns for focused data exploration.
- Lightweight, easy to integrate, and runs in the terminal.

---

## ℹ️ Overview

**TreeTableApp** is a terminal-based tool for rendering hierarchical JSON data. It displays the structure in a tree format and provides a tabular view of the node data. It is helpful for analyzing, debugging, or exploring nested datasets interactively.

---

## ✍️ Authors

Created by [Nolan Mai](https://github.com/PotBorger) under the guidance of Dr. Isaacs of SCI at the U.
Reach out for feedback, suggestions, or contributions on [GitHub](https://github.com/PotBorger/Independent-Study-SCI).

---

### Keyboard Commands

| Key          | Action                               |
|--------------|--------------------------------------|
| **Enter**    | Select the current node              |
| **Space**    | Expand or collapse a tree node       |
| **Up**       | Move the cursor up                   |
| **Down**     | Move the cursor down                 |
| **Tab**      | Switch cursor between tree and table |


---

## 🚀 Usage

```python
from TreeTableApp import TreeTableApp
import json

# Load your JSON data
with open("json_files_for_testing/ExampleJsonShort.json", "r") as file:
    data = json.load(file)

# Initialize and run the app
app = TreeTableApp()
app.drawTreeTable(data)
```

## 📝 Data Format

The input JSON must follow this structure:

```json
                      
            {
    "Data Tree": { // Whether the node is expanded (true) or collapsed (false)
                // The root must always be "Data Tree" and should not contain any data
                // (no "data" attribute for the root node).
        "open": true,
        "children": {
            "A": { //Child node
                "open": false,
                "data": {
                    "value": 5
                },
                "children": {
                    "B": {
                        "open": false,
                        "data": {
                            "value": 10
                        },
                        "children": {}
                    },
                    "C": {
                        "open": false,
                        "data": {
                            "value": 4
                        },
                        "children": {
                            "D": {
                                "open": false,
                                "data": {
                                    "value": 12,
                                    "message": "hi"
                                },
                                "children": {
                                    "E": {
                                        "open": false,
                                        "data": {
                                            "value": 13,
                                            "message": "hello"
                                        },
                                        "children": {}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```
Expected output:


### Data Notes

1. **`open`:** Defines whether the node is initially expanded (`true`) or collapsed (`false`).

 **Note** for **`open`**: This attribute is optional. If there is none, the program 
will automatically add one **`open`:** for each node and set it to `false`, which makes the node collapsed.
2. **`data`:** A dictionary containing key-value pairs associated with the node.
3. **`children`:** A dictionary of child nodes, recursively formatted.

### Filtering out columns in DataTable

To filter out the unnecessary data in the input json, add a **`[columns]`** list as the second argument when calling drawTreeTable.

```python
from TreeTableApp import TreeTableApp
import json

# Load your JSON data
with open("json_files_for_testing/ExampleJsonShort.json", "r") as file:
    data = json.load(file)

# Initialize and run the app
app = TreeTableApp()
app.drawTreeTable(data, ['value'])
```
Expected output:

---

## ⬇️ Installation

Install the required dependencies and ensure you are using **Python 3.10+**.

```bash
pip install textual 
```

---

## 💻 How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/PotBorger/Independent-Study-SCI.git
    cd Independent-Study-SCI
    ```

2. Use the sample data in `json_files_for_testing/ExampleJsonShort.json` or provide your own JSON file.

3. Run the app:
    ```bash
    python3 program.py
    ```

---

