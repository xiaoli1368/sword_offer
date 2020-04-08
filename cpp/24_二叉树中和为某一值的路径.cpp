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

    // 打印一维向量
    void print_vector(std::vector<int>& vec) {
        if (vec.empty()) {
            return;
        }
        for (auto i : vec) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    // 打印二维向量
    void print_2d_vector(std::vector<std::vector<int>>& vec) {
        for (auto v1 : vec) {
            for (auto v2 : v1) {
                std::cout << v2 << " ";
            }
            std::cout << std::endl;
        }
    }

    // 用于递归的函数
    void backTracking(TreeNode* root, int target) {
        if (root == nullptr) {
            return;
        }

        path.push_back(root->val);
        target -= root->val;

        if (target == 0 && root->left == nullptr && root->right == nullptr) {
            ret.push_back(path);
        } else {
            backTracking(root->left, target);
            backTracking(root->right, target);
        }

        path.pop_back();
    }

    // 寻找和为某值的路径
    std::vector<std::vector<int>> FindPath(TreeNode* root, int target) {
        backTracking(root, target);
        return ret;
    }

private:
    std::vector<int> path;             // 当前某一条路径
    std::vector<std::vector<int>> ret; // 返回值
};

int main(int argc, char* argv[])
{
    Solution s;
    std::vector<int> vec = {10, 7, 4, -1, -1, 5, -1, -1, 12, -1, -1};

    // 初始化并且打印查看
    TreeNode* head = s.init_with_array(vec);
    s.print_TreeNode(head);

    // 寻找路径
    std::vector<std::vector<int>> result;
    result = s.FindPath(head, 22);
    s.print_2d_vector(result);

    return 0;
}