#!/bin/bash python
"""
560. 和为K的子数组

思路：
前缀和逐渐优化
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        暴力方法，O(n^3) + O(1)
        三重循环（中间sum也算一层循环）
        """
        cnt, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) == k:
                    cnt += 1
        return cnt

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        暴力方法优化，O(n^2) + O(1)
        在第二层循环中，遍历的时候直接累计和
        """
        cnt, n = 0, len(nums)
        for i in range(n):
            ssum = 0
            for j in range(i, n):
                ssum += nums[j]
                if ssum == k:
                    cnt += 1
        return cnt

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        前缀和方法，O(n^2) + O(n)
        """
        cnt, n = 0, len(nums)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + nums[i]
        for i in range(n):
            for j in range(i, n):
                if dp[j + 1] - dp[i] == k:
                    cnt += 1
        return cnt


