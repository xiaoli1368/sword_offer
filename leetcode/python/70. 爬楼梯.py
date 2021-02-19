#!/bin/bash python
"""
70. 爬楼梯

思路：
1. 直接递归
2. 动态规划
3. 动态规划 + 状态压缩 = 变量迭代
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n + 1))
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b