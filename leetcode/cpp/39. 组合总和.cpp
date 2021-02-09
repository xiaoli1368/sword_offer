class Solution {
public:
    void dfs(vector<vector<int>>& ret, vector<int>& path, const vector<int>& nums, int target, int i) {
        if (target == 0) {
            ret.push_back(path);
        } else if (target > 0 && i < nums.size()) {
            dfs(ret, path, nums, target, i + 1); // 当前不选
            path.push_back(nums[i]); // 选取当前，但是下一层仍然是i
            dfs(ret, path, nums, target - nums[i], i);
            path.pop_back();
        }
        return;
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!candidates.empty()) {
            dfs(ret, path, candidates, target, 0);
        }
        return ret;
    }
};