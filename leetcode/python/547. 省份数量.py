#!/bin/bash python
"""
547. 省份数量

思路：
常规DFS，给定图的邻接矩阵，求连通域个数
"""

class Solution(object):
    def dfs(self, isConnected, visited, n, i):
        """
        DFS
        """
        visited.add(i)
        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                self.dfs(isConnected, visited, n, j)
        return
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        已知邻接矩阵，求连通域
        """
        # 特殊情况
        if isConnected == []:
            return 0
        # 开始遍历
        cnt = 0
        n = len(isConnected)
        visited = set()
        for i in range(n):
            if i not in visited:
                cnt += 1
                self.dfs(isConnected, visited, n, i)
        return cnt
	
	# ===== BFS的方式 ======
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        类似DBSCAN聚类
        外部BFS，内部DFS
        """
        if isConnected == [] or isConnected[0] == []:
            return 0
        
        cnt = 0 # 聚类个数
        n = len(isConnected) # 城市个数
        visited = set() # 已经遍历过的城市
        city = set(range(n)) # 剩余未遍历的城市

        while city:
            cnt += 1
            queue = [city.pop()]
            while queue:
                i = queue.pop(0) # 当前城市
                visited.add(i)
                for j in range(n): # 下一个城市
                    if isConnected[i][j] == 1 and j not in visited:
                        queue.append(j)
                        visited.add(j)
            city = city - visited
        return cnt