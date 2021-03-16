#!/bin/bash python
"""
59. 螺旋矩阵 II

思路:
分解为4条直线
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        分解为4条直线填充
		注意初始化值为n*n, 是为了保证中心元素满足要求
        """
        ret = [[n*n] * n for _ in range(n)]
        cnt, top, left, bottom, right = 0, 0, 0, n - 1, n - 1
        while top < bottom and left < right:
            for i in range(left, right):
                cnt += 1
                ret[top][i] = cnt
            for i in range(top, bottom):
                cnt += 1
                ret[i][right] = cnt
            for i in range(right, left, -1):
                cnt += 1
                ret[bottom][i] = cnt
            for i in range(bottom, top, -1):
                cnt += 1
                ret[i][left] = cnt
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return ret