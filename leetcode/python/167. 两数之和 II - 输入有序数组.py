#!/bin/bash python
"""
167. 两数之和 II - 输入有序数组

思路：
经典双指针

思考双指针解法的正确性（其实就是在暴力遍历O(n^2)的基础上进行了剪枝）
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        双指针
        """
        if numbers == []:
            return [0, 0]
        
        n = len(numbers)
        l, h = 0, n - 1
        while l < h:
            ssum = numbers[l] + numbers[h]
            if ssum == target:
                return [l + 1, h + 1]
            elif ssum < target:
                l += 1
            elif ssum > target:
                h -= 1
        return [0, 0]

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
		简洁版本
        """
        l, h = 0, len(numbers) - 1
        while l <= h:
            ssum = numbers[l] + numbers[h]
            if ssum == target:
                break
            elif ssum > target:
                h -= 1
            elif ssum < target:
                l += 1
        return [l + 1, h + 1]