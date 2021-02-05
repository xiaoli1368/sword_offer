#!/bin/bash python
"""
417. 太平洋大西洋水流问题

思路：
DFS/BFS
"""

class Solution(object):
	# ===== 错解 =====
    def dfs(self, matrix, flag, row, col, i, j):
        """
        进行DFS遍历
        返回当前位置所处的终点
        这里保证当前位置没有越界
        """
        # 如果遍历过，直接返回
        if flag[i][j] > 0:
            return flag[i][j]
        # 没有遍历过，但到达了边界
        elif (i == 0 and j == col - 1) or (j == 0 and i == row - 1):
            flag[i][j] = 4
        elif i == 0 or j == 0:
            flag[i][j] = 2
        elif i == row - 1 or j == col - 1:
            flag[i][j] = 3
        # 没有遍历过，且没有到达边界，递归寻找4各个方向终点
        else:
            curr = 1
            dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in dires:
                x, y = i + d[0], j + d[1]
                # 保证下一个节点不越界，且高度下降
                if 0 <= x < row and 0 <= y < col and matrix[i][j] >= matrix[x][y]:
                    nnext = self.dfs(matrix, flag, row, col, x, y)
                    if nnext == 4:
                        curr = 4
                        break
                    elif (nnext == 3 and curr == 2) or (nnext == 2 and curr == 3):
                        curr = 4 
                        break
                    curr = max(curr, nnext)
            flag[i][j] = curr
            # 这里存在问题，应该对4回溯w44，那么应该去遍历周围与它相等的位置也初始化为4
            # 也就是说一旦某个位置wei
        return flag[i][j]

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        感觉双向BFS可行（模拟全球海平面上升，两大洋淹没亚欧大陆，水漫金山，666）
        然后如果是DFS，那么必然要使用记忆化搜索
        遍历所有的位置，如果之前遍历过了，则跳过，如果没有遍历过则进入DFS
        内部递归向位置更低的地方遍历，如果最终可以到达太平洋或者大西洋
        则返回时同样给之前遍历过的位置记录最终到达的目的地
        """
        # 特殊情况
        if matrix == []:
            return 0
        
        # 初始化，flag中[0, 1, 2, 3, 4]表示[未遍历，均不可，可到太平洋，可到大西洋，均可]
        ret = []
        row = len(matrix)
        col = len(matrix[0])
        flag = [[0] * col for _ in range(row)]

        # 获取当前位置[i, j]的终点状态
        for i in range(row):
            for j in range(col):
                if self.dfs(matrix, flag, row, col, i, j) == 4:
                    ret.append([i, j])
        #print(flag)
        return ret
	
    # ===== 正解DFS =====
    def dfs(self, matrix, flag, row, col, index, i, j):
        """
        进行DFS，从(i, j)位置水漫金山并且标记可以到达的位置
        保证没有越界，且没有遍历过
        """
        flag[i][j][index] = 1
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in dires:
            x, y = i + d[0], j + d[1]
            # 下一层不越界，未遍历，且高度递增
            if 0 <= x < row and 0 <= y < col and matrix[x][y] >= matrix[i][j] and flag[x][y][index] == 0:
                self.dfs(matrix, flag, row, col, index, x, y)
        return

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        从四条边开始水漫金山
        使用DFS/BFS标记当前方格可以到达那片海洋
        最终遍历得到结果
        """
        # 特殊情况
        if matrix == []:
            return []
        
        # 初始化
        ret = []
        row = len(matrix)
        col = len(matrix[0])
        flag = [[[0] * 2 for _ in range(col)] for _ in range(row)]

        # 按行水漫金山
        for i in range(row):
            self.dfs(matrix, flag, row, col, 0, i, 0)
            self.dfs(matrix, flag, row, col, 1, i, col - 1)
        
        # 按列水漫金山
        for j in range(col):
            self.dfs(matrix, flag, row, col, 0, 0, j)
            self.dfs(matrix, flag, row, col, 1, row - 1, j)
        
        # 进行遍历
        for i in range(row):
            for j in range(col):
                if flag[i][j][0] + flag[i][j][1] == 2:
                    ret.append([i, j])
        return ret
	
	# ===== 正解BFS =====
    def bfs(self, matrix, flag, row, col, queue, index):
        """
        进行BFS，从queue开始水漫金山并且标记可以到达的位置
        """
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.pop()
            flag[i][j][index] = 1
            for d in dires:
                x, y = i + d[0], j + d[1]
                # 下一层不越界，未遍历，且高度递增
                if 0 <= x < row and 0 <= y < col and matrix[x][y] >= matrix[i][j] and flag[x][y][index] == 0:
                    queue.append((x, y))
        return

    def pacificAtlantic(self, matrix):
        """
        从四条边开始水漫金山
        使用DFS/BFS标记当前方格可以到达那片海洋
        最终遍历得到结果
        """
        # 特殊情况
        if matrix == []:
            return []
        
        # 初始化
        ret = []
        row = len(matrix)
        col = len(matrix[0])
        flag = [[[0] * 2 for _ in range(col)] for _ in range(row)]

        # 统计水漫金山的两个队列
        queueP = []
        queueA = [] 
        for i in range(row):
            queueP.append((i, 0))
            queueA.append((i, col - 1))
        for j in range(col):
            queueP.append((0, j))
            queueA.append((row - 1, j))
        self.bfs(matrix, flag, row, col, queueP, 0)
        self.bfs(matrix, flag, row, col, queueA, 1)
        
        # 进行遍历
        for i in range(row):
            for j in range(col):
                if flag[i][j][0] + flag[i][j][1] == 2:
                    ret.append([i, j])
        return ret