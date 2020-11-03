#include <vector>
#include <stack>
#include <map>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    std::vector<int> ret;
public:
    // 递归法
    std::vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return ret;
        }

        postorderTraversal(root->left);
        postorderTraversal(root->right);
        ret.push_back(root->val);

        return ret;
    }

    // 状态标记法
    std::vector<int> postorderTraversal2(TreeNode* root) {
        std::vector<int> ret;
        std::stack<std::pair<TreeNode*, bool>> stack;
        if (root) {
            stack.push(std::make_pair(root, false));
        }
        while (!stack.empty()) {
            std::pair<TreeNode*, bool> node = stack.top();
            stack.pop();
            if (node.second) {
                ret.push_back(node.first->val);
                continue;
            }
            stack.push(std::make_pair(node.first, true));
            if (node.first->right) {
                stack.push(std::make_pair(node.first->right, false));
            }
            if (node.first->left) {
                stack.push(std::make_pair(node.first->left, false));
            }
        }
        return ret;
    }

	// 更加高效的迭代方法
	vector<int> postorderTraversal3(TreeNode* root) {
		std::vector<int> ret;
		std::stack<TreeNode*> stack;
		TreeNode* curr = root;
		TreeNode* prev = nullptr;
		while (!stack.empty() || curr) {
			// 遍历左子树
			while (curr) {
				stack.push(curr);
				curr = curr->left;
			}
			// 获取根节点
			curr = stack.top();
			stack.pop();
			if (curr->right && curr->right != prev) {
				// 遍历右子树
				stack.push(curr);
				curr = curr->right;
			} else {
				// 遍历根节点
				ret.push_back(curr->val);
				prev = curr;
				curr = nullptr;
			}
		}
		return ret;
	}
};