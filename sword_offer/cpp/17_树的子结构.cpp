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
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;
*/

class Solution {
public:
    // 1. 完全内部实现另外一个递归函数
    bool HasSubtree(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        return isSubtree2(a, b, false);
    }

    // 定义用于递归调用的函数
    // 存在问题，中间会跳过节点判断，无法判断之前是否已经对齐
    bool isSubtree(TreeNode* a, TreeNode* b) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr) {
            return false;
        }
        if (a->val == b->val) {
            return isSubtree(a->left, b->left) && \
                   isSubtree(a->right, b->right) || \
                   isSubtree(a->left, b) || \
                   isSubtree(a->right, b);
        } else {
            return isSubtree(a->left, b) || isSubtree(a->right, b);
        }
    }


    // 定义用于递归调用的函数（优化版）
    // 增加flag用来指示之前是否已经对齐（正确）
    bool isSubtree2(TreeNode* a, TreeNode* b, bool flag) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr) {
            return false;
        }
        if (flag && a->val != b->val) { // 如果之前对齐，本次不等
            return false;
        }
        if (a->val == b->val && isSubtree2(a->left, b->left, true) && isSubtree2(a->right, b->right, true)) {
            return true;
        }
        return isSubtree2(a->left, b, false) || isSubtree2(a->right, b, false);
    }

    // 2. 自身递归即可
    // 注意题目要求空树不是任何树的子结构
    // 这一点与递归中空树是任何树的子结构是冲突的
    // 因为递归才会麻烦一些
    // 同样存在问题，无法判断之前是否已经对齐
    bool HasSubtree2(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        bool tmp = false;
        if (a->val == b->val) {
            if (b->left == nullptr && b->right == nullptr) {
                return true;
            } else if (b->left == nullptr && b->right != nullptr) {
                tmp = HasSubtree2(a->right, b->right);
            } else if (b->right == nullptr && b->left != nullptr) {
                tmp = HasSubtree2(a->left, b->left);
            } else {
                tmp = HasSubtree2(a->left, b->left) && HasSubtree2(a->right, b->right);
            }
        }

        if (tmp) {
            return tmp;
        } else {
            return HasSubtree2(a->left, b) || HasSubtree2(a->right, b);
        }
        // 等价为： return tmp || HasSubtree2(a->left, b) || HasSubtree2(a->right, b);
    }

    // 3. 两个函数，互相递归，先序遍历（根、左、右）
    bool HasSubTree3(TreeNode* a, TreeNode* b) {
        return (a != nullptr && b != nullptr) && (isSubTree3(a, b) || HasSubTree3(a->left, b) || HasSubTree3(a->right, b));
    }

    // 判断是否是子结构，辅助函数，不进行向下的延伸
    bool isSubTree3(TreeNode* a, TreeNode* b) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr || a->val != b->val) {
            return false;
        }
        return isSubTree3(a->left, b->left) && isSubTree3(a->right, b->right);
    }

    // 测试函数
    void test(std::vector<int>& A, std::vector<int>& B) {
        bool result;
        struct timeval start, end;
        TreeNode* a = TreeNode_creatFromFrontOrder(A);
        TreeNode* b = TreeNode_creatFromFrontOrder(B);

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(a, b);
            gettimeofday(&end, nullptr);
            printf("result: %d, times(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(TreeNode*, TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::HasSubtree,
                                       &Solution::HasSubtree2,
                                       &Solution::HasSubTree3};
};


int main(int argc, char* argv[])
{
    std::vector<int> A = {8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1};
    std::vector<int> B = {8, 9, -1, -1, 2, -1, -1};
    std::vector<int> A2 = {1, 0, -4, -1, -1, -3, -1, -1, 1, -1, -1};
    std::vector<int> B2 = {1, -4, -1, -1, -1};

    Solution s;
    s.test(A, B);
    s.test(A2, B2);

    return 0;
}