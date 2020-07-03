#ifndef TREENODE_H
#define TREENODE_H

#include <vector>
#include <stdio.h>

// 定义树节点
typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {};
} TreeNode;

// 从先序序列中构建二叉树
// 空为-1
TreeNode* TreeNode_creatFunc(std::vector<int>& vec, int& begin, int& end) {
    if (vec.empty() || begin > end || vec[begin] == -1) {
        begin++;
        return nullptr;
    }

    TreeNode* root = new TreeNode(vec[begin++]);
    root->left = TreeNode_creatFunc(vec, begin, end);
    root->right = TreeNode_creatFunc(vec, begin, end);

    return root;
}

TreeNode* TreeNode_creatFromFrontOrder(std::vector<int>& vec) {
    int begin = 0;
    int end = vec.size() - 1;
    return TreeNode_creatFunc(vec, begin, end);
}

// 先序遍历输出
void TreeNode_printFrontOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    printf("%d, ", root->val);
    TreeNode_printFrontOrder(root->left);
    TreeNode_printFrontOrder(root->right);
    return;
}

// 中序遍历输出
void TreeNode_printMiddleOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    TreeNode_printMiddleOrder(root->left);
    printf("%d, ", root->val);
    TreeNode_printMiddleOrder(root->right);
    
    return;
}

// 后序遍历输出
void TreeNode_printBackOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    TreeNode_printMiddleOrder(root->left);
    TreeNode_printMiddleOrder(root->right);
    printf("%d, ", root->val);

    return;
}

// 输出三种遍历顺序
void TreeNode_printThreeOrder(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    printf("===== three order =====\n");
    TreeNode_printFrontOrder(root);
    printf("\n");
    TreeNode_printMiddleOrder(root);
    printf("\n");
    TreeNode_printBackOrder(root);
    printf("\n");
}

#endif