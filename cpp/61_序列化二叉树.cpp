/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    std::string ret;
    
    std::string my_Serialize(TreeNode *root) {
        if (root == nullptr) {
            return "#";
        } else {
            // 先序遍历
            return std::to_string(root->val) + "!" + my_Serialize(root->left) + my_Serialize(root->right);
        }
    }
    
    TreeNode* my_Deserialize(char* &str) {
        if (*str == '#') {
            return nullptr;
        }
        
        // 提取当前结点值
        int curr_val = 0;
        while (*str != '!') {
            curr_val = curr_val * 10 + (*str - '0');
            str++;
        }
        
        TreeNode* currNode = new TreeNode(curr_val);
        currNode->left = my_Deserialize(++str);
        currNode->right = my_Deserialize(++str);
        
        return currNode;
    }
    
    char* Serialize(TreeNode *root) {    
        if (root == nullptr) {
            return nullptr;
        }
        
        this->ret = my_Serialize(root);
        return (char*)(ret.c_str());
    }
    
    TreeNode* Deserialize(char *str) {
        if (str == nullptr) {
            return nullptr;
        }
        
        return my_Deserialize(str);
    }
};