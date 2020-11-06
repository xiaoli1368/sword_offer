#!/bin/bash python
"""
448. 找到所有数组中消失的数字

思路：
原地哈希
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        原地哈希
        """
        if nums == []:
            return []
        
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                curr = nums[i]
                nums[i], nums[curr - 1] = nums[curr - 1], nums[i]
        #print(nums)

        ret = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ret.append(i + 1)
        return ret