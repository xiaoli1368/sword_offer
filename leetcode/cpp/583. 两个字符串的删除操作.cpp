class Solution {
public:
    int minDistance(string word1, string word2) {
        int row = 1 + word1.size();
        int col = 1 + word2.size();
        vector<vector<int>> dp(row, vector<int>(col, 0));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 0;
                } else if (i == 0) {
                    dp[i][j] = 1 + dp[i][j - 1];
                } else if (j == 0) {
                    dp[i][j] = 1 + dp[i - 1][j];
                } else if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        return dp.back().back();
    }
};