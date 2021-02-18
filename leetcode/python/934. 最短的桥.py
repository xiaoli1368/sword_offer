#!/bin/bash python
"""
934. 最短的桥

思路：
1. 先暴力检索得到第一个岛屿的入口
2. 使用DFS完成对第一个岛屿的标记
3. 使用BFS完成两个岛屿最短路径的判断
"""

class Solution(object):
    def dfs(self, vec, flag, dires, ret, row, col, i, j):
        """
        进行DFS遍历，找到第一座岛屿
        从[i,j]作为入口，将第一座岛屿连通的坐标保存到ret中
        """
        # 没有越界，没有遍历过，是岛屿
        if 0 <= i < row and 0 <= j < col and not flag[i][j] and vec[i][j] == 1:
            flag[i][j] = True
            ret.append((i, j))
            for d in dires:
                x, y = i + d[0], j + d[1]
                self.dfs(vec, flag, dires, ret, row, col, x, y)
        return
    
    def bfs(self, vec, queue, flag, dires, row, col):
        """
        进行BFS
        判断由当前queue广度搜索到下一层的1的最短路径
        """
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                for d in dires: # 遍历下一层的四个方向
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < row and 0 <= y < col and flag[x][y] == False:
                        if vec[x][y] == 1: # 找到了
                            return step
                        else:
                            flag[x][y] = True
                            queue.append((x, y))
            step += 1
        return step

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        先二重循环遍历找到第一个1
        然后进行一层的BFS，找到周围的1
        然后进行二层的BFS，找到周围的0
        然后进行N层的BFS，直到找到1
        """
        # 特殊情况
        if A == []:
            return 0
        # 初始化
        queue = []
        row, col = len(A), len(A[0])
        flag = [[False] * col for _ in range(row)]
        dires = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # 找到第一座岛屿后，直接DSF/BFS
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    self.dfs(A, flag, dires, queue, row, col, i, j)
                    return self.bfs(A, queue, flag, dires, row, col)
        return 0