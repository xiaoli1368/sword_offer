class Solution {
public:
    void dfs(vector<vector<int>>& ret, const vector<int>& nums, vector<int>& path, int i) {
        if (i >= nums.size()) {
            ret.push_back(path);
            return;
        }
        dfs(ret, nums, path, i + 1);
        path.push_back(nums[i]);
        dfs(ret, nums, path, i + 1);
        path.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!nums.empty()) {
            dfs(ret, nums, path, 0);
        }
        return ret;
    }

	// ===== 更加兼容排列的写法 =====
    void dfs(vector<vector<int>>& ret, const vector<int>& nums, vector<int>& path, int i) {
        ret.push_back(path);
        if (i >= nums.size()) {
            return;
        }
        for (int j = i; j < nums.size(); j++) {
            path.push_back(nums[j]);
            dfs(ret, nums, path, j + 1);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!nums.empty()) {
            dfs(ret, nums, path, 0);
        }
        return ret;
    }
};