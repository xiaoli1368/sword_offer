#!/bin/bash python
"""
287. 寻找重复数

思路:
原地hash
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. 直接使用hash
        2. 直接原地hash
        """
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        """
        原地hash
        将数字val放到val-1的位置上
        """
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] - 1 != i:
                return nums[i]
        return -1