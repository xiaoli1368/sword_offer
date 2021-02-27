#!/bin/bash python
"""
712. 两个字符串的最小ASCII删除和

思路：
动态规划
"""

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        所有字母均为小写，因此可以映射a-z为1-26
          ""  s   e   a
        "" 0  19  24  25
        e  5  24  19  20
        a  6  25  20  19
        t  26 45  40  39
        最终删掉两个字符为st，总花费为：39 + 96 * 2 = 231
        dp[i][j]表示a[i]与b[j]结尾的两字符串的最小删除和
        dp[i][j] = dp[i - 1][j - 1], if a[i] == b[j]
        dp[i][j] = min(ord(a[i]) + dp[i - 1][j], ord(b[j]) + dp[i][j - 1])
        """
        row, col = 1 + len(s1), 1 + len(s2)
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + ord(s2[j - 1]) 
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + ord(s1[i - 1])
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1])
        return dp[-1][-1]