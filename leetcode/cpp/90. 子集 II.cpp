class Solution {
public:
    void dfs(vector<vector<int>>& ret, vector<int>& path, const vector<int>& nums, int last, int i) {
        if (i >= nums.size()) {
            ret.push_back(path);
            return;
        }
        dfs(ret, path, nums, last, i + 1);
        if (find(nums.begin() + last + 1, nums.begin() + i, nums[i]) == nums.begin() + i) {
            path.push_back(nums[i]);
            dfs(ret, path, nums, i, i + 1);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!nums.empty()) {
            sort(nums.begin(), nums.end());
            dfs(ret, path, nums, -1, 0);
        }
        return ret;
    }

	// ===== 与排列兼容的方式 =====
	void dfs(vector<vector<int>>& ret, vector<int>& path, const vector<int>& nums, int i) {
        ret.push_back(path);
        if (i >= nums.size()) {
            return;
        }
        for (int j = i; j < nums.size(); j++) {
            if (find(nums.begin() + i, nums.begin() + j, nums[j]) != nums.begin() + j) {
                continue;
            }
            path.push_back(nums[j]);
            dfs(ret, path, nums, j + 1);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!nums.empty()) {
            sort(nums.begin(), nums.end());
            dfs(ret, path, nums, 0);
        }
        return ret;
    }
};