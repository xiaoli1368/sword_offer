#!/bin/bash python
"""
64. 最小路径和

思路：
动态规划
1. 标志二维DP
2. 不使用额外空间，直接原地修改
3. 不允许改变原始数组，对额外空间进行状态压缩
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        二维dp
        dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        """
        if grid == []:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        优化：不使用dp，直接原地迭代
        """
        if grid == []:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue 
                top = grid[i - 1][j] if i >= 1 else float("+inf")
                lef = grid[i][j - 1] if j >= 1 else float("+inf")
                grid[i][j] += min(top, lef)
        return grid[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        二维dp状态压缩
        dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        因为dp[i][j]只与左侧一位，与上方一位有关，因此状态压缩为一维空间
        """
        if grid == []:
            return 0
        dp = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = grid[i][j] + dp[j - 1]
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        return dp[-1]