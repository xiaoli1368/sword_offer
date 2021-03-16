#!/bin/bash python
"""
54. 螺旋矩阵

思路:
分解为四条单独打印的直线
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        ret = []
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while top < bottom and left < right:
            # 上横
            for i in range(left, right):
                ret.append(matrix[top][i])
            # 右竖
            for i in range(top, bottom):
                ret.append(matrix[i][right])
            # 下横
            for i in range(right, left, -1):
                ret.append(matrix[bottom][i])
            # 左竖
            for i in range(bottom, top, -1):
                ret.append(matrix[i][left])
            # 更新
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        
        # 特殊情况
        if top == bottom and left == right: # 只有一个值
            ret.append(matrix[top][left])
        elif top == bottom: # 只有一行
            ret += [matrix[top][i] for i in range(left, right + 1)]
        elif left == right: # 只有一列
            ret += [matrix[i][left] for i in range(top, bottom + 1)]

        # 返回结果
        return ret

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        分解为4条直线
        考虑特殊情况，每条直线都完成本直线的全部打印
        """
        ret, row, col = [], len(matrix), len(matrix[0])
        top, left, bottom, right = 0, 0, row - 1, col - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ret.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                ret.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    ret.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    ret.append(matrix[i][left])
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return ret