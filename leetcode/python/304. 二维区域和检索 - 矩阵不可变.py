#!/bin/bash python
"""
304. 二维区域和检索 - 矩阵不可变

思路：
二维前缀和
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        二维前缀和
        dp[i][j]表示maxtrix[i][j]左上角区域的和
        不包括当前行列，因此[i,j]最大取值为[row,col]
        """
        if matrix == [] or matrix[0] == []:
            return
        row, col = len(matrix), len(matrix[0])
        self.dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]
        return


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)