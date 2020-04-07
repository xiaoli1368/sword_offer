#include <iostream>
#include <vector>

typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 先序创建二叉树（从向量中）
    // 由于使用了引用，这种方式会损坏外部的向量vec
    TreeNode* creat_TreeNode(std::vector<int>& vec) {
        if (vec.size() == 0) {
            return nullptr;
        }
        if (vec[0] == -1) {
            vec.erase(vec.begin());
            return nullptr;
        }
        TreeNode* currHead = new TreeNode(vec[0]);
        vec.erase(vec.begin());
        currHead->left = creat_TreeNode(vec);
        currHead->right = creat_TreeNode(vec);
        return currHead;
    }

    // 先序打印二叉树
    void print_TreeNode(TreeNode* head) {
        if (head == nullptr) {
            std::cout << -1 << " ";
            return;
        }
        std::cout << head->val << " ";
        print_TreeNode(head->left);
        print_TreeNode(head->right);
    }

    // 返回当前二叉树的镜像
    TreeNode* Mirror(TreeNode* root) {
        if (root == nullptr) {
            return root;
        }

        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        Mirror(root->left);
        Mirror(root->right);

        return root;
    }

    // 返回二叉树的镜像（无返回值版本，直接指针操作）
    void Mirror2(TreeNode* root) {
        if (root == nullptr) {
            return;
        }

        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        Mirror2(root->left);
        Mirror(root->right);
        return;
    }
};


int main(int argc, char* argv[])
{
    std::vector<int> array = {8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1};

    Solution s;
    TreeNode* head = s.creat_TreeNode(array);

    s.print_TreeNode(head);
    std::cout << std::endl;

    head = s.Mirror(head);
    s.print_TreeNode(head);
    std::cout << std::endl;

    return 0;
}