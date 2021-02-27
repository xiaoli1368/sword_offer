#!/bin/bash python
"""
300. 最长递增子序列

思路：
动态规划，以及使用二分进行优化

基础dp：O(n^2) + O(n)
dp[i]表示以dp结尾的最长递增子序列长度
dp[i] = max(dp[i], 1 + dp[j]), j=0:i-1, dp[j] < dp[i]
ret = max(ret, dp[i]), i=0:n

错误思路，单调栈思路：O(n^2) + O(n)
数组dp为单调递增栈，表示包括当前nums[i]元素可以达到的最长递增子序列
如果dp递增，则正常添加元素，否则出栈以维持dp单调性
ret = max(ret, len(dp))
这种方式解决不了：[1,3,6,7,9,4,10,5,6]
原因是处理4之前是：[1,3,6,7,9]，添加4之后是：[1,3,4]，后续无法达到最大长度6
错误的原因是：添加4之后，扼杀了之前子序列增长的可能性

贪心+二分思路
要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。因此如上述例子，在处理4的时候，不进行出栈操作，反而是在之前数组的基础上查找，找到[a < 4 < b]的位置，然后使用4代替b，这样后续有机会从4开始增长，同时也没有额外原来的从9开始增长的可能性，并且在有序数组中查找右边界，可以使用二分加速。
（这种方式可以找到：最长长度的上升子序列，且保证该子序列的和最小）
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        # 基础dp
        ret, dp = 1, [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ret = max(ret, dp[i])
        return ret

    # ===== 贪心 + 二分 =====
    def binarySearch(self, vec, target):
        """
        在vec中找到target的右侧最近的更大值
        已经明确 vec[-1] >= target
        """
        l, h = 0, len(vec) - 1
        while l < h:
            m = l + (h - l) // 2
            if vec[m] < target:
                l = m + 1
            else:
                h = m
        return l

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        # 事实上已经和dp关系不大了
        # dp维持一个单调递增的数组
        dp = []
        for i in range(len(nums)):
            if dp == [] or dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                index = self.binarySearch(dp, nums[i])
                dp[index] = nums[i]
        return len(dp)