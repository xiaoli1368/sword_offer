#!/bin/bash python
"""
131. 分割回文串

思路：
回文子串预处理 + 回溯
预处理可以是动态规划或者中心延拓法
"""

class Solution(object):
    def dfs(self, ret, path, dp, s, n, i):
        """
        回溯法
        i表示当前正在遍历索引i
        """
        if i >= n:
            ret.append(path[:])
            return
        for j in range(i, n):
            if dp[i][j] == True:
                path.append(s[i:j+1])
                self.dfs(ret, path, dp, s, n, j + 1)
                path.pop()
        return

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        1. 先利用DP得到所有的回文子串
           dp[i][j]表示区间[i:j]是否为回文串
           dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
           遍历方式为：i -> [n, 0], j -> [0, n], 注意 i > j 情况下区间为空，结果为True
        2. 然后利用DFS回溯得到所有的分割方案
        """
        if s == "":
            return []
        
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        ret, path = [], []
        self.dfs(ret, path, dp, s, n, 0)
        return ret