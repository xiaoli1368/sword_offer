class Solution {
public:
    // 注意答案不会int溢出，但是中间状态有可能溢出
    int numDistinct(string s, string t) {
        int row = 1 + t.size(), col = 1 + s.size();
        vector<vector<long>> dp(row, vector<long>(col, 0));
        dp[0] = vector<long>(col, 1);
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (s[j - 1] != t[i - 1]) {
                    dp[i][j] = dp[i][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
                }
            }
        }
        return dp[row - 1][col - 1];
    }
};