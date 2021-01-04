#!/bin/bash python
"""
38. 搜索二维矩阵 II

思路：
其实就是剑指offer中搜索二维数据的变形

1. 暴力搜索，O(nm)，没有利用已知条件
2. 每行二分搜索，O(nlogm)，只是利用每行有序，没有利用列有序
3. 联合行列搜索，考虑四个角，只有从左下或者右上才能进行二分
"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix[0] == []:
            return 0
            
        row = len(matrix)
        col = len(matrix[0])
        cnt, i, j = 0, 0, col - 1
        
        while i < row and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                cnt += 1
                j -= 1
                i += 1
        
        return cnt