class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i] + nums[i];
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == dp[n] - dp[i + 1]) {
                return i;
            }
        }
        return -1;
    }
};