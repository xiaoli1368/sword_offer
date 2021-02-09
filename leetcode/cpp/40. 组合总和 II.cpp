class Solution {
public:
    void dfs(vector<vector<int>>& ret, vector<int>& path, const vector<int>& nums, int target, int i) {
        if (target == 0) {
            ret.push_back(path);
        } else if (target > 0 && i < nums.size()) {
            for (int j = i; j < nums.size(); j++) {
                if (find(nums.begin() + i, nums.begin() + j, nums[j]) == nums.begin() + j) {
                    path.push_back(nums[j]);
                    dfs(ret, path, nums, target - nums[j], j + 1);
                    path.pop_back();
                }
            }
        }
        return;
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> path;
        vector<vector<int>> ret;
        if (!candidates.empty()) {
            sort(candidates.begin(), candidates.end());
            dfs(ret, path, candidates, target, 0);
        }
        return ret;
    }
};