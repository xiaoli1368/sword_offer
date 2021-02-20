#!/bin/bash python
"""
63. 不同路径 II

思路：
常规DP，增加对当前方格是否为障碍物的判断
"""

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        在原来的基础上，考虑当前网格是否为障碍物
        dp[i][j] = 0 # 障碍物
        dp[i][j] = grid[i][j] + min(dp[i-1][j], d[i][j-1])
        """
        if grid == []:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = 1 - grid[i][j] # 将障碍物处理为0
                if grid[i][j] == 0 or (i == 0 and j == 0):
                    continue
                top = grid[i - 1][j] if i >= 1 else 0
                lef = grid[i][j - 1] if j >= 1 else 0
                grid[i][j] = top + lef
        return grid[-1][-1]