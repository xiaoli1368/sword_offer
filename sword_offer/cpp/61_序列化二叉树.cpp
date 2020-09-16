#include <string>
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
private:
    std::string ret;

public:
    // 1. string接口
    // 序列化，先序遍历
    // 使用逗号分割，空节点为#
    std::string Serialize(TreeNode *root) {
        if (root == nullptr) {
            return "#,";
        } else {
            return std::to_string(root->val) + "," + Serialize(root->left) + Serialize(root->right);
        }
    }
    
    // 反序列化
    TreeNode* Deserialize(std::string str) {
        int index = 0;
        return Des(str, index);
    }

    // 递归函数
    TreeNode* Des(std::string& str, int& i) {
        if (str.empty() || i >= str.size()) { // 防止溢出
            return nullptr;
        }

        if (str[i] == '#') { // 空节点
            i += 2;
            return nullptr;
        }

        // 提取当前结点值
        int curr_val = 0;
        for (; str[i] != ','; i++) {
            curr_val = curr_val * 10 + (str[i] - '0');
        }
        i++; // 跳过标志符号','
        
        TreeNode* root = new TreeNode(curr_val);
        root->left = Des(str, i);
        root->right = Des(str, i);
        return root;
    }
    
    // 2. char*接口（用于牛客网提交，本地不进行调试）
    char* char_Serialize(TreeNode *root) {    
        if (root == nullptr) {
            return nullptr;
        }
        this->ret = this->Serialize(root);
        return (char*)(ret.c_str());
    }
    
    TreeNode* char_Deserialize(char *str) {
        if (str == nullptr) {
            return nullptr;
        }
        std::string tmp = str;
        return Deserialize(tmp);
    }

    // 测试函数
    void test(std::vector<int>& vec) {
        struct timeval start, end;
        std::string str;
        TreeNode* rec = nullptr;
        TreeNode* ori = TreeNode_creatFromFrontOrder(vec);

        printf("=====\n");
        gettimeofday(&start, nullptr);
        str = this->Serialize(ori);
        rec = this->Deserialize(str);
        gettimeofday(&end, nullptr);
        
        printf("times(us): %ld, str: %s\n", end.tv_usec - start.tv_usec, str.c_str());
        printf("ori-front-order: ");
        TreeNode_printFrontOrder(ori);
        printf("\nrec-front-order: ");
        TreeNode_printFrontOrder(rec);
        printf("\n");
    }
};

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1};

    Solution s;
    s.test(vec);

    return 0;
}