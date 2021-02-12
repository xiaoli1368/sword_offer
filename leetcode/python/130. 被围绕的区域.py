#!/bin/bash python
"""
130. 被围绕的区域

思路：
DFS，但是有两种思路
这里的难点是判断每个节点是否与边界相连
"""

class Solution(object):
    def bfs(self, board, flag, point, row, col, i, j):
        """
        广度优先遍历，找到与(i, j)相连的最大连通域，坐标添加到point
        返回结果表示该连通域是否为封闭的
        如果是封闭的则外部将所有的point置O
        如果不是封闭的则将所有的point的flag标记为已经遍历
        """
        if flag[i][j] == True or board[i][j] == "X": # 已经遍历过了
            return True
        if (i == 0 or i == row - 1 or j == 0 or j == col - 1) and board[i][j] == "O":
            return False
        
        # 遍历当前位置
        flag[i][j] = True
        point.append((i, j))

        # 如果四个方向都闭合
        a = self.bfs(board, flag, point, row, col, i + 1, j)
        b = self.bfs(board, flag, point, row, col, i - 1, j)
        c = self.bfs(board, flag, point, row, col, i, j + 1)
        d = self.bfs(board, flag, point, row, col, i, j - 1)
        if a and b and c and d:
           return True
        else:
            return False


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) <= 1:
            return
        
        row = len(board)
        col = len(board[0])
        flag = [[False] * col for _ in range(row)]

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                point = []
                if self.bfs(board, flag, point, row, col, i, j):
                    for p in point:
                        board[p[0]][p[1]] = "X"
        return
	
	# ===== 另一种方式 =====
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        遍历找到区域内的O，然后开始DFS洪水填充
        注意这里的关键是：与边界上的O相连的O也是不能填充的
        """
        def dfs(board, flag, dires, row, col, i, j):
            """
            DFS
            返回当前区域与边界相连
            """
            # 越界，已经访问过，或者不是O，退出
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != "O" or flag[i][j] == True:
                return
            # 标记为已经访问
            flag[i][j] = True
            # 遍历四个方向
            for d in dires:
                x, y = i + d[0], j + d[1]
                dfs(board, flag, dires, row, col, x, y)
            return
        # ===== 调用 =====
        if board == []:
            return
        row = len(board)
        col = len(board[0])
        flag = [[False] * col for _ in range(row)]
        dires = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 从边界上的O开始DFS，把所有与之相连的标记为True
        for i in range(col):
            dfs(board, flag, dires, row, col, 0, i)
            dfs(board, flag, dires, row, col, row - 1, i)
        for i in range(row):
            dfs(board, flag, dires, row, col, i, 0)
            dfs(board, flag, dires, row, col, i, col - 1)
        # 遍历整个二维数组，把合法的O进行翻转
        for i in range(row):
            for j in range(col):
                if flag[i][j] == False:
                    board[i][j] = "X"
        return