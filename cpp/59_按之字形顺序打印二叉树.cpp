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
    vector<vector<int> > Print(TreeNode* root) {
        vector<vector<int>> ret;
        if (root == nullptr) {
            return ret;
        }
        
        int sign = 0; // 表示从左到右
        vector<TreeNode*> curr_list = {root};
        
        while (!curr_list.empty()) {
            vector<int> tmp;
            vector<TreeNode*> next_list;
            
            // 永远是倒序遍历
            // 0先右后左添加，1先左后右添加
            for (int j = curr_list.size() - 1; j >= 0; j--) {
                auto i = curr_list[j];
                tmp.push_back(i->val);
                if (sign == 0) {
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                } else {
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                }
            }
            ret.push_back(tmp);
            curr_list = next_list;
            sign = 1 - sign;
        }
        
        return ret;
    }
};