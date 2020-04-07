#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 使用向量来初始化二叉树
    // 先序，-1表示空
    TreeNode* init_with_array(std::vector<int>& vec) {
        if (vec.empty()) {
            return nullptr;
        }
        if (vec.front() == -1) {
            vec.erase(vec.begin());
            return nullptr;
        }

        TreeNode* tmp = new TreeNode(vec.front());
        vec.erase(vec.begin());
        tmp->left = init_with_array(vec);
        tmp->right = init_with_array(vec);
        return tmp;
    }

    // 先序打印二叉树
    void print_func(TreeNode* head) {
        if (head == nullptr) {
            // 这里的-1就不打印了
            return;
        }
        std::cout << head->val << " ";
        print_func(head->left);
        print_func(head->right);
    }

    // 先序列打印二叉树，包含换行
    void print_TreeNode(TreeNode* head) {
        print_func(head);
        std::cout << std::endl;
    }

    // 打印向量
    void print_vector(std::vector<int>& vec) {
        if (vec.empty()) {
            return;
        }
        for (auto i : vec) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    // 从上往下打印二叉树
    // 两个向量交替存储法
    std::vector<int> PrintFromTopToBottom(TreeNode* head) {
        std::vector<int> result;
        if (head == nullptr) {
            return result;
        }

        std::vector<TreeNode*> curr_list;
        curr_list.push_back(head);
        while (!curr_list.empty()) {
            std::vector<TreeNode*> next_list;
            for (auto node : curr_list) {
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

    // 从上往下打印二叉树
    // 使用队列的形式
    std::vector<int> PrintFromTopToBottom2(TreeNode* head) {
        std::vector<int> result;
        if (head == nullptr) {
            return result;
        }

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

    // 从上到下打印二叉树
    // 使用真正的队列形式
    std::vector<int> PrintFromTopToBottom3(TreeNode* head) {
        std::vector<int> result;
        if (head == nullptr) {
            return result;
        }

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

    // 拓展，之字形打印
    std::vector<int> Print_type_zhi(TreeNode* head) {
        std::vector<int> result;
        if (head == nullptr) {
            return result;
        }
 
        int index = 1;
        std::vector<TreeNode*> curr_list = {head};

        while (!curr_list.empty()) {
            std::vector<int> curr_result;
            std::vector<TreeNode*> next_list;

            for (auto node : curr_list) {
                curr_result.push_back(node->val);
                if (node->left) {
                    next_list.push_back(node->left);
                }
                if (node->right) {
                    next_list.push_back(node->right);
                }
            }

            if (index % 2 == 1) {
                // 借助stl算法库完成vector的反转
                std::reverse(curr_result.begin(), curr_result.end());
            }

            index++;
            result.insert(result.end(), curr_result.begin(), curr_result.end());
            curr_list = next_list;
        }

        return result;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> vec = {1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1};

    // 初始化并且打印查看
    TreeNode* head = s.init_with_array(vec);
    s.print_TreeNode(head);

    // 从上往下打印
    std::vector<int> result;
    result = s.PrintFromTopToBottom(head);
    s.print_vector(result);
    result = s.PrintFromTopToBottom2(head);
    s.print_vector(result);
    result = s.PrintFromTopToBottom3(head);
    s.print_vector(result);

    // 之字型打印
    result = s.Print_type_zhi(head);
    s.print_vector(result);

    return 0;
}