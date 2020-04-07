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

    // 定义用于递归调用的函数
    bool isSubtree(TreeNode* a, TreeNode* b) {
        if (b == nullptr) {
            return true;
        }
        if (a == nullptr) {
            return false;
        }
        if (a->val == b->val) {
            return isSubtree(a->left, b->left) && \
                   isSubtree(a->right, b->right) || \
                   isSubtree(a->left, b) || \
                   isSubtree(a->right, b);
        } else {
            return isSubtree(a->left, b) || isSubtree(a->right, b);
        }
    }

    // 判断b是否为a的子结构
    bool HasSubtree(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        return isSubtree(a, b);
    }

    // 判断b是否为a的子结构
    // 不使用递归的方式
    bool HasSubtree2(TreeNode* a, TreeNode* b) {
        if (a == nullptr || b == nullptr) {
            return false;
        }

        bool tmp = false;
        if (a->val == b->val) {
            if (b->left == nullptr && b->right == nullptr) {
                return true;
            } else if (b->left == nullptr && b->right != nullptr) {
                tmp = HasSubtree2(a->right, b->right);
            } else if (b->right == nullptr && b->left != nullptr) {
                tmp = HasSubtree2(a->left, b->left);
            } else {
                tmp = HasSubtree2(a->left, b->left) && HasSubtree2(a->right, b->right);
            }
        }

        if (tmp) {
            return tmp;
        } else {
            return HasSubtree2(a->left, b) || HasSubtree2(a->right, b);
        }
    }
};


int main(int argc, char* argv[])
{
    std::vector<int> array = {8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1};
    std::vector<int> array2 = {8, 9, -1, -1, 2, -1, -1};

    Solution s;
    TreeNode* head = s.creat_TreeNode(array);
    TreeNode* head2 = s.creat_TreeNode(array2);

    s.print_TreeNode(head);
    std::cout << std::endl;
    s.print_TreeNode(head2);
    std::cout << std::endl;

    std::cout << s.HasSubtree(head, head2) << std::endl;
    std::cout << s.HasSubtree2(head, head2) << std::endl;

    return 0;
}