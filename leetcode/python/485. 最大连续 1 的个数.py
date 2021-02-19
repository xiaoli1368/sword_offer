#!bin/bash python
"""
485. 最大连续 1 的个数

思路：
滑窗法，线性扫描
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        直接线性扫描，区间为：(l, h]
        """
        ret, l = 0, -1
        for h in range(len(nums)):
            if nums[h] == 1:
                ret = max(ret, h - l)
            else:
                l = h
        return ret