#!/bin/bash python
"""
566. 重塑矩阵

思路:
利用一维索引相等这个条件
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        利用reshape前后，两个二维数组的一维index相等这个特性
        """
        row, col = len(nums), len(nums[0])
        if row * col != r * c:
            return nums
        ret = [[0] * c for _ in range(r)]
        for i in range(row):
            for j in range(col):
                index = i * col + j
                ii, jj = index // c, index % c
                ret[ii][jj] = nums[i][j]
        return ret