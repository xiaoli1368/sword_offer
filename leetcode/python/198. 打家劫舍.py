#!/bin/bash python
"""
198. 打家劫舍

思路：
动态规划，思考递推方程，尝试状态压缩
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        思考状态递推方程：
        dp[i]表示小偷从0走到i，所能偷到的最多金钱
        当前房屋不偷：dp[i] = dp[i - 1]
        当前房屋偷盗：dp[i] = nums[i] + dp[i - 2]
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        """
        if nums == []:
            return 0
        n = len(nums)
        dp = [0] * (n + 1) # 使用n+1长度，相当于之前左侧补0
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        """
        思考状态递推方程：
        dp[i]表示小偷从0走到i，所能偷到的最多金钱
        当前房屋不偷：dp[i] = dp[i - 1]
        当前房屋偷盗：dp[i] = nums[i] + dp[i - 2]
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
		这种方式没有补0，更好理解
        """
        if nums == []:
            return 0
        dp = nums[:]
        for i in range(1, len(nums)):
            currMax = nums[i] + (0 if i < 2 else dp[i - 2])
            dp[i] = max(dp[i - 1], currMax)
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        思考状态压缩：dp中只是三个变量迭代
        """
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(b, a + nums[i])
        return b

	def rob(self, nums: List[int]) -> int:
        """
		来自网友的究极优化版本，建议全文背诵
        """
        prev = curr = 0
        for val in nums:
            prev, curr = curr, max(curr, prev + val)
        return curr