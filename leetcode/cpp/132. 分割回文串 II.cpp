class Solution {
public:
    int minCut(string s) {
        if (s.empty()) {
            return 0;
        }

        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, true));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = (s[i] == s[j] && dp[i + 1][j - 1]);
            }
        }

        vector<int> dp2(n + 1, n);
        dp2[0] = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i <= j; i++) {
                if (dp[i][j] == true) {
                    dp2[j + 1] = min(dp2[j + 1], 1 + dp2[i]);
                }
            }
        }
        return dp2.back() - 1;
    }
};