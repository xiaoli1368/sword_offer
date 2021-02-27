class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        if (word1.empty() || word2.empty()) {
            return 0;
        }

        string s = word1 + word2;
        int n1 = word1.size(), n = s.size(), ret = 0; 
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[i][j] = 1;
                } else if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                    if (i < n1 && n1 <= j) {
                        ret = max(ret, dp[i][j]);
                    }
                } else {
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
                }
            }
        }
        return ret;
    }
};