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

    # ===== BFS的方式 =====
    def bfs(self, grid, dires, row, col, i, j):
        """
        进行BFS
        确保进入的位置为1
        """
        grid[i][j] = "2"
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            for d in dires:
                x, y = i + d[0], j + d[1]
                if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                    grid[x][y] = "2"
                    queue.append((x, y))
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS
        0表示水，1表示未遍历过的岛屿，2表示已经遍历过的岛屿
        """
        # 特殊情况
        if grid == []:
            return 0
        
        # 初始化
        cnt = 0
        row, col = len(grid), len(grid[0])
        dires = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # 二重循环并进行BFS
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    cnt += 1
                    self.bfs(grid, dires, row, col, i, j)
        return cnt