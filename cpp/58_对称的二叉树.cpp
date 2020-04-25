/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSame(TreeNode* a, TreeNode* b) {
        if (a == nullptr && b == nullptr) {
            return true;
        } else if (a != nullptr && b != nullptr) {
            return a->val == b->val && isSame(a->left, b->right) && isSame(a->right, b->left);
        } else {
            return false;
        }
    }
    
    bool isSymmetrical(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        return isSame(root->left, root->right);
    }

};