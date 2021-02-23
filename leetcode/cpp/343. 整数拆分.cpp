class Solution {
public:
    // n次均值不等式，这n个数尽可能相等，则乘积最大
    // 接下来就是思考分为多少个数
    // 贪心策略：
    //     分1效率为负，分2/3效率较高，分4则效率变低
    //     以12为例，2^6 = 64, 3^4 = 81, 4^3 = 64，因此3效率最高，2/4次之，4与2等价
    //     贪心方法就是，优先分3，其次分2
    // 动态规划：
    //     dp[i]表示将正整数i拆分为两个正整数的和，所能得到的最大乘积
    //     尝试将i分为两部分，j与i-j，每部分又分别考虑是否仍然进行拆分
    //     dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j])), j = 1:i-1
    int integerBreak(int n) {
        if (n <= 1) {
            return n;
        }
        vector<int> dp(n + 1, 1);
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j * 2 <= i; j++) {
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]));
            }
        }
        return dp[n];
    }

	// ===== 贪心 + 快速幂 =====
    // 计算快速幂，b非负
    int quickPow(long a, int b) {
        int ret = 1;
        while (b) {
            if (b % 2 == 1) {
                ret *= a;
                b -= 1;
            }
            a *= a;
            b /= 2;
        }
        return ret;
    }
    
    int integerBreak(int n) {
        if (n <= 3) {
            return n - 1;
        }
        int cnt3 = (n % 3 == 1 ? n / 3 - 1 : n / 3);
        int cnt2 = (n - 3 * cnt3) / 2;
        return quickPow(3, cnt3) * quickPow(2, cnt2);
    }
};