class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int ret = 0, n = A.size();
        vector<unordered_map<long, int>> dp(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diff = long(A[i]) - A[j];
                dp[i][diff] += 1;
                if (dp[j].count(diff) > 0) {
                    dp[i][diff] += dp[j][diff];
                    ret += dp[j][diff];
                }
            }
        }
        return ret;
    }
};