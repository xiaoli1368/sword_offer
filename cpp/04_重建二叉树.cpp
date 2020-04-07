// 建立树的结构，完成舒适化
// 完成三种遍历方式
// 完成两种遍历方式确定整个树

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
    // 由先序数组，创建完全二叉树，
    // 输出数组长度必须是一颗完全二叉树的总节点数目
    // 也没有对错误的情况做出处理
    void creatTree(std::vector<int> vec, TreeNode* head) {
        int length = vec.size();

        if (length == 0) {
            return;
        }

        head->val = vec[0];

        if (length == 1) {
            head->left = nullptr;
            head->right = nullptr;
        }

        if (length > 1) {
            head->left = new TreeNode(0);
            head->right = new TreeNode(0);

            std::vector<int> vec2;
            vec2.assign(vec.begin() + 1, vec.begin() + 1 + length / 2);
            creatTree(vec2, head->left);

            vec2.assign(vec.begin() + 1 + length / 2, vec.end());
            creatTree(vec2, head->right);
        }

    }

    // 更为高效的构建方式
    // 传递两个索引值和数组的引用
    void creatTree2(std::vector<int>& vec, int begin, int end, TreeNode* head) {
        int length = end - begin + 1;
        if (length == 0) {
            return;
        }

        head->val = vec[begin];
        // for test
        //std::cout << head->val << std::endl;

        if (length == 1) {
            head->left = nullptr;
            head->right = nullptr;
        }

        if (length > 1) {
            head->left = new TreeNode(0);
            head->right = new TreeNode(0);
            creatTree2(vec, begin + 1, (begin + end) / 2, head->left);
            creatTree2(vec, (begin + end) / 2 + 1, end, head->right);
        }
    }

    // 先序遍历输出
    void print_front_order(TreeNode* head) {
        if (head == nullptr) {
            return;
        }
        std::cout << head->val << " ";
        print_front_order(head->left);
        print_front_order(head->right);
    }

    // 中序遍历输出
    void print_middle_order(TreeNode* head) {
        if (head == nullptr) {
            return;
        }
        print_middle_order(head->left);
        std::cout << head->val << " ";
        print_middle_order(head->right);
    }

    // 后序遍历输出
    void print_end_order(TreeNode* head) {
        if (head == nullptr) {
            return;
        }
        print_end_order(head->left);
        print_end_order(head->right);
        std::cout << head->val << " ";
    }

    // 将三种遍历格式化输出一遍
    void print_three_order(TreeNode* head) {
        std::cout << "===== three orders =====" << std::endl;
        print_front_order(head);
        std::cout << std::endl;
        print_middle_order(head);
        std::cout << std::endl;
        print_end_order(head);
        std::cout << std::endl;
    }

    TreeNode* reConstructBinaryTree(std::vector<int> pre, std::vector<int> vin) {
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
            newTree->left = reConstructBinaryTree(newLeftPre, newLeftVin);
        }
        if (newRightPre.size() != 0) {
            newTree->right = reConstructBinaryTree(newRightPre, newRightVin);
        }
        
        return newTree;
    }
};

int main(int argc, char* argv[])
{
    // 注意到这个是完全二叉树
    // 如果是非完全二叉树，则应该使用null标记，即使是完全的也要标记
    // {1, 2, 4, null, null, 5, null, null, 3, 6, null, null, 7, null, null}
    // 因此需要使用null来确定每个节点的位置
    std::vector<int> vec = {1, 2, 4, 5, 3, 6, 7};
    Solution s;
    TreeNode* head = new TreeNode(0);

    //s.creatTree(vec, head);
    s.creatTree2(vec, 0, vec.size() - 1, head);
    s.print_three_order(head);


    // 利用前序数组和中序列数组，重建二叉树
    std::vector<int> pre = {1, 2, 4, 7, 3, 5, 6, 8};
    std::vector<int> vin = {4, 7, 2, 1, 5, 3, 6, 8};
    TreeNode* myNewTree = s.reConstructBinaryTree(pre, vin);
    s.print_three_order(myNewTree);

    return 0;
}