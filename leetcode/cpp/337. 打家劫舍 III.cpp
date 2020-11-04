/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#define MAX(x, y) ((x) > (y) ? (x) : (y))
class Solution {
public:
    // 后续遍历
    void back(TreeNode* root, int& rootOn, int& rootOff) {
        if (root == nullptr) {
            return;
        }
        int leftOn = 0, leftOff = 0, rightOn = 0, rightOff = 0;
        back(root->left, leftOn, leftOff);
        back(root->right, rightOn, rightOff);
        rootOn = root->val + leftOff + rightOff;
        rootOff = MAX(leftOn, leftOff) + MAX(rightOn, rightOff);
        return;
    }
	
    int rob(TreeNode* root) {
        int rootOn = 0, rootOff = 0;
        back(root, rootOn, rootOff);
        return MAX(rootOn, rootOff);
    }
};