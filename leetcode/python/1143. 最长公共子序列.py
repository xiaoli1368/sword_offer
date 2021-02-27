#!/bin/bash python
"""
1143. 最长公共子序列

思路：
动态规划
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
          "" a b c d e
        "" 0 0 0 0 0 0
        a  0 1 1 1 1 1
        c  0 1 1 2 2 2
        e  0 1 1 2 2 3
        dp[i][j] = 1 + dp[i - 1][j - 1], if a[i] == b[j]
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], if a[i] != b[j])
        """
        row, col = 1 + len(text1), 1 + len(text2)
        dp = [[0] * col for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]