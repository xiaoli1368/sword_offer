#!/bin/bash python
"""
132. 分割回文串 II

思路：
无脑DFS也可以，不过复杂度较大
动态规划 + 另一个动态规划
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        第一步，还是得预处理得到回文子串的信息
        第二步，思考能否进行动态规划，dp[j]表示区间[0:j]的最少回文串个数
               dp[j] = 1 + min(dp[i])，i表示j左侧相邻的上一次最少回文串个数
        综上所述，两次动态规划
        """
        if s == "":
            return 0
        
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        
        dp2 = [0] + [n] * n
        for j in range(n):
            for i in range(j + 1):
                if dp[i][j] == True:
                    dp2[j + 1] = min(dp2[j + 1], 1 + dp2[i])
        return dp2[-1] - 1