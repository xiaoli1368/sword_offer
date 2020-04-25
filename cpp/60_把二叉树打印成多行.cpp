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
            
            vector<TreeNode*> curr_list = {root};
            
            while (!curr_list.empty()) {
                // 将curr_list内值整理到ret，同时子结点整理到next_list
                vector<int> tmp;
                vector<TreeNode*> next_list;
                for (auto i : curr_list) {
                    tmp.push_back(i->val);
                    if (i->left != nullptr) {
                        next_list.push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        next_list.push_back(i->right);
                    }
                }
                
                ret.push_back(tmp);
                curr_list = next_list;
            }
            
            return ret;
        }
};