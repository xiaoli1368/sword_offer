class Solution {
public:
    void dfs(int& ret, const vector<int>& nums, int target) {
        if (target == 0) {
            ret += 1;
        } else if (target > 0) {
            for (const auto & i : nums) {
                dfs(ret, nums, target - i);
            }
        }
        return;
    }

    int combinationSum4(vector<int>& nums, int target) {
        int ret = 0;
        if (!nums.empty() && target > 0) {
            dfs(ret, nums, target);
        }
        return ret;
    }
};