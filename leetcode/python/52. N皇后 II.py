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
	
	# ===== 更加高效的方法 =====
    def totalNQueens(self, n: int) -> int:
        """
        更加高效的方式，使用辅助三个数组
        对行进行遍历，三个数组记录列、左对角线和右对角线上是否有皇后
		注意到不需要使用Board这个棋盘数组
        """
        def dfs(cols, ldiags, rdiags, ret, n, i):
            """
            i表示正在遍历第i行
            [i,j]位置的左右对角线索引为：[n - 1 - i + j, i + j]
            """
            if i >= n:
                ret[0] += 1
                return
            for j in range(n):
                l, r = n - 1 - i + j, i + j
                if not cols[j] and not ldiags[l] and not rdiags[r]:
                    cols[j] = ldiags[l] = rdiags[r] = True
                    dfs(cols, ldiags, rdiags, ret, n, i + 1)
                    cols[j] = ldiags[l] = rdiags[r] = False
            return
        # ===== 调用 =====
        if n <= 0:
            return 0
        ret = [0]
        cols = [False] * n
        ldiags = [False] * (2 * n - 1)
        rdiags = [False] * (2 * n - 1)
        dfs(cols, ldiags, rdiags, ret, n, 0)
        return ret[0]

if __name__ == "__main__":
	s = Solution()
	print(s.totalNQueens(4))
	print(s.totalNQueens(8))