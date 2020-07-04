#include <iostream>
#include <vector>
#include <stack>
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
    // 1. 递归法，自顶向下，在原树上操作
    TreeNode* Mirror1(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        // 左右子树交换
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        // 递归下一层
        Mirror1(root->left);
        Mirror1(root->right);

        return root;
    }

    // 2. 辅助栈，自顶向下，在原树上操作
    TreeNode* Mirror2(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        std::stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();

            // 交换左右子树
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;

            // 入栈
            if (node->left) {
                stack.push(node->left);
            }
            if (node->right) {
                stack.push(node->right);
            }
        }

        return root;
    }

    // 3. 递归法，自底向上，新建一颗树（也可以在原树上操作）
    TreeNode* Mirror3(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        TreeNode* head = new TreeNode(root->val);
        head->left = Mirror3(root->right);
        head->right = Mirror3(root->left);

        return head;
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        struct timeval start, end;
        TreeNode* result = nullptr;
        printf("=====\n");

        for (auto & func : this->func_vec_) {
            TreeNode* root = TreeNode_creatFromFrontOrder(vec);
            gettimeofday(&start, nullptr);
            result = (this->*func)(root);
            gettimeofday(&end, nullptr);
            printf("result: ");
            TreeNode_printFrontOrder(result);
            printf("times(us): %ld\n", end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef TreeNode* (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::Mirror1,
                                       &Solution::Mirror2,
                                       &Solution::Mirror3};
};


int main(int argc, char* argv[])
{
    std::vector<int> vec = {8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1};

    Solution s;
    s.test(vec);

    return 0;
}