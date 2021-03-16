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

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        原地hash
        注意寻找的是没有出现过的元素
        映射为：(1, n) -> (0, n-1)
        值为i的元素，映射到i-1索引处，前提是目标位置没有达成匹配
        4 3 2 7 8 2 3 1
        7 3 2 4 8 2 3 1
        3 3 2 4 8 2 7 1
        2 3 3 4 8 2 7 1
        3 2 3 4 8 2 7 1 -> 3
        3 2 3 4 1 2 7 8
        1 2 3 4 3 2 7 8 -> 3, 2
        """
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [i + 1 for i in range(len(nums)) if i + 1 != nums[i]]

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        原地哈希
        把已经出现过的位置标记为负数，最终保持正数的位置就是没有出现过的元素
        4 3 2 7 8 2 3 1
        -4 -3 -2 -7 8 2 -3 -1
        """
        ret = []
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] = -nums[pos]
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)
        return ret