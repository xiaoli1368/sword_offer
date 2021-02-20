class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m <= 0 || n <= 0) {
            return 0;
        }
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                int top = (i >= 1 ? dp[i - 1][j] : 0);
                int lef = (j >= 1 ? dp[i][j - 1] : 0);
                dp[i][j] = top + lef;
            }
        }
        return dp[m - 1][n - 1];
    }
};