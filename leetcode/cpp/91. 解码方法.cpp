class Solution {
public:
    int numDecodings(string s) {
        if (s.empty()) {
            return 0;
        }
        vector<int> dp(s.size() + 1, 0);
        dp[0] = 1;
        for (int i = 0; i < s.size(); i++) {
            if (i >= 0 && s[i] >= '1') {
                dp[i + 1] += dp[i];
            }
            if (i >= 1 && s[i - 1] != '0' && s.substr(i - 1, 2) <= "26") {
                dp[i + 1] += dp[i - 1];
            }
            if (dp[i + 1] == 0) {
                break;
            }
        }
        return dp.back();
    }
};