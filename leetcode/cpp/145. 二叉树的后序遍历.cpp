#include <vector>
#include <stack>
#include <map>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    std::vector<int> ret;
public:
    // 递归法
    std::vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return ret;
        }

        postorderTraversal(root->left);
        postorderTraversal(root->right);
        ret.push_back(root->val);

        return ret;
    }

    // 状态标记法
    std::vector<int> postorderTraversal2(TreeNode* root) {
        std::vector<int> ret;
        std::stack<std::pair<TreeNode*, bool>> stack;
        if (root) {
            stack.push(std::make_pair(root, false));
        }
        while (!stack.empty()) {
            std::pair<TreeNode*, bool> node = stack.top();
            stack.pop();
            if (node.second) {
                ret.push_back(node.first->val);
                continue;
            }
            stack.push(std::make_pair(node.first, true));
            if (node.first->right) {
                stack.push(std::make_pair(node.first->right, false));
            }
            if (node.first->left) {
                stack.push(std::make_pair(node.first->left, false));
            }
        }
        return ret;
    }

    

};