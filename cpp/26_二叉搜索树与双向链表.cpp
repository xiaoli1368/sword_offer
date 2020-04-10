#include <iostream>

typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 中序遍历：左 中　右
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

    // 中序遍历：右　中　左
    TreeNode* head = nullptr;
    TreeNode* Convert2(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        // 右
        Convert(root->right);
        
        // 中
        root->right = head;
        if (head != nullptr) {
            head->left = root;
        }
        head = root;
        
        // 左
        Convert(root->left);
        
        return head;
    }
};

int main(int argc, char* argv[])
{
    return 0;
}