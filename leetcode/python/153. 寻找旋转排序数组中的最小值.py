#!/bin/bash python
"""
153. 寻找旋转排序数组中的最小值

思路：
旋转二分
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] <= nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]