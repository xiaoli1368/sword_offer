#include <vector>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"
#include "my_vector.h"

/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
*/

class Solution {
public:
    // 1. 两vector迭代，顺序遍历，借助stl翻转
    std::vector<std::vector<int>> PrintLevelOrder1(TreeNode* root) {
        if (root == nullptr) {
            return std::vector<std::vector<int>> {};
        }

        int flag = 0;
        std::vector<std::vector<int>> ret;
        std::vector<TreeNode*> curr_list = {root};

        while (!curr_list.empty()) {
            std::vector<int> curr_vec;
            std::vector<TreeNode*> next_list;

            for (auto & node : curr_list) {
                curr_vec.push_back(node->val);
                if (node->left) {
                    next_list.push_back(node->left);
                }
                if (node->right) {
                    next_list.push_back(node->right);
                }
            }

            if (flag == 1) {
                std::reverse(curr_vec.begin(), curr_vec.end());
            }
            flag = 1 - flag;

            ret.push_back(curr_vec);
            curr_list = next_list;
        }

        return ret;
    }

    // 2. 两个vector迭代，倒序遍历，借助flag翻转
    std::vector<std::vector<int> > PrintLevelOrder2(TreeNode* root) {
        if (root == nullptr) {
            return std::vector<std::vector<int>> {};
        }

        int sign = 0; // 表示从左到右
        std::vector<std::vector<int>> ret;
        std::vector<TreeNode*> curr_list = {root};
        
        while (!curr_list.empty()) {
            std::vector<int> curr_vec;
            std::vector<TreeNode*> next_list;
            
            // 永远是倒序遍历
            // 0先右后左添加，1先左后右添加
            for (int j = curr_list.size() - 1; j >= 0; j--) {
                auto i = curr_list[j];
                curr_vec.push_back(i->val);
                if (sign == 0) {
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                } else {
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                }
            }
            sign = 1 - sign;
            ret.push_back(curr_vec);
            curr_list = next_list;
        }
        
        return ret;
    }

    // 3. 使用vec模拟双端队列，选择不同的插入位置，单端队列实现按层次遍历
    std::vector<std::vector<int> > PrintLevelOrder3(TreeNode* root) {
        if (root == nullptr) {
            return std::vector<std::vector<int>> {};
        }

        std::vector<std::vector<int>> ret;
        std::deque<TreeNode*> queue = {root};
        
        while (!queue.empty()) {
            TreeNode* node = nullptr;
            std::vector<int> curr_vec;
            int last_num = queue.size();

            for (int i = 0; i < last_num; i++) {
                node = queue.front();
                queue.pop_front();
                auto insertIndex = (ret.size() % 2 ? curr_vec.begin() : curr_vec.end()); // 奇偶层选择头插或尾插
                curr_vec.insert(insertIndex, node->val);
                if (node->left) queue.push_back(node->left);
                if (node->right) queue.push_back(node->right);
            }
            ret.push_back(curr_vec);
        }
        
        return ret;
    }

    // 测试函数
    void test(std::vector<int> vec) {
        std::vector<std::vector<int>> result;
        struct timeval start, end;
        TreeNode* head = TreeNode_creatFromFrontOrder(vec);
        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(head);
            gettimeofday(&end, nullptr);
            printf("times(us): %ld, result: \n", end.tv_usec - start.tv_usec);
            printf_2d_vec(result);
        }
    }

private:
    typedef std::vector<std::vector<int>> (Solution::*func_ptr)(TreeNode*);
    std::vector<func_ptr> func_vec_ = {&Solution::PrintLevelOrder1,
                                       &Solution::PrintLevelOrder2,
                                       &Solution::PrintLevelOrder3};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1};
    std::vector<int> vec2 = {3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1};

    Solution s;
    //s.test(vec);
    s.test(vec2);

    return 0;
}