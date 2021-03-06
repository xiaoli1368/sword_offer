class Solution {
public:
    void count(const string& s, int& cnt0, int& cnt1) {
        cnt0 = 0, cnt1 = 0;
        for (const char& c : s) {
            if (c == '0') cnt0++;
            if (c == '1') cnt1++;
        }
        return;
    }

    int findMaxForm(vector<string>& strs, int m, int n) {
        if (strs.empty() || m < 0 || n < 0) {
            return 0;
        }

        int mi = 0, ni = 0;
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (const auto & s : strs) {
            count(s, mi, ni);
            for (int i = m; i >= mi; i--) {
                for (int j = n; j >= ni; j--) {
                    dp[i][j] = max(dp[i][j], dp[i - mi][j - ni] + 1);
                }
            }
        }
        return dp[m][n];
    }
};