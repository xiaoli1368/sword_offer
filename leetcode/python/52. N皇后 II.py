#!/bin/bash python
"""
52. N皇后 II

回溯法：
按行填充，使用额外的数据记录已经放置了棋子的位置
需要额外的函数来判断当前位置新放置棋子是否合理
"""

class Solution(object):
	def __init__(self):
		self.cnt = 0
	
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
	
	def isValid(self, board, n, i, j):
		"""
		其它版本的canSet函数，之前写的，可以用来回顾对比
		通过4个方向和k距离，进行四面八方的遍历
		"""
		directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
		for k in range(n):
			if board[i][k] == "Q": # 横线
				return False
			if board[k][j] == "Q": # 竖线
				return False
			for dire in directions: # 四个斜线方向
				x, y = i + k*dire[0], j + k*dire[1]
				if 0 <= x < n and 0 <= y < n and board[x][y] == "Q":
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
			self.cnt += 1
			return
		for j in range(n):
			if self.canSet(chess, i, j):
				board[i][j] = "Q"
				chess.append((i, j))
				self.backTracking(board, chess, n, i + 1)
				board[i][j] = "."
				chess.pop()

	def totalNQueens(self, n):
		"""
		board为二维数组，记录棋盘信息
		chess为一维数组，记录已经放置棋子的位置
		"""
		if n <= 0:
			return 0
		self.cnt = 0 # 防止不同的测试影响
		chess = []
		board = [["."] * n for _ in range(n)]
		self.backTracking(board, chess, n, 0)
		return self.cnt

if __name__ == "__main__":
	s = Solution()
	print(s.totalNQueens(4))
	print(s.totalNQueens(8))