#include <bits/stdc++.h>
using namespace std;


struct treenode 
{
    treenode *left;
    treenode *right;
    int val;

    public:
        treenode(int x) {
            left = nullptr;
            right = nullptr;
            val = x;
        }
};


void print_tree(treenode *root, string prefix="", bool is_left=true) 
{
    if (root==nullptr)
        return;

    cout<<prefix;

    cout<< (is_left ? "├──" : "└──");

    // Print the value of the node
    cout<< root->val << endl;

    print_tree(root->left, prefix + (is_left ? "│   " : "    "), true);
    print_tree(root->right, prefix + (is_left ? "│   " : "    "), false);
}


treenode * create_binarytree_helper(vector<int> arr, int index) 
{
    
    if (index > arr.size()) 
        return nullptr;

    treenode *root = new treenode(arr[index]);
    root->left = create_binarytree_helper(arr, 2*index+1);
    root->right = create_binarytree_helper(arr, 2*index+2);

    return root;

}

treenode *create_binarytree(vector<int> &arr) 
{
    if (arr.empty()) {
        return nullptr;
    }

    treenode *root_node = create_binarytree_helper(arr, 0);

    return root_node;
}

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6};

    /*
                  1
                 / \
                2   3
               / \ /
              4  5 6
    */

    arr = {1, 2, 3, NULL, 4, NULL, NULL, 5, 6, NULL, 7};

    treenode*root = create_binarytree(arr);

    if (root) {
        print_tree(root);
    }

    return 0;

}