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
private:
    std::vector<int> ret;
public:
    // 递归法
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return ret;
        }

        inorderTraversal(root->left);
        ret.push_back(root->val);
        inorderTraversal(root->right);

        return ret;
    }

    // 迭代法
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> stack;
        TreeNode* curr = root;
        while (!stack.empty() || curr) {
            // 遍历左子树，直到最左侧
            while (curr) {
                stack.push(curr);
                curr = curr->left;
            }
            // 存储中间值
            curr = stack.top();
            stack.pop();
            ret.push_back(curr->val);
            // 指向右子树
            curr = curr->right;
        }
        return ret;
    }
};