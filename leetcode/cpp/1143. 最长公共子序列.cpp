class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int row = 1 + text1.size();
        int col = 1 + text2.size();
        vector<vector<int>> dp(row, vector<int>(col, 0));
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp.back().back();
    }
};