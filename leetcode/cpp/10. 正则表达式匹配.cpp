class Solution {
public:
    bool isMatch(string s, string p) {
        int row = s.size(), col = p.size();
        vector<vector<int>> dp(row + 1, vector<int>(col + 1, false));

        // 初始化第一行
        dp[0][0] = true;
        for (int j = 1; j <= col; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        // 正式的dp
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2] || dp[i][j - 2] || ((s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j]); 
                }
            }
        }
        return dp[row][col];
    }
};