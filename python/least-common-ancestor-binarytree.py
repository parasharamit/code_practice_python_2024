from typing import *

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None



def create_binarytree_level_order(root_lst: List[int], idx: int) -> Optional[TreeNode]:
    
    if idx >= len(root_lst) or not root_lst[idx]:
        return None 
    
    root_node = TreeNode(root_lst[idx])
    root_node.left = create_binarytree_level_order(root_lst, 2 * idx + 1)
    root_node.right = create_binarytree_level_order(root_lst, 2 * idx + 2)

    return root_node




def lineage_search(root_node, res_str, tmp_str, val):
    if root_node==None:
        return
    
    elif root_node.val==val:
        res_str = str(tmp_str)
        return res_str

    
    lineage_search(root_node, res_str, tmp_str+"L", val)
    lineage_search(root_node, res_str, tmp_str+"R", val)


    return

if __name__ == "__main__":
    root_lst = [5,1,2,3,None,6,4]

    root_node = create_binarytree_level_order(root_lst, 0)

    res_str = ""

    lineage_search(root_node, res_str, "", 6)

    