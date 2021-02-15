#!/bin/bash python
"""
37. 解数独

思路：
经典回溯法，注意对于九宫格子的遍历方式
"""

class Solution(object):
    def isValid(self, board, i, j, value):
        """
        判断在board[i][j]的位置上，填入value是否合法
        """
        for k in range(9):
            if value == board[i][k]:
                return False
            if value == board[k][j]:
                return False
            if value == board[i//3*3 + k//3][j//3*3 + k%3]:
                return False
        return True
    
    def backTracking(self, board, points, index):
        """
        遍历当前待填入位置的集合points
        index表示当前正在填入第index个位置
        """
        if index >= len(points):
            return True
        for num in range(1, 10):
            i, j = points[index]
            value = str(num)
            if self.isValid(board, i, j, value):
                board[i][j] = value
                if self.backTracking(board, points, index + 1):
                    return True
                else:
                    board[i][j] = "."
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        points = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    points.append((i, j))
        self.backTracking(board, points, 0)

    # ===== 其它优化版方法 =====
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, pos, rows, cols, grids, index):
            """
            回溯法，返回是否成功
            """
            if index >= len(pos):
                return True
            # 遍历1-9，选取合适的值填充当前index位置
            i, j = pos[index]
            ind = i // 3 * 3 + j // 3
            for val in range(1, 10):
                if rows[i][val] == cols[j][val] == grids[ind][val] == False:
                    board[i][j] = str(val)
                    rows[i][val] = cols[j][val] = grids[ind][val] = True
                    if dfs(board, pos, rows, cols, grids, index + 1):
                        return True
                    rows[i][val] = cols[j][val] = grids[ind][val] = False
                    board[i][j] = "."
            return False
        # =========================
        if board == []:
            return
        # 使用数组hash，表示每行列九宫格出现数字的情况，第i行的数字j是否出现过
        pos = []
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        grids = [[False] * 10 for _ in range(9)]
        # 遍历初始化数组hash，并保存要遍历的位置
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    pos.append((i, j))
                else:
                    val = int(board[i][j])
                    ind = i // 3 * 3 + j // 3
                    rows[i][val] = cols[j][val] = grids[ind][val] = True
        # 正式遍历
        dfs(board, pos, rows, cols, grids, 0)
        return