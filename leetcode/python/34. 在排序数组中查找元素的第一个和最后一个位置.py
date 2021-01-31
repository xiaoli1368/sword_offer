#!/bin/bash python
"""
34. 在排序数组中查找元素的第一个和最后一个位置

思路：
有序数组里的查找，所以是经典的二分方法
1. 暴力枚举，记录出现target的最小索引和最大索引，O(n)
2. 二分查找左边界，然后暴力枚举右边界，O(logn + n)
3. 二分查找左边界，然后在此基础上二分查找右边界，O(2logn)
4. 复用函数二分查找左边界，然后查找target和target+1，代码量减少
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

	# ===== 更加简便的方法 =====
    def binarySearch(self, nums, target, l, h):
        """
        寻找数组中大于等于target的最小索引
        注意返回结果有可能大于数组有效索引
        """
        while l < h:
            m = (l + h) // 2
            if nums[m] < target:
                l = m + 1
            else:
                h = m
        return l if l >= len(nums) or nums[l] >= target else l + 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分法
        """
        n = len(nums)
        left = self.binarySearch(nums, target, 0, n - 1)
        right = self.binarySearch(nums, target + 1, left, n - 1)
        return [left, right - 1] if left < len(nums) and nums[left] == target else [-1, -1]