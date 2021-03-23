#!/bin/bash python
"""
724. 寻找数组的中心下标

思路：
前缀和
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        前缀和
        """
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + nums[i]
        for i in range(n):
            if dp[i] == dp[n] - dp[i + 1]:
                return i
        return -1