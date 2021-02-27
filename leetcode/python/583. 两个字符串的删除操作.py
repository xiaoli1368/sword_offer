#!/bin/bash python
"""
583. 两个字符串的删除操作

思路：
动态规划
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
          "" s e a
        "" 0 1 2 3
        e  1 2 1 2
        a  2 3 2 1
        t  3 4 3 2
        dp[i][j]表示a[i]和b[j]结尾的字符串的最小操作步数
        dp[i] = dp[i - 1][j - 1], if a[i] == b[j]
        dp[i] = 1 + min(dp[i][j - 1], dp[i - 1][j], if a[i] != b[j])
        """
        row = len(word1) + 1
        col = len(word2) + 1
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = 1 + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = 1 + dp[i - 1][j]
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]