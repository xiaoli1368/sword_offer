class Solution {
public:
    int my_abs(const int& x) {
        return (x >= 0 ? x : -x);
    }
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size(), sum = accumulate(nums.begin(), nums.end(), 0);
        if (my_abs(S) > sum) {
            return 0;
        }
        int row = n + 1, col = 2 * sum + 1, curr;
        vector<vector<int>> dp(row, vector<int>(col, 0));
        dp[0][sum] = 1;
        for (int i = 1; i < row; i++) {
            curr = my_abs(nums[i - 1]);
            for (int j = 0; j < col; j++) {
                if (j >= curr) dp[i][j] += dp[i - 1][j - curr];
                if (j < col - curr) dp[i][j] += dp[i - 1][j + curr];
            }
        }
        return dp[n][S + sum];
    }
};