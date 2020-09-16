#include <vector>
#include <queue>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"
#include "my_vector.h"

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
    // 1. 两个向量交替存储
    std::vector<std::vector<int> > PrintLevelOrder1(TreeNode* root) {
        if (root == nullptr) {
            return std::vector<std::vector<int>>{};
        }

        std::vector<std::vector<int>> ret;
        std::vector<TreeNode*> curr_list = {root};
        
        while (!curr_list.empty()) {
            std::vector<int> curr_vec;
            std::vector<TreeNode*> next_list;
            for (auto & i : curr_list) {
                curr_vec.push_back(i->val);
                if (i->left != nullptr) {
                    next_list.push_back(i->left);
                }
                if (i->right != nullptr) {
                    next_list.push_back(i->right);
                }
            }
            ret.push_back(curr_vec);
            curr_list = next_list;
        }
        
        return ret;
    }

    // 2. 队列法，bfs
    std::vector<std::vector<int>> PrintLevelOrder2(TreeNode* root) {
        if (root == nullptr) {
            return std::vector<std::vector<int>>{};
        }

        std::vector<std::vector<int>> ret;
        std::queue<TreeNode*> queue;
        queue.push(root);

        while (!queue.empty()) {
            std::vector<int> curr_vec;
            int last_num = queue.size();
            for (int i = 0; i < last_num; i++) { // 遍历提取上一层
                TreeNode* node = queue.front();
                queue.pop();
                curr_vec.push_back(node->val);
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            ret.push_back(curr_vec);
        }

        return ret;
    }

    // 3. 递归法，dfs
    std::vector<std::vector<int>> PrintLevelOrder3(TreeNode* root) {
        std::vector<std::vector<int>> ret;
        dfs(root, ret, 0);
        return ret;
    }

    void dfs(TreeNode* root, std::vector<std::vector<int>>& ret, int level) {
        if (root == nullptr) {
            return;
        }
        if (level >= ret.size()) {
            ret.push_back(std::vector<int>{});
        }
        ret[level].push_back(root->val);
        dfs(root->left, ret, level + 1);
        dfs(root->right, ret, level + 1);
        return;
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
    s.test(vec);
    s.test(vec2);

    return 0;
}