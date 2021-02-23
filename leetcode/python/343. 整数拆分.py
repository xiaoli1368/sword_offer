#!/bin/bash python
"""
343. 整数拆分

思路：
贪心法，或者DP
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
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        """
        DP
        """
        if n <= 1:
            return n
        dp = [1] * (n + 1)
        for i in range(n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        return dp[n]

    def integerBreak(self, n):
        """
        贪心法
        """
        if n <= 3:
            return n - 1
        cnt3 = n//3-1 if n % 3 == 1 else n // 3
        cnt2 = (n - 3 * cnt3) // 2
        return 3**cnt3 * 2**cnt2