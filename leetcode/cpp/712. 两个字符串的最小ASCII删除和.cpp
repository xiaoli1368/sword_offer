class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int row = 1 + s1.size(), col = 1 + s2.size();
        vector<vector<int>> dp(row, vector<int>(col, 0));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 0;
                } else if (i == 0) {
                    dp[i][j] = dp[i][j - 1] + s2[j - 1];
                } else if (j == 0) {
                    dp[i][j] = dp[i - 1][j] + s1[i - 1];
                } else if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
                }
            }
        }
        return dp.back().back();
    }
};