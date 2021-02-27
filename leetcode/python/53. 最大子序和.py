#!/bin/bash python
"""
53. 最大子序和

思路：
动态规划
dp[i]表示以dp为结尾的最大子序列和
dp[i] = max(nums[i], nums[i] + dp[i - 1])
dp[i] = nums[i] + max(0, dp[i - 1])
可以使用空间压缩
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        """
        if nums == []:
            return 0
        curr_sum, max_sum = 0, float("-inf")
        for i in range(len(nums)):
            curr_sum = nums[i] + max(0, curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum