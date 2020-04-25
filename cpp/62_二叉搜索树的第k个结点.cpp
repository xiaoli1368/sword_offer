//思路一：
//先整体排序，保存到vector，之后输出所以为k-1的元素

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
    std::vector<TreeNode*> tmp;
    void sortInsert(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        
        sortInsert(root->left);
        this->tmp.push_back(root);
        sortInsert(root->right);
        return;
    }
    
    TreeNode* KthNode(TreeNode* root, int k) {
        if (root == nullptr or k <= 0) {
            return nullptr;
        }
        
        // 按照大小顺序插入排序
        sortInsert(root);
        
        // 返回第三个值
        if (k > tmp.size()) {
            return nullptr;
        }
        
        return tmp[k - 1];
    }
};

//高效方法：
//中序遍历第k个即可，利用全局变量来

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
    int index = 0;
    
    TreeNode* KthNode(TreeNode* root, int k) {
        if (root == nullptr or k <= 0) {
            return nullptr;
        }
        
        TreeNode* tmp;
        tmp = KthNode(root->left, k);
        if (tmp) { // 需要提前检测是否要返回
            return tmp;
        }
        
        if (++index == k) {
            return root;
        }
        
        tmp = KthNode(root->right, k);
        if (tmp) { // 需要提前检测是否要返回
            return tmp;
        }
        
        return nullptr; // 如果没有找到
    }
};