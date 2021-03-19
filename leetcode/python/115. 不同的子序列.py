#!/bin/bash python
"""
115. 不同的子序列

思路：
动态规划
"""

class Solution(object):
    def numDistinct(self, s: str, t: str) -> int:
        """
        1. 暴力方法：生成s的所有子序列，找到与t相同的个数
        2. 回溯剪枝：对s[i]进行回溯，每个元素是否选择，同时保证和t[j]字符相等
        3. 动态规划：dp[i][j]表示s[i]的子序列中包括t[j]的个数
                    dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i] == t[j] else 0)
        """
        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            return dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)
        return dfs(0, 0)

    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        理解为字符串编辑，编辑方式只有一种：删除当前位置
        要求由s编辑得到t，共有多少种方法
        dp[i][j]表示由s[:j]编辑得到t[:i]的方法数量
        if s[j] == t[i]: dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        if s[j] != t[i]: dp[i][j] = dp[i][j - 1]
        初始化，注意第一行为1，第一列为0
            "" b  a  b  g  b  a  g
        ""  1  1  1  1  1  1  1  1
        b   0  1  1  2  2  3  3  3  
        a   0  0  1  1  1  1  4  4
        g   0  0  0  0  1  1  1  5
        """
        row, col = 1 + len(t), 1 + len(s)
        dp = [[1 if i == 0 else 0] * col for i in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                if s[j - 1] != t[i - 1]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        return dp[-1][-1]