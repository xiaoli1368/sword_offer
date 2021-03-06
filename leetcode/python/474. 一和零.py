#!/bin/bash python
"""
474. 一和零

思路：
动态规划，背包问题
"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        看作01背包问题，每个元素都有取或者不取两种情况
        但是重量则有两个维度，(m, n)，不能超过(m, n)
        要求子集包含元素最大，也就是每个元素的价值为1，要求更多的元素
        dp[i][m][n]，表示前i个元素，在重量最大为(m, n)的情况下的最大价值
        dp[i][m][n] = max(dp[i - 1][m][n], dp[i - 1][m - mi][n - ni] + 1)
        优化1：考虑到i只与i-1有关，因此为迭代i次，dp[m][n] = max(dp[m][n], dp[m-mi][n-ni] + 1)
        优化2：考虑到每个元素的重量(mi, ni)需要实时count，因此可以提前使用O(n)来存储
        """
        if strs == [] or m < 0 or n < 0:
            return 0
        
        weights = [[0] * 2 for _ in range(len(strs))]
        for i in range(len(strs)):
            weights[i][0] = strs[i].count("0")
            weights[i][1] = strs[i].count("1")
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(strs)):
            mi, ni = weights[i]
            for x in range(m, mi - 1, -1):
                for y in range(n, ni - 1, -1):
                    dp[x][y] = max(dp[x][y], dp[x - mi][y - ni] + 1)
        return dp[-1][-1]

class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        优化版
        不需要O(n)空间来存储weights
        因为每个weights[i]只用一次，因此直接计算就行了
        并且直接对元素遍历就行了
        """
        if strs == [] or m < 0 or n < 0:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            mi, ni = s.count("0"), s.count("1")
            for i in range(m, mi - 1, -1):
                for j in range(n, ni - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - mi][j - ni] + 1)
        return dp[-1][-1]