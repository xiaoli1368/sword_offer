class Solution {
public:
    int numSquares(int n) {
        if (n <= 0) {
            return 0;
        }
        int sqrt = 1;
        vector<int> dp(n + 1, n);
        for (int i = 1; i <= n; i++) {
            if (i == sqrt * sqrt) {
                dp[i] = 1;
                sqrt += 1;
                continue;
            }
            for (int j = 1; j < sqrt; j++) {
                dp[i] = min(dp[i], 1 + dp[i - j * j]);
            }
        }
        return dp[n];
    }

	// ===== 优化方式 =====
	// 只是看起来简化了，但是对于完全平方数的处理，存在冗余
	int numSquares(int n) {
        vector<int> dp(n + 1, n);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = min(dp[i], 1 + dp[i - j * j]);
            }
        }
        return dp[n];
    }
};