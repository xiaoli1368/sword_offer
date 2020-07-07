#include <iostream>
#include <vector>
#include <queue>
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
    // 1. 两个向量交替存储法，模拟队列优化版
    std::vector<int> PrintFromTopToBottom1(TreeNode* head) {
        if (head == nullptr) {
            return std::vector<int>{};
        }

        std::vector<int> result;
        std::vector<TreeNode*> curr_list = {head};

        while (!curr_list.empty()) {
            std::vector<TreeNode*> next_list;
            for (auto & node : curr_list) {
                result.push_back(node->val);
                if (node->left) {
                    next_list.push_back(node->left);
                }
                if (node->right) {
                    next_list.push_back(node->right);
                }
            }
            curr_list = next_list;
        }

        return result;
    }

    // 2. 使用vector模拟队列
    std::vector<int> PrintFromTopToBottom2(TreeNode* head) {
        if (head == nullptr) {
            return std::vector<int>{};
        }

        std::vector<int> result;
        std::vector<TreeNode*> queue = {head};

        while (!queue.empty()) {
            TreeNode* currNode = queue.front();
            queue.erase(queue.begin());
            result.push_back(currNode->val);
            if (currNode->left) {
                queue.push_back(currNode->left);
            }
            if (currNode->right) {
                queue.push_back(currNode->right);
            }
        }

        return result;
    }

    // 3. 真正的队列形式
    std::vector<int> PrintFromTopToBottom3(TreeNode* head) {
        if (head == nullptr) {
            return std::vector<int>{};
        }

        std::vector<int> result;
        std::queue<TreeNode*> queue;
        queue.push(head);

        while (!queue.empty()) {
            TreeNode* currNode = queue.front();
            queue.pop();
            result.push_back(currNode->val);
            if (currNode->left) {
                queue.push(currNode->left);
            }
            if (currNode->right) {
                queue.push(currNode->right);
            }
        }

        return result;
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        std::vector<int> result;
        struct timeval start, end;
        TreeNode* head = TreeNode_creatFromFrontOrder(vec);
        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head);
            gettimeofday(&end, nullptr);
            printf("times(us): %ld, result: ", end.tv_usec - start.tv_usec);
            printf_1d_vec(result);
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::PrintFromTopToBottom1,
                                       &Solution::PrintFromTopToBottom2,
                                       &Solution::PrintFromTopToBottom3};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1};
    std::vector<int> vec2 = {3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1};

    Solution s;
    s.test(vec);
    s.test(vec2);

    return 0;
}