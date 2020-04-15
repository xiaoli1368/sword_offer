#include <iostream>

typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 平衡二叉树的定义就是左右子树的高度差小于等于1
    // 因此在递归获取高度时一旦发现不满足，则应退出保存
    // 所以需要借助一个类内的全局变量
    bool isBalanced = true;

    // 首先需要获取高度
    int getTreeHeight(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int left = getTreeHeight(root->left);
        int right = getTreeHeight(root->right);

        // 调整二者大小，使得 left >= right
        if (left < right) {
            int tmp = left;
            left = right;
            right = tmp;
        }

        if (left - right > 1) {
            isBalanced = false;
        }

        return 1 + left;
    }

    // 参考答案
    bool isBalanced_Solution(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        getTreeHeight(root);
        return isBalanced;
    }

    // 个人解法
    bool isBalanced_Solution2(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        int l = getTreeHeight(root->left);
        int r = getTreeHeight(root->right);

        // 交换位置使得l为较大的值
        // 不能使用 (l - r <= 1 || r - l <= 1)
        // 因为这个是一定成立的
        if (l < r) {
            int tmp = l;
            l = r;
            r = tmp;
        }

        return l - r <= 1 && isBalanced_Solution2(root->left) && isBalanced_Solution2(root->right);
    }
};

int main(int argc, char* argv[])
{
    // 需要补充测试用例
    return 0;
}