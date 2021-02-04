#!/bin/bash python
"""
695. 岛屿的最大面积

思路：
正常DFS
"""

class Solution:
    def dfs(self, grid, flag, row, col, i, j):
        """
        进行dfs遍历
        把(i, j)周围相邻的陆地，标记为已遍历
        """
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0 or flag[i][j] == True:
            return
        self.area += 1
        flag[i][j] = True
        self.dfs(grid, flag, row, col, i + 1, j)
        self.dfs(grid, flag, row, col, i - 1, j)
        self.dfs(grid, flag, row, col, i, j + 1)
        self.dfs(grid, flag, row, col, i, j - 1)
        return
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        DFS
        """
        # 特殊情况
        if grid == []:
            return 0
        
        # 初始化
        ret = 0
        row = len(grid)
        col = len(grid[0])
        flag = [[False] * col for _ in range(row)]

        # 进行遍历
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and flag[i][j] == False:
                    self.area = 0
                    self.dfs(grid, flag, row, col, i, j)
                    ret = max(ret, self.area)
        return ret