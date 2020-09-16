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
    // 1. 中序遍历：左 中　右
    TreeNode* last = nullptr; // 类内变量，记录双链表的尾部
    TreeNode* Convert(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // 左
        // 将左子树挂载到last上，并返回头
        TreeNode* head = Convert(root->left); // 中间变量，记录双链表的头
        if (head == nullptr) {
            head = root;
        }
        
        // 中
        // 完成last和根的链接
        root->left = last;
        if (last != nullptr) {
            last->right = root;
        } 
        last = root;
        
        // 右
        Convert(root->right);
        return head;
    }

    // 2. 中序遍历：右　中　左
    TreeNode* head = nullptr;
    TreeNode* Convert2(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // 右
        Convert2(root->right);
        
        // 中
        root->right = head;
        if (head != nullptr) {
            head->left = root;
        }
        head = root;
        
        // 左
        Convert2(root->left);
        
        return head;
    }

    // 按双向链表顺序打印二叉树（先右子树方向，然后按左子树方向返回）
    void printf_2d_tree(TreeNode* root) {
        if (root == nullptr) {
            return;
        }

        TreeNode* tail = nullptr;
        while (root != nullptr) {
            tail = root;
            printf("%d, ", root->val);
            root = root->right;
        }

        while (tail != nullptr) {
            printf("%d, ", tail->val);
            tail = tail->left; 
        }
        printf("\n");
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
            printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
            printf_2d_tree(result);
        }
    }

private:
    typedef TreeNode* (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::Convert, &Solution::Convert2};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {4, 2, 1, -1, -1, 3, -1, -1, 6, 5, -1, -1, 7, -1, -1};

    Solution s;
    s.test(vec);

    return 0;
}