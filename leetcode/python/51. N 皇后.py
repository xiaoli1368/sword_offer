#!/bin/bash python
"""
51. N皇后

回溯法：（与52同，先写的52）
按行填充，使用额外的数据记录已经放置了棋子的位置
需要额外的函数来判断当前位置新放置棋子是否合理
"""

class Solution(object):
	def __init__(self):
		self.ret = []
	
	def canSet(self, chess, i, j):
		"""
		能否在(i, j)位置上新添一颗棋子
		借助chess数组可以更加方便地遍历
		注意一行代码完成横竖斜三种情况
		"""
		for che in chess:
			x, y = che
			if x == i or y == j or abs(x-i) == abs(y-j):
				return False
		return True
	
	def backTracking(self, board, chess, n, i):
		"""
		回溯法
		board：当前棋盘
		chess：已经放置了棋子的位置
		n：棋盘维度
		i：将要放置的行索引
		"""
		if i >= n:
			tmp = ["".join(line) for line in board]
			self.ret.append(tmp)
			return
		for j in range(n):
			if self.canSet(chess, i, j):
				board[i][j] = "Q"
				chess.append((i, j))
				self.backTracking(board, chess, n, i + 1)
				board[i][j] = "."
				chess.pop()

	def SolveNQueens(self, n):
		"""
		board为二维数组，记录棋盘信息
		chess为一维数组，记录已经放置棋子的位置
		"""
		if n <= 0:
			return []
		self.cnt = 0 # 防止不同的测试影响
		chess = []
		board = [["."] * n for _ in range(n)]
		self.backTracking(board, chess, n, 0)
		return self.ret

if __name__ == "__main__":
	s = Solution()
	print(s.solveNQueens(4))
	#print(s.solveNQueens(8))