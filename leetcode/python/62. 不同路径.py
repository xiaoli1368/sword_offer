#!/bin/bash python
"""
62. 不同路径

思路：
正常的二维DP
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                top = dp[i - 1][j] if i >= 1 else 0
                lef = dp[i][j - 1] if j >= 1 else 0
                dp[i][j] = top + lef
        return dp[-1][-1]