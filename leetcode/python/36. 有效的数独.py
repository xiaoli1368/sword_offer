#!/bin/bash python
"""
36. 有效的数独

思路：
常规遍历来确定是否重复
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 使用set判断是否重复
        s = set()
        # 遍历9次即可
        for i in range(9):
            # 第i行
            s.clear()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
            # 第i列
            s.clear()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
            # 第i个九宫格
            s.clear()
            for j in range(9):
                x = i // 3 * 3 + j // 3
                y = i % 3 * 3 + j % 3
                if board[x][y] == ".":
                    continue
                if board[x][y] in s:
                    return False
                s.add(board[x][y])
        return True

	# 其它方法
	def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def checkExist(val, s):
            """
            判断元素val是否存在于字典s中
            """
            if val != "." and val in s:
                return True
            s.add(val)
            return False
        # ========================
        # 特殊情况
        if len(board) != 9:
            return False
        # 判断行列九宫格内是否重复
        for i in range(9):
            rows, cols, grids = set(), set(), set()
            for j in range(9):
                if checkExist(board[i][j], rows) or checkExist(board[j][i], cols) or checkExist(board[i//3*3 + j//3][i%3*3 + j%3], grids):
                    return False
        return True