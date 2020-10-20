#include <vector>
#include <map>

typedef struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int val=0) : val(val), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
public:
    // 中序遍历生成哈希
	void mid(TreeNode* root, std::map<int, bool>& map) {
		if (root == nullptr) {
			return;
		}
		map[root->val] = true;
		mid(root->left, map);
		mid(root->right, map);
		return;
	}

	// 中序遍历生成有序数组
	void mid(TreeNode* root, std::vector<int>& vec) {
		if (root == nullptr) {
			return;
		}
		mid(root->left, vec);
		vec.push_back(root->val);
		mid(root->right, vec);
		return;
	}

	// 哈希法
	bool findTarget(TreeNode* root, int k) {
		std::map<int, bool> map;
		mid(root, map);
		for (auto it = map.begin(); it != map.end(); it++) {
			int val = it->first;
			if (val * 2 != k && map.count(k - val)) {
				return true;
			}
		}
		return false;
	}

	// 双指针
	bool findTarget2(TreeNode* root, int k) {
		std::vector<int> vec;
		mid(root, vec);
		int l = 0, r = vec.size() - 1;
		while (l < r) {
			int sum = vec[l] + vec[r];
			if (sum == k) {
				return true;
			} else if (sum < k) {
				l += 1;
			} else {
				r -= 1;
			}
		}
		return false;
	}
};