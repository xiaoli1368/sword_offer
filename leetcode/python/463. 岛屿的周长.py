#!/bin/bash python
"""
463. 岛屿的周长

思路：
1. 可以直接二维循环遍历，统计每个陆地周围的水域情况，并累计与水域相邻的边数，复杂度O(m*n*4)
2. 直接dfs回溯法，统计各个陆地周围的边（包括出界或者朝向水域的情况），复杂度要小，因此只用遍历陆地
3. 思考优化空间，一是只需要对陆地遍历即可，二是针对每个陆地都要检测4个朝向，这里当两个陆地相邻时
   第一个陆地检测完后，可以进行标记，那么第二个陆地便不需要检测该方向了（这里存在优化空间）
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

	# ===== 二重循环法 =====
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        统计一个陆地方格，周围有多少条边与水域接壤
        因为只有一个岛屿，因此所有的陆地一定是接壤的
        那么直接遍历所有的方格即可
        """
        # 特殊情况
        if grid == []:
            return 0
        
        # 初始化
        ret = 0
        row = len(grid)
        col = len(grid[0])
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 直接遍历
        for i in range(row):
            for j in range(col):
                # 当前位置为陆地
                if grid[i][j] == 1:
                    # 遍历4个方向判断是否为海洋或者越界了
                    for d in dires:
                        x, y = i + d[0], j + d[1]
                        if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0:
                            ret += 1
        return ret