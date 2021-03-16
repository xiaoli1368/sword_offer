#!/bin/bash python
"""
74. 搜索二维矩阵

思路:
见注释
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        1. 暴力方法，二重循环查找，O(m * n)
        2. 优化方法，先查找一行，再查找一列，O(m + n)
        3. 优化方法，二分查找一行和一列，O(logm * logn)
		4. 更加优化，二分查找一行和一列，O(logm * logn)，直接进行二分，O(log(m+n))
		   m * n > m + n, log(m * n) > log(m + n), log(m) + log(n) > log(m + n)
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        分别查找一行一列
        """
        m, n = len(matrix), len(matrix[0])

        i = -1
        while i < m - 1:
            if target >= matrix[i + 1][0]:
                i += 1
            else:
                break
        if i == -1:
            return False
        
        for num in matrix[i]:
            if num == target:
                return True
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        二分查找一行和一列，O(logm * logn)
        """
        row, col = len(matrix), len(matrix[0])

        # 查找行索引row
        l, h = 0, row - 1
        while l < h:
            m = (l + h + 1) // 2
            if matrix[m][0] > target:
                h = m - 1
            else:
                l = m

        # 特殊情况
        if matrix[l][0] > target:
            return False 
        
        # 查找列索引
        index = l
        l, h = 0, col - 1
        while l <= h:
            m = (l + h) // 2
            if matrix[index][m] == target:
                return True
            elif matrix[index][m] > target:
                h = m - 1
            else:
                l = m + 1
        return False

    # ===== 封装函数后的优化版 =====
    def binarySearch(self, matrix, target, index, axis=0):
        """
        选定matrix的axis轴上第index个向量，得到一维vec
        axis=0/1，分别表示纵轴，横轴
        在vec中寻找小于等于target的最大索引，注意有可能返回-1
        """
        # 越界的特殊情况
        if index < 0:
            return index
        # 二分查找
        l, h = 0, (len(matrix) if axis == 0 else len(matrix[0])) - 1
        while l <= h:
            m = (l + h + 1) // 2
            val = matrix[m][index] if axis == 0 else matrix[index][m]
            if val > target:
                h = m - 1
            else:
                l = m
                if l == h:
                    break
        return h

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        优化方法，二分查找一行和一列，O(logm * logn)
        """
        row = self.binarySearch(matrix, target, index=0, axis=0)
        col = self.binarySearch(matrix, target, index=row, axis=1)
        return row >= 0 and col >= 0 and matrix[row][col] == target

    # ===== 最优的方法 =====
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        直接进行二分查找
        区别是需要从二维数组中取值
        index在[row, col]维度上的索引为：[i // col, i % col]
        """
        row, col = len(matrix), len(matrix[0])
        l, h = 0, row * col - 1
        while l <= h:
            m = (l + h) // 2
            val = matrix[m//col][m%col]
            if val == target:
                return True
            elif val > target:
                h = m - 1
            else:
                l = m + 1
        return False 