#!/bin/bash python
"""
51. N皇后

回溯法：（与52同，先写的52）
按行填充，使用额外的数据记录已经放置了棋子的位置
需要额外的函数来判断当前位置新放置棋子是否合理

最顶级的优化方式，就是使用位运算来标记列左右对角线的标记
因此这样可以把空间复杂度降为O(1)，三个二进制整数
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
	
	# ===== 更加高效的方法 =====
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        更加高效的方式，使用辅助三个数组
        对行进行遍历，三个数组记录列、左对角线和右对角线上是否有皇后
        """
        def dfs(board, cols, ldiags, rdiags, ret, n, i):
            """
            i表示正在遍历第i行
            [i,j]位置的左右对角线索引为：[n - 1 - i + j, i + j]
            """
            if i >= n:
                tmp = ["".join(line) for line in board]
                ret.append(tmp)
                return
            for j in range(n):
                l, r = n - 1 - i + j, i + j
                if not cols[j] and not ldiags[l] and not rdiags[r]:
                    board[i][j] = "Q"
                    cols[j] = ldiags[l] = rdiags[r] = True
                    dfs(board, cols, ldiags, rdiags, ret, n, i + 1)
                    cols[j] = ldiags[l] = rdiags[r] = False
                    board[i][j] = "."
            return
        # ===== 调用 =====
        if n <= 0:
            return 0
        ret = []
        cols = [False] * n
        ldiags = [False] * (2 * n - 1)
        rdiags = [False] * (2 * n - 1)
        board = [["."] * n for _ in range(n)]
        dfs(board, cols, ldiags, rdiags, ret, n, 0)
        return ret
	
if __name__ == "__main__":
	s = Solution()
	print(s.solveNQueens(4))
	#print(s.solveNQueens(8))