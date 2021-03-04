#!/bin/bash python
"""
303. 区域和检索 - 数组不可变

思路：
一维前缀和
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        一维dp，前缀和
        """
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]
            
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.dp == [] or i > j or i < 0:
            return 0
        elif i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)