class Solution {
public:
    int mergeStones(vector<int>& stones, int kk) {
        int n = stones.size();
        if ((n - 1) % (kk - 1) != 0) {
            return -1;
        }
        vector<int> pre_sum(n + 1, 0);
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 1; i <= n; i++) {
            pre_sum[i] = pre_sum[i - 1] + stones[i - 1];
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                int mmin_cost = INT_MAX, curr_cost;
                for (int m = i; m < j; m += kk - 1) {
                    curr_cost = ((j - i) % (kk - 1) == 0 ? pre_sum[j + 1] - pre_sum[i] : 0);
                    mmin_cost = min(mmin_cost, dp[i][m] + dp[m + 1][j] + curr_cost);
                }
                dp[i][j] = (mmin_cost == INT_MAX ? 0 : mmin_cost);
            }
        }
        return dp[0][n - 1];
    }
};