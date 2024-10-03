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



def sum_numbers_helper(root_node, res, num=[]):
    if root_node==None:
        return 
        
    num.append(root_node.val)

    if root_node.left==None and root_node.right==None:
        res.append(list(num))
    

    sum_numbers_helper(root_node.left, res, num)
    sum_numbers_helper(root_node.right, res, num)

    num.pop()


def sum_numbers(root_node: Optional[treenode]) ->int:
    
    if not root_node:
        return 0

    res = []
    num=[]
    sum_numbers_helper(root_node, res, num)
    
    total = 0
    for lst in res:
        temp_sum = 0
        pos = 0    
        for i in range(len(lst)-1, -1, -1):
            
            temp_sum += lst[i] * (10**pos)
            pos += 1

        total += temp_sum
    

    return total
    

if __name__ == "__main__":
    root_arr = [1,2,3]
    root_arr = [4,9,0,5,1]
    # root_arr = [1, 2, 3, 4, 5, 6, 7]
    root_node = create_binary_tree_levelorder(root_arr, 0)

    # root_node = treenode(1)
    # root_node.left = treenode(2)
    # root_node.right = treenode(3)
    # print_tree(root_node)

    print(sum_numbers(root_node))
