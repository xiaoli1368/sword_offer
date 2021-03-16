#!/bin/bash python
"""
48. 旋转图像

思路:
两层遍历, 进行赋值
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        注意内部不能是 for i in range(left, right)，因此需要的是相对距离
        """
        n = len(matrix)
        top, left, bottom, right = 0, 0, n - 1, n - 1
        while top < bottom and left < right:
            for i in range(right - left):
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return