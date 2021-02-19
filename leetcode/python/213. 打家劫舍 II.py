#!/bin/bash python
"""
213. 打家劫舍 II

思路：
思考循环条件影响了什么？
影响了首尾的判断，首尾只能取一个
当在遍历尾部的时候，无法从dp[i-1]中得出是否包括首部的信息
因为整体是环，所以需要人为的选定头尾
只有两种情况，选中索引0，或者不选择索引0，其它情况下以其它索引为头部等价
因此分别考虑两种情况，然后求最大值即可
"""

class Solution(object):
    def getMax(self, nums, begin, end):
        """
        对nums，从[begin, end]最多获取金钱
        不考虑圆圈限制
        """
        if begin == end:
            return nums[begin]
        dp = nums[begin:end+1]
        for i in range(1, end - begin + 1):
            currMax = nums[begin + i] + (0 if i < 2 else dp[i - 2])
            dp[i] = max(dp[i - 1], currMax)
        return dp[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思考循环条件影响了什么？
        影响了首尾的判断，首尾只能取一个
        当在遍历尾部的时候，无法从dp[i-1]中得出是否包括首部的信息
        因为整体是环，所以需要人为的选定头尾
        只有两种情况，选中索引0，或者不选择索引0，其它情况下以其它索引为头部等价
        因此分别考虑两种情况，然后求最大值即可
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        return max(self.getMax(nums, 0, n - 2), self.getMax(nums, 1, n - 1))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        究极优化版本
        """
        def robLine(nums, begin, end):
            prev = curr = 0
            for i in range(begin, end + 1):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr
        # ============================
        n = len(nums)
        return nums[0] if n == 1 else max(robLine(nums, 0, n - 2), robLine(nums, 1, n - 1))