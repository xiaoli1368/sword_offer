#!/bin/bash python
"""
287. 寻找重复数

思路:
原地hash
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        原地hash
        """
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] != i + 1:
                return nums[i]
        return 0