// 建立树的结构，完成舒适化
// 完成三种遍历方式
// 完成两种遍历方式确定整个树

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
    // 第一次的解法，存在很大的优化空间
    // 可以看到每次都是传递数组值，效率比较低
    TreeNode* reConstructBinaryTree1(std::vector<int> pre, std::vector<int> vin) {
        TreeNode* newTree = new TreeNode(pre[0]);
        if (pre.size() == 1 && vin.size() == 1) {
            return newTree;
        }
        
        int index = 0;
        for (auto i : vin) {
            if (i != pre[0]) {
                index++;
            } else {
                break;
            }
        }
        
        std::vector<int> newLeftPre, newLeftVin, newRightPre, newRightVin;
        newLeftPre.assign(pre.begin() + 1, pre.begin() + 1 + index);
        newRightPre.assign(pre.begin() + 1 + index, pre.end());
        newLeftVin.assign(vin.begin(), vin.begin() + index);
        newRightVin.assign(vin.begin() + 1 + index, vin.end());
        
        if (newLeftPre.size() != 0) {
            newTree->left = reConstructBinaryTree1(newLeftPre, newLeftVin);
        }
        if (newRightPre.size() != 0) {
            newTree->right = reConstructBinaryTree1(newRightPre, newRightVin);
        }
        
        return newTree;
    }

    // 递归优化版
    TreeNode* reConstructBinaryTree2(std::vector<int> pre, std::vector<int> vin) {
        if (pre.empty() || vin.empty()) {
            return nullptr;
        }

        return reConstructFunc(pre, 0, pre.size() - 1, vin, 0, vin.size() - 1);
    }

    TreeNode* reConstructFunc(std::vector<int>& pre, int p1, int p2, std::vector<int>& vin, int v1, int v2) {
        if (p1 > p2 || v1 > v2) {
            return nullptr;
        }
        
        // 获取划分点坐标
        int vinMid = v1;
        while (vinMid <= v2) {
            if (vin[vinMid] == pre[p1]) {
                break;
            }
            vinMid++;
        }
        int preMid = p1 + vinMid - v1; // 注意二者有可能不是对齐的，所以需要两个mid

        TreeNode* root = new TreeNode(pre[p1]);
        root->left = reConstructFunc(pre, p1+1, preMid, vin, v1, vinMid-1);
        root->right = reConstructFunc(pre, preMid+1, p2, vin,vinMid+1, v2);

        return root;
    }

    // 测试函数
    void test(std::vector<int>& pre, std::vector<int>& vin) {
        TreeNode* root = nullptr;
        struct timeval start, end;

        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            root = (this->*func)(pre, vin);
            gettimeofday(&end, nullptr);
            printf("times(us): %ld, result:\n", end.tv_usec - start.tv_usec);
            TreeNode_printThreeOrder(root);
        }

        return;
    }

private:
    typedef TreeNode* (Solution::*func_ptr)(std::vector<int>, std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::reConstructBinaryTree1,
                                       &Solution::reConstructBinaryTree2};
};

int main(int argc, char* argv[])
{
    // 利用前序数组和中序列数组，重建二叉树
    std::vector<int> pre = {1, 2, 4, 7, 3, 5, 6, 8};
    std::vector<int> vin = {4, 7, 2, 1, 5, 3, 6, 8};

    Solution s;
    s.test(pre, vin);

    return 0;
}