#!/bin/bash python
"""
34. 在排序数组中查找元素的第一个和最后一个位置

思路：
二分查找左边界
然后查找右边界（可以二分，也可以普通查找）
注意各种特殊情况
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        二分查找左右边界
        """
        if nums == []:
            return [-1, -1]
            
        # 寻找大于等于target的第一个索引
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            if nums[m] >= target:
                h = m
            else:
                l = m + 1
        left = h
        
        # 如果不存在
        if nums[left] != target:
            return [-1, -1]
        
        # 查找右边界
        l, h = left, len(nums) - 1
        while l < h:
            m = l + (h - l + 1) // 2
            if nums[m] <= target:
                l = m
            else:
                h = m - 1
        right = l
        
        return [left, right]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分法
        """
        # 特殊情况
        if nums == []:
            return [-1, -1]
        # 进行二分，查找左边界
        l, h = 0, len(nums) - 1
        while l <= h:
            m = l + (h - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] >= target:
                h = m - 1
        # 验证是否满足
        left = right = h + 1
        if left < 0 or left >= len(nums) or nums[left] != target:
            return [-1, -1]
        # 查找右边界
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        # 返回结果
        return [left, right]