from typing import *

class treenode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_tree(root_node: Optional[treenode], prefix: str="", is_left: bool=True):
    if not root_node:
        return None


    # Print the current node with the appropriate prefix
    print(prefix, end="")
    print("├── " if is_left else "└── ", end="")
    print(root_node.val)


    if is_left:
        prefix += "│   "
    else:
        prefix += "    "

    # Recursively print the left and right children
    print_tree(root_node.left, prefix, True)
    print_tree(root_node.right, prefix, False)



def create_binary_tree_levelorder(root_arr: List[int], idx: int) -> Optional[treenode]:
     
    if idx >= len(root_arr):
        return None
    
    root_node = treenode(root_arr[idx])
    root_node.left = create_binary_tree_levelorder(root_arr, 2*idx+1)
    root_node.right = create_binary_tree_levelorder(root_arr, 2*idx+2)

    return root_node