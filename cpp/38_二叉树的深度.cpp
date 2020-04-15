#include <iostream>

typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {};
} TreeNode;

class Solution {
public:
    int TreeDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int left = TreeDepth(root->left);
        int right = TreeDepth(root->right);

        return 1 + (left > right ? left : right);
    }
};

int main(int argc, char* argv[])
{
    // 需要补充测试用例
    return 0;
}