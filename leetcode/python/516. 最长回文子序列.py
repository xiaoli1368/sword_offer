#!/bin/bash python
"""
516. 最长回文子序列

思路：
动态规划
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        dp[i][j]表示区间[i,j]内的最长回文子序列长度，并不一定包含两端
        dp[i][j] = 2 + dp[i + 1][j - 1], if s[i] == s[j]
        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]), if s[i] != s[j]
        因此i依赖于i+1, j依赖于j-1，因此i从大到小遍历，j从小到大遍历
        并且需要保证 i <= j
        """
        if s == "":
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]