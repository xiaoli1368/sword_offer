/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // 获取三数中的最大值
    inline int max(int a, int b, int c) {
        int tmp = a > b ? a : b;
        return tmp > c ? tmp : c;
    }

    // 找到值为x的节点
    TreeNode* front(TreeNode* root, int x) {
        if (root == nullptr || root->val == x) {
            return root;
        }
        TreeNode* left = front(root->left, x);
        if (left) {
            return left;
        }
        TreeNode* right = front(root->right, x);
        if (right) {
            return right;
        }
        return nullptr;
    }

    // 统计二叉树个数
    int nodeNum(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return 1 + nodeNum(root->left) + nodeNum(root->right);
    }

    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        if (root == nullptr) {
            return true;
        }
        TreeNode* curr = front(root, x);
        int left = nodeNum(curr->left);
        int right = nodeNum(curr->right);
        int num = max(left, right, n - left - right - 1);
        return num > n - num;
    }
};