class Solution {
public:
	// ===== 常规DP版本 =====
    int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        vector<int> dp = nums;
        for (int i = 1; i < dp.size(); i++) {
            int currMax = (i < 2 ? nums[i] : nums[i] + dp[i - 2]);
            dp[i] = max(dp[i - 1], currMax);
        }
        return dp.back();
    }

	// ===== DP状态空间优化版本 =====
	int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        } else if (nums.size() == 1) {
            return nums[0];
        }
        int a = nums[0], b = max(nums[0], nums[1]), c = 0;
        for (int i = 2; i < nums.size(); i++) {
            c = max(b, a + nums[i]);
            a = b;
            b = c;
        }
        return b;
    }

	// ===== 究极优化版本 =====
    int rob(vector<int>& nums) {
        int prev = 0, curr = 0, tmp = 0;
        for (const auto & val : nums) {
            tmp = max(curr, prev + val);
            prev = curr;
            curr = tmp;
        }
        return curr;
    }
};