#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"

/*
typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {};
} TreeNode;
*/

class Solution {
public:
    // 递归法
    int TreeDepth1(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int left = TreeDepth1(root->left);
        int right = TreeDepth1(root->right);

        return 1 + (left > right ? left : right);
    }

    // 迭代法，bfs，寻找最深的层次
    int TreeDepth2(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int ret = 0;
        std::vector<TreeNode*> last = {root};

        while (!last.empty()) {
            std::vector<TreeNode*> curr;
            for (auto & node : last) {
                if (node->left) {
                    curr.push_back(node->left);
                }
                if (node->right) {
                    curr.push_back(node->right);
                }
            }
            last = curr;
            ret++;
        }

        return ret;
    }

    // 测试函数
    void test(TreeNode* root) {
        int result = 0;
        struct timeval start, end;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(root);
            gettimeofday(&end, nullptr);
            printf("result: %d, times(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::TreeDepth1, &Solution::TreeDepth2};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1};
    TreeNode* root = TreeNode_creatFromFrontOrder(vec);

    Solution s;
    s.test(root);

    return 0;
}