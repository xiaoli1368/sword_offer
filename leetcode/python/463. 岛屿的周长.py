#!/bin/bash python
"""
463. 岛屿的周长

思路：直接dfs回溯法，统计各个陆地周围的边（包括出界或者朝向水域的情况）
"""

class Solution(object):
    def __init__(self):
        self.ret = 0
    
    def dfs(self, grid, flag, n, m, i, j):
        """
        回溯法
        """
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
            self.ret += 1
            return
        if flag[i][j] == True:
            return
        flag[i][j] = True
        self.dfs(grid, flag, n, m, i - 1, j)
        self.dfs(grid, flag, n, m, i + 1, j)
        self.dfs(grid, flag, n, m, i, j - 1)
        self.dfs(grid, flag, n, m, i, j + 1)
        return

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        回溯法，记录每个陆地周围是海的边数
        """
        m = len(grid)
        n = len(grid[0])
        flag = [[False] * n for _ in range(m)]

        # 找到陆地的入口
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, flag, m, n, i, j)
                    return self.ret