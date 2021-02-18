#!/bin/bash python
"""
994. 腐烂的橘子

思路：
BFS
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        与leetcode542很像
        1. 暴力检索找到腐烂的橘子
        2. 进行水漫金山
        注意直接使用grid作为是否遍历过的flag
        """
        # 特殊情况
        if grid == []:
            return 0
        
        # 初始化
        queue = []
        row, col = len(grid), len(grid[0])
        dires = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        # 找到腐烂的橘子，并统计新鲜的橘子个数
        newOrange = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    newOrange += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # 如果初始情况就没有新鲜的橘子
        if newOrange == 0:
            return 0
        
        # BFS
        time = -1
        while queue:
            time += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                for d in dires:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        newOrange -= 1
                        grid[x][y] = 2
                        queue.append((x, y))
        
        # 返回是否没有新鲜橘子
        return time if newOrange == 0 else -1