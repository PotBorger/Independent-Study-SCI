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

#     DATA_TREE = {
#     "Data Tree": {
#         "open": True,  
#         "children": {

#             "A": {
#                 "open": True,  
#                 "data": {
#                     "value": 5
#                 },
                
#                 "children": {
#                     "B": {
#                         "open": True,
#                         "data": {
#                             "value": 10
#                         },
#                         "children": {}
#                     },
#                     "C": {
#                         "open": True, 
#                         "data": {
#                             "value": 4
#                         },
#                         "children": {
#                             "D": {
#                                 "open": True, 
#                                 "data": {
#                                     "value": 12,
#                                     "message": "hi"
#                                 },\
#                                 "children": {
#                                     "E": {
#                                 "open": True, 
#                                 "data": {
#                                     "value": 12,
#                                     "message": "hi"
#                                 },
#                                 "children": {}
#                             }
#                                 }
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }

    DATA_TREE = {
        "Data Tree": {
            "open": True,
            "children": {
                "Company": {
                    "open": True,
                    "data": {
                        "name": "TechCorp",
                        "established": 2005
                    },
                    "children": {
                        "HR Department": {
                            "open": True,
                            "data": {
                                "head": "Alice Johnson",
                                "employees": 25
                            },
                            "children": {
                                "Recruitment Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Michael Brown",
                                        "open_positions": 5
                                    },
                                    "children": {}
                                },
                                "Training Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Sophie Green",
                                        "trainings_conducted": 8
                                    },
                                    "children": {}
                                }
                            }
                        },
                        "Engineering Department": {
                            "open": True,
                            "data": {
                                "head": "David Wilson",
                                "employees": 100
                            },
                            "children": {
                                "Backend Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "James Carter",
                                        "projects": 5
                                    },
                                    "children": {
                                        "API Project": {
                                            "open": True,
                                            "data": {
                                                "project_lead": "Sophia Thompson",
                                                "status": "In Progress",
                                                "developers": 10
                                            },
                                            "children": {}
                                        },
                                        "Database Optimization": {
                                            "open": True,
                                            "data": {
                                                "project_lead": "Robert Miller",
                                                "progress": "60%"
                                            },
                                            "children": {}
                                        }
                                    }
                                },
                                "Frontend Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Emma Garcia",
                                        "projects": 3
                                    },
                                    "children": {
                                        "UI Redesign": {
                                            "open": True,
                                            "data": {
                                                "project_lead": "Liam Martinez",
                                                "status": "In Progress",
                                                "designers": 4
                                            },
                                            "children": {}
                                        },
                                        "Accessibility Improvement": {
                                            "open": True,
                                            "data": {
                                                "project_lead": "Grace Lopez",
                                                "status": "Planning",
                                                "expected_completion": "Q4 2024"
                                            },
                                            "children": {}
                                        }
                                    }
                                }
                            }
                        },
                        "Sales Department": {
                            "open": True,
                            "data": {
                                "head": "Laura Roberts",
                                "employees": 40
                            },
                            "children": {
                                "Domestic Sales": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Noah Walker",
                                        "clients": 75
                                    },
                                    "children": {}
                                },
                                "International Sales": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "William White",
                                        "clients": 50
                                    },
                                    "children": {
                                        "Europe Region": {
                                            "open": True,
                                            "data": {
                                                "region_lead": "Charlotte Anderson",
                                                "active_clients": 20
                                            },
                                            "children": {}
                                        },
                                        "Asia Region": {
                                            "open": True,
                                            "data": {
                                                "region_lead": "Henry Harris",
                                                "active_clients": 30
                                            },
                                            "children": {}
                                        }
                                    }
                                }
                            }
                        },
                        "Finance Department": {
                            "open": True,
                            "data": {
                                "head": "Ethan Clark",
                                "budget": "10M USD"
                            },
                            "children": {
                                "Audit Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Mason Lewis",
                                        "auditors": 8,
                                        "last_audit": "Q2 2024"
                                    },
                                    "children": {}
                                },
                                "Accounts Payable": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Ava King",
                                        "invoices_processed": 300
                                    },
                                    "children": {}
                                }
                            }
                        },
                        "Operations Department": {
                            "open": True,
                            "data": {
                                "head": "Grace Young",
                                "employees": 30
                            },
                            "children": {
                                "Logistics Team": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Lucas Scott",
                                        "deliveries_per_month": 150
                                    },
                                    "children": {}
                                },
                                "Facility Management": {
                                    "open": True,
                                    "data": {
                                        "team_lead": "Amelia Baker",
                                        "buildings_managed": 5
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


    def compose(self):
        with Container(id="container"):
            # Create a tree widget
            tree: Tree[dict] = Tree("Data Tree")
            self.build_tree(tree.root, self.DATA_TREE["Data Tree"])
            yield tree

                        # Create a DataTable widget
            table = DataTable()
            yield table

            # Build the table columns and rows
            self.build_table(table, self.DATA_TREE["Data Tree"])

    def build_tree(self, root_node: TreeNode, node_data: dict):
    # Set the expansion state based on the 'open' field
        if node_data.get("open",False):
            root_node.expand()
        else:
            root_node.collapse()

        # Iterate over the children nodes
        children = node_data.get("children", {})
        for child_name, child_data in children.items():
           
            if child_name == "open":
                continue

            # Add the child node
            child_node = root_node.add(child_name)

            # Add data as a leaf
            if "data" in child_data:
                for key, value in child_data["data"].items():
                    child_node.add_leaf(f"{key}: {value}")

            # Recursively build the tree for the child nodes
            if "children" in child_data and isinstance(child_data["children"], dict):
                self.build_tree(child_node, child_data)

    def build_table(self, table: DataTable, node_data: dict):
        # Collect all unique keys from the data properties of all nodes
        columns = {}
        self.collect_columns(node_data, columns, table)

        # Populate the DataTable with rows based on the data in each node
        self.populate_table_rows(table, node_data)

    def collect_columns(self, node_data: dict, columns: dict, table: DataTable):
        """Recursively collect all unique column keys from the data properties and add columns to the table."""
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
            table.add_row("")
            for key, value in node_data["data"].items():
                row_key = f"{parent_key}_{key}_row" if parent_key else f"{key}_row"
                # Prepare a row with values in the same order as the columns
                row = []
                for column in table.columns.keys():
                    row.append(str(value) if column == key else "")

                # Add the row to the table with a unique key
                table.add_row(*row, key=row_key, height=1)

        children = node_data.get("children", {})
        for child_name, child_data in children.items():
            # Recursively add rows for children nodes
            child_key = f"{parent_key}_{child_name}" if parent_key else child_name
            self.populate_table_rows(table, child_data, parent_key=child_key)

if __name__ == "__main__":
    app = TreeTableApp()
    app.run()
