#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"
#include "my_vector.h"

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
    // 递归法
    std::vector<std::vector<int>> FindPath(TreeNode* root, int target) {
        std::vector<int> path; // 记录临时的一条路径
        std::vector<std::vector<int>> ret; // 记录最终结果
        backTracking(root, path, ret, target);
        return ret;
    }

    // 用于递归的函数
    void backTracking(TreeNode* root, std::vector<int>& path, std::vector<std::vector<int>>& ret, int target) {
        if (root == nullptr) {
            return;
        }

        path.push_back(root->val); // 打入当前节点
        target -= root->val;

        if (target == 0 && root->left == nullptr && root->right == nullptr) {
            ret.push_back(path); // 找到根节点，并且满足要求
        } else {
            backTracking(root->left, path, ret, target); // 遍历下一层
            backTracking(root->right, path, ret, target);
        }

        path.pop_back(); // 弹出当前节点
    }

    // 测试函数
    void test(std::vector<int>& vec, int target) {
        struct timeval start, end;
        std::vector<std::vector<int>> result;
        TreeNode* root = TreeNode_creatFromFrontOrder(vec);

        printf("=====\n");
        gettimeofday(&start, nullptr);
        result = this->FindPath(root, target);
        gettimeofday(&end, nullptr);
        printf("times(us): %ld, result: \n", end.tv_usec - start.tv_usec);
        printf_2d_vec(result);
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {10, 7, 4, -1, -1, 5, -1, -1, 12, -1, -1};
    std::vector<int> vec2 = {5, 4, 11, 7, -1, -1, 2, -1, -1, -1, 8, 13, -1, -1, 4, 5, -1, -1, 1, -1, -1};

    Solution s;
    s.test(vec, 22);
    s.test(vec2, 22);

    return 0;
}