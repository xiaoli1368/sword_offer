class Solution {
public:
    int countSubstrings(string s) {
        int ret = 0, n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, true));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = (s[i] == s[j] && dp[i + 1][j - 1]);
                ret += (dp[i][j] ? 1 : 0);
            }
        }
        return ret + n;
    }
};