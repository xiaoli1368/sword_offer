class Solution {
public:
	// ===== 动态规划 =====
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int ret = 1;
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            ret = max(ret, dp[i]);
        }
        return ret;
    }

	// ===== 贪心 + 二分 =====
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        vector<int> dp;
        for (const int& num : nums) {
            if (dp.empty() || dp.back() < num) {
                dp.push_back(num);
            } else {
                auto itr = lower_bound(dp.begin(), dp.end(), num);
                *itr = num;
            }
        }
        return dp.size();
    }
};