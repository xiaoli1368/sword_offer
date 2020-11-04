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
    // 后续遍历
    // 0安装相机，1已覆盖，2未覆盖
    int back(TreeNode* root, int& ret) {
        if (root == nullptr) {
            return 1;
        }
        int left = back(root->left, ret);
        int right = back(root->right, ret);
        if (left == 2 || right == 2) {
            ret += 1;
            return 0;
        } else if (left == 0 || right == 0) {
            return 1;
        } else {
            return 2;
        }
    }

    int minCameraCover(TreeNode* root) {
        int ret = 0;
        if (back(root, ret) == 2) {
            ret += 1;
        }
        return ret;
    }
};