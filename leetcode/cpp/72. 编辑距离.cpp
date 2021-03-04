class Solution {
public:
    int min3(const int& a, const int& b, const int& c) {
        return min(min(a, b), c);
    }

    int minDistance(string word1, string word2) {
        int row = word2.size(), col = word1.size();
        vector<vector<int>> dp(row + 1, vector<int>(col + 1, 0));
        for (int i = 0; i <= row; i++) {
            for (int j = 0; j <= col; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 0;
                } else if (i == 0) {
                    dp[i][j] = 1 + dp[i][j - 1];
                } else if (j == 0) {
                    dp[i][j] = 1 + dp[i - 1][j];
                } else if (word2[i - 1] == word1[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min3(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        return dp[row][col];
    }
};