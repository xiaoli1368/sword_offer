#!/bin/bash python
"""
542. 01 矩阵

思路：
1. DFS/BFS
2. 动态规划
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        类似洪水填充，洪水淹没，0是洪水，1是小岛
        一次遍历，找到所有第一级的1，然后开始bfs
        每淹没一次，距离加一
        """
        # 特殊情况
        if matrix == [] or matrix[0] == []:
            return matrix
        
        # 初始化
        row, col = len(matrix), len(matrix[0])
        ret = [[0] * col for _ in range(row)]

        # 找到第一级阶梯
        queue = []
        visited = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    if (j - 1 >= 0 and matrix[i][j - 1] == 0) or \
                       (j + 1 < col and matrix[i][j + 1] == 0) or \
                       (i - 1 >= 0 and matrix[i - 1][j] == 0) or \
                       (i + 1 < row and matrix[i + 1][j] == 0):
                        queue.append((i, j))
                        visited.add((i, j))
        
        # 进行BFS
        k = 0
        while queue:
            k += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                ret[i][j] = k
                if j - 1 >= 0 and matrix[i][j - 1] == 1 and (i, j - 1) not in visited:
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))
                if j + 1 < col and matrix[i][j + 1] == 1 and (i, j + 1) not in visited: # 注意这里不是elif，一开始写成了elif导致一直不通过
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
                if i - 1 >= 0 and matrix[i - 1][j] == 1 and (i - 1, j) not in visited:
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))
                if i + 1 < row and matrix[i + 1][j] == 1 and (i + 1, j) not in visited:
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
        
        # 返回结果
        return ret

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        使用dires进行优化
        """
        # 特殊情况
        if matrix == [] or matrix[0] == []:
            return matrix
        
        # 初始化
        row, col = len(matrix), len(matrix[0])
        ret = [[0] * col for _ in range(row)]
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 找到第一级阶梯
        queue = []
        visited = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1: # 保证当前位置为1
                    for d in dires: # 遍历四个方向
                        x = i + d[0]
                        y = j + d[1]
                        if 0 <= x < row and 0 <= y < col and matrix[x][y] == 0: # 保证周围存在0相邻
                            visited.add((i, j))
                            queue.append((i, j))
                            break
        
        # 进行BFS
        k = 0
        while queue:
            k += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                ret[i][j] = k
                # 遍历四个方向
                for d in dires:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < row and 0 <= y < col and matrix[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
        
        # 返回结果
        return ret
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        进一步优化版
        使用了每个ret[i][j]=-1来表示是否遍历过
        注意到由全局的0，找到第一阶梯的1，本身就是一个BFS的过程
        或者使用暴力循环来找到
        """
        # 特殊情况
        if matrix == [] or matrix[0] == []:
            return matrix
        
        # 初始化
        row, col = len(matrix), len(matrix[0])
        ret = [[-1] * col for _ in range(row)]
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 保存所有0元素的位置
        queue = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                elif matrix[i][j] == 1:
                    for d in dires: # 遍历四个方向
                        x = i + d[0]
                        y = j + d[1]
                        if 0 <= x < row and 0 <= y < col and matrix[x][y] == 0: # 保证周围存在0相邻
                            ret[i][j] = 666 # 这里使用666表示遍历过了
                            queue.append((i, j))
                            break
        
        # 从零开始的异世界BFS
        k = 0
        while queue:
            k += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                ret[i][j] = k
                # 遍历四个方向
                for d in dires:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < row and 0 <= y < col and ret[x][y] == -1 and matrix[x][y] == 1:
                        ret[x][y] = 666 # 这里先临时赋值非-1，避免后续重复添加
                        queue.append((x, y))
        
        # 返回结果
        return ret

    # ===== 个人优化版本 =====
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        反向洪水填充，水漫金山，记录每个位置的水漫高度
        1. 二重循环遍历，找到所有的0位置
        2. 开始BFS对1进行水漫金山，同时更新高度
        其它高效方法：DP
        """
        # 特殊情况
        if matrix == []:
            return []
        
        # 初始化
        step, queue = 0, []
        row, col = len(matrix), len(matrix[0])
        ret = [[0] * col for _ in range(row)]
        flag = [[False] * col for _ in range(row)]
        dires = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    flag[i][j] = True
                    queue.append((i, j))
        
        # BFS
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                for d in dires:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < row and 0 <= y < col and flag[x][y] == False:
                        ret[x][y] = step
                        flag[x][y] = True
                        queue.append((x, y))
        return ret

    # ===== 四个方向遍历 =====
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
		思路：
		1. 对于一维的01数组，找到每个元素最近的0，方法是左右遍历
		2. 对于二维的01数组，找到每个元素最近的0，方法是先左右遍历，再上下遍历
		思考这样方式的准确性，每个位置处的元素，都综合了四个方向上的信息
		首先按行遍历，获取了横向上能到达的最近的0的距离，然后进行纵向上的遍历
		这里的关键点在于：对位置[x,y]进行纵向遍历时，前y列已经完成update，但是后col-y列还没有更新
		并且之后也没有机会来更新前y列了，那么此时能够保证前y列的结果一定准确吗？答案是一定的
		例如正在进行[x4, y5]的列遍历，对于已经遍历的位置[x2, y3]，所有的行信息已经获取并汇总到第y3列
		那么[x2, y3]再在第y3列上汇总，得到的就是全局的最佳信息
        尝试一下四个方向的遍历
        """
        if matrix == []:
            return []
        
        row, col = len(matrix), len(matrix[0])
        dp = [[float("+inf")] * col for _ in range(row)]

        # 行
        for i in range(row):
            # 从左到右（注意这里需要对0的初始化）
            for j in range(col):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                elif matrix[i][j] == 1 and j >= 1:
                    dp[i][j] = 1 + dp[i][j - 1]
            # 从右到左
            for j in range(col - 2, -1, -1):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])
        
        # 列
        for j in range(col):
            # 从上到下
            for i in range(1, row):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
            # 从下到上
            for i in range(row - 2, -1, -1):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
        
        return dp

    # ===== 从对角线方向遍历 =====
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        改进版：划分为左上和右下两部分，两次遍历即可
        """
        if matrix == []:
            return []
        
        row, col = len(matrix), len(matrix[0])
        dp = [[float("+inf")] * col for _ in range(row)]

        # 从左上到右下
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0: # 这里需要对0的初始化
                    dp[i][j] = 0
                    continue
                top = dp[i - 1][j] if i >= 1 else float("+inf")
                lef = dp[i][j - 1] if j >= 1 else float("+inf")
                dp[i][j] = min(dp[i][j], 1 + top, 1 + lef)
        
        # 从右下到左上
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == 1:
                    bot = dp[i + 1][j] if i <= row - 2 else float("+inf")
                    rig = dp[i][j + 1] if j <= col - 2 else float("+inf")
                    dp[i][j] = min(dp[i][j], 1 + bot, 1 + rig)
        
        return dp