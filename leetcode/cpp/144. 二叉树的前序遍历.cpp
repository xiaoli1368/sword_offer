#include <vector>
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // 先序遍历
    void front(TreeNode* root, vector<int>& ret) {
        if (root == nullptr) {
            return;
        }
        ret.push_back(root->val);
        front(root->left);
        front(root->right);
        return;
    }

    // 递归法
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        front(root, ret);
        return ret;
    }

    // 迭代法
    vector<int> preorderTraversal2(TreeNode* root) {
        std::vector<int> ret;
        std::stack<TreeNode*> stack;
        if (root) {
            stack.push(root);
        }

        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            ret.push_back(node->val);
            if (node->right) {
                stack.push(node->right);
            }
            if (node->left) {
                stack.push(node->left);
            }
        }

        return ret;
    }
};