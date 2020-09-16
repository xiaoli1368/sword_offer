#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"

/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/

class Solution {
public:
    // 递归法
    bool isSymmetrical(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        return isSame(root->left, root->right);
    }

    bool isSame(TreeNode* a, TreeNode* b) {
        if (a == nullptr && b == nullptr) {
            return true;
        }
        if (a == nullptr || b == nullptr) {
            return false;
        }
        return a->val == b->val && isSame(a->left, b->right) && isSame(a->right, b->left);
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        bool result;
        struct timeval start, end;
        TreeNode* root = TreeNode_creatFromFrontOrder(vec);
        printf("=====\n");
        gettimeofday(&start, nullptr);
        result = this->isSymmetrical(root);
        gettimeofday(&end, nullptr);
        printf("result: %d, times(us): %ld, front-order: ", result, end.tv_usec - start.tv_usec);
        TreeNode_printFrontOrder(root);
        printf("\n");
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 3, -1, -1, 4, -1, -1, 2, 4, -1, -1, 3, -1, -1};
    std::vector<int> vec2 = {1, 2, -1, 3, -1, -1, 2, -1, 3, -1, -1};

    Solution s;
    s.test(vec);
    s.test(vec2);

    return 0;
}