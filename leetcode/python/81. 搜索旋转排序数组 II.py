#!/bin/bash python
"""
81. 搜索旋转排序数组 II

思路：
旋转二分，关键在于有重叠元素
需要思考清楚，先排除了三点相等的情况，剩余的m==h情况发生会是哪些场景？
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        区别在于包含了重复元素
        """
        if nums == []:
            return False
        
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target: # 直接找到
                return True
            elif nums[m] == nums[l] == nums[h]: # 只能顺序遍历
                return target in nums[l:h+1]
            elif nums[m] <= nums[h]: # 注意此时nm=nh，只有m在右半段一种情况，否则三者相等
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
            elif nums[m] > nums[h]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
        return False