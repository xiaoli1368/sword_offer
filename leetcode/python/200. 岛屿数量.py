#!/bin/bash python
"""
200. 岛屿数量

思路：
常规的DFS，这里一个值得思考的例子是遍历所有的1
一种方式是直接二重循环（前边已经遍历过的1会标记，使得后续不会重复遍历）
另一种方式是直接使用BFS来找打到所有的1（但总感觉这样不是很容易编程）
"""

class Solution(object):
    def dfs(self, grid, flag, row, col, i, j):
        """
        进行dfs遍历
        把(i, j)周围相邻的陆地，标记为已遍历
        """
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0" or flag[i][j] == True:
            return
        flag[i][j] = True
        self.dfs(grid, flag, row, col, i + 1, j)
        self.dfs(grid, flag, row, col, i - 1, j)
        self.dfs(grid, flag, row, col, i, j + 1)
        self.dfs(grid, flag, row, col, i, j - 1)
        return
        
    def numIslands(self, grid):
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
                if grid[i][j] == "1" and flag[i][j] == False:
                    ret += 1
                    self.dfs(grid, flag, row, col, i, j)
        return ret