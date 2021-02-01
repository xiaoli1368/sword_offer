#!/bin//bash python
"""
33. 搜索旋转排序数组

思路：
旋转二分，最关键的就是先通过与末尾元素的比较，划分前后区间
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        本题是严格升序，所以要好做一些
        旋转后数组分为了两个递增区间，而区分这两个递增区间的条件是
        nums[m] <= nums[h] || nums[m] >= nums[l]
        """
        if nums == []:
            return -1
        
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target: # 找到了直接返回
                return m
            elif nums[m] <= nums[h]: # 没找到，位于右侧区间
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
            elif nums[m] > nums[h]: # 没找到，位于左侧区间
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
        return -1