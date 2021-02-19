class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }

    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        long dp[n + 1];
        dp[1] = 1, dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

	int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int a = 1, b = 2, c = 3;
        for (int i = 3; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};