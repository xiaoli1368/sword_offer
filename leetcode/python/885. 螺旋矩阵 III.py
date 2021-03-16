#!/bin/bash python
"""
885. 螺旋矩阵 III

思路:
还是分解4条直线
"""

class Solution(object):
    def value(self, row, col, i, j):
        """
        判断[i, j]是否在[row, col]内
        """
        return i >= 0 and j >= 0 and i < row and j < col

    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        if r0 < 0 or c0 < 0 or r0 >= R or c0 > C:
            return []
        
        ret = []
        top = bottom = r0
        left = right = c0
        
        while len(ret) < R * C:
            # 上横
            right += 1
            for i in range(left, right):
                if self.value(R, C, top, i):
                    ret.append([top, i])
            # 右竖
            bottom += 1
            for i in range(top, bottom):
                if self.value(R, C, i, right):
                    ret.append([i, right])
            # 下横
            left -= 1
            for i in range(right, left, -1):
                if self.value(R, C, bottom, i):
                    ret.append([bottom, i])
            # 左竖
            top -= 1
            for i in range(bottom, top, -1):
                if self.value(R, C, i, left):
                    ret.append([i, left])

        # 返回结果
        return ret

    # ===== 优化版 =====
    def tryToAdd(self, ret, R, C, x, y):
        """
        如果索引合法则添加
        """
        if 0 <= x < R and 0 <= y < C:
            ret.append([x, y])

    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        什么时候停止？当输出ret的size达到R*C的时候停止，分解为4条直线
        """
        ret = []
        top = bottom = r0
        left = right = c0
        while len(ret) < R * C:
            right += 1
            for i in range(left, right):
                self.tryToAdd(ret, R, C, top, i)
            bottom += 1
            for i in range(top, bottom):
                self.tryToAdd(ret, R, C, i, right)
            left -= 1
            for i in range(right, left, -1):
                self.tryToAdd(ret, R, C, bottom, i)
            top -= 1
            for i in range(bottom, top, -1):
                self.tryToAdd(ret, R, C, i, left)
        return ret