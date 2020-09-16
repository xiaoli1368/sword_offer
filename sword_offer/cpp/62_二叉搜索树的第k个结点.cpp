#include <vector>
#include <stdio.h>
#include <sys/time.h>

#include "TreeNode.h"

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
    // 1. 整体中序遍历，返回有序数组节点，输出索引为k-1的元素
    TreeNode* KthNode1(TreeNode* root, int k) {
        if (root == nullptr or k <= 0) {
            return nullptr;
        }

        std::vector<TreeNode*> vec;
        getMiddleVec(root, vec);

        if (k > vec.size()) {
            return nullptr;
        }
        return vec[k - 1];
    }

    // 中序遍历，添加节点到数组中
    void getMiddleVec(TreeNode* root, std::vector<TreeNode*>& vec) {
        if (root == nullptr) {
            return;
        }

        getMiddleVec(root->left, vec);
        vec.push_back(root);
        getMiddleVec(root->right, vec);
        return;
    }

    // 2. 高效方法：中序遍历第k个即可，利用全局变量来
    int cnt = 0; // 外部计数变量
    TreeNode* KthNode2(TreeNode* root, int k) {
        if (root == nullptr or k <= 0) {
            return nullptr;
        }

        TreeNode* ret = KthNode2(root->left, k);
        if (ret != nullptr) {
            return ret;
        }
        
        if (++cnt == k) {
            return root;
        }

        ret = KthNode2(root->right, k);
        if (ret != nullptr) {
            return ret;
        }
        
        return nullptr; // 如果没有找到
    }

    // 测试函数
    void test(std::vector<int>& vec, int k) {
        TreeNode* result = nullptr;
        TreeNode* root = TreeNode_creatFromFrontOrder(vec);
        struct timeval start, end;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(root, k);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result->val, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef TreeNode* (Solution::*func_ptr)(TreeNode*, int);
    std::vector<func_ptr> func_vec_  = {&Solution::KthNode1, &Solution::KthNode2};
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {5, 3, 2, 1, -1, -1, -1, 4, -1, -1, 6, -1, -1};

    Solution s;
    s.test(vec, 3);

    return 0;
}