#!/bin/bash python
"""
41. 缺失的第一个正数

思路：
原地hash，注意循环条件
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        把正数n放到索引为n-1的位置，原地哈希
        """
        if nums == []:
            return 1
        
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] and nums[i] != i + 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                curr = nums[i]
                nums[i], nums[curr - 1] = nums[curr - 1], nums[i]
        
        # 检索缺失的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
	
	# ===== 优化版 =====
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        原地hash
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] < n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1