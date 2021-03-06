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

    // 对于INT_MAX越界，这里只是简单的跳过了
    // 默认最终正确的case没有超过INT_MAX的情况
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (int j = 1; j <= target; j++) {
            for (const int& num : nums) {
                if (j >= num && dp[j] < INT_MAX - dp[j - num]) {
                    dp[j] += dp[j - num];
                }
            }
        }
        return dp[target];
    }
};