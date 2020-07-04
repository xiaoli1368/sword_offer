#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>

#include "TreeNode.h"

/*
typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;
*/

class Solution {
public:
    // 1. 个人解法，先序遍历，自顶向下递归调用，存在优化空间
    bool isBalanced_Solution1(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        return abs(depth(root->left) - depth(root->right)) <= 1 && isBalanced_Solution1(root->left) && isBalanced_Solution1(root->right);
    }

    // 获取树的深度
    int depth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return 1 + std::max(depth(root->left), depth(root->right));
    }

    // 2. 后序遍历，提前剪枝
    bool isBalanced_Solution2(TreeNode* root) {
        return depthAndJudge(root) != -1;
    }

    // 返回当前树的高度，如果是-1，表明是非平衡二叉树
    int depthAndJudge(TreeNode* root) {
        if (root == nullptr) { // 当前节点为空
            return 0;
        }

        int left = depthAndJudge(root->left);
        if (left == -1) { // 左子树不平衡
            return -1;
        }

        int right = depthAndJudge(root->right);
        if (right == -1) { // 右子树不平衡
            return -1;
        }

        if (abs(left - right) > 1) { // 当前节点不平衡
            return -1;
        }

        return 1 + std::max(left, right); // 返回正常高度
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        bool result = false;
        struct timeval start, end;
        TreeNode* root = TreeNode_creatFromFrontOrder(vec);

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(root);
            gettimeofday(&end, nullptr);
            printf("result: %d, times(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::isBalanced_Solution1,
                                       &Solution::isBalanced_Solution2};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1};
    std::vector<int> vec2 = {1, 2, 3, 4, -1, -1, 4, -1, -1, 3, -1, -1, 2, -1, -1};

    Solution s;
    s.test(vec);
    s.test(vec2);

    return 0;
}