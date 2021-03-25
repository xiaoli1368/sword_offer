#!/bin/bash python
"""
73. 矩阵置零

思路：
二重循环

这道题值得思考的地方在于，时间复杂度
首先必须先使用O(n^2)来记录rows和cols
然后有两种思路来进行修改
1. 直接对二维数组进行O(n^2)的遍历，对应其中行列位于[rows, cols]的元素进行置0
2. 分别进行两次遍历，一次选定rows遍历所有的列，二次选定cols遍历所有的行

可以发现二者的性能优劣：
1. 第一种方式，不会存在同一处位置被多次置0的情况，但[rows, cols]较小时，存在大量冗余
2. 第二种方式，存在本身的冗余，同一处位置可能会被多次置0，但是不会遍历其它不可能被置0的位置

综上所述：
如果 [rows, cols] 非常接近原始的 [m, n]，也就是存在大量的0值，则使用方法1
否则，使用方法2
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return
        
        row, col = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        return

    # ===== 其它思考 =====
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in cols:
                matrix[i][j] = 0
        return