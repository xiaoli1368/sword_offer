#!/bin/bash python
"""
154. 寻找旋转排序数组中的最小值 II

思路：
增加了重复元素
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        区别在于存在重复数组
        """
        if nums == []:
            return 0
        
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[l] == nums[m] == nums[h]: # 此时无法进行区分
                return min(nums[l:h+1])
            elif nums[m] <= nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]