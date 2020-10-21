typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 中序遍历，更新差值
    void mid(TreeNode* root, int& ret, int& lastVal) {
        if (root == nullptr) {
            return;
        }
        mid(root->left, ret, lastVal);
        if (root->val - lastVal < ret) {
            ret = root->val - lastVal;
        }
        lastVal = root->val;
        mid(root->right, ret, lastVal);
    }

    int getMinimum(TreeNode* root) {
        int ret = 0x7fffffff;
        int lastVal = 0x80000000;
        mid(root, ret, lastVal);
        return ret;
    }
};