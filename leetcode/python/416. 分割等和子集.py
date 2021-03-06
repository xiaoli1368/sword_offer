#!/bin/bash python
"""
416. 分割等和子集

思路：
1. 判断是否存在解：求和然后判断是否为偶数
2. 暴力方法：DFS，每个当前元素只有两种可能，是否选取当前元素，然后求当前的和
			优化方法为排序，这样就可以在大于target的时候进行剪枝
3. 背包问题：dp[i][j]表示在前i个元素并且给定背包大小为j的情况下，最大收益
			背包容量为sum//2，对每个元素nums[k]，重量为nums[k]，价格也是nums[k]
			每个元素只能挑选0/1次，因此是01背包问题，重量为nums[k]，保证了子集的和必然
			不大于sum//2，价格是nums[k]保证了在此基础上使得求和最大
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
			优化：空间压缩，dp[i][j]表示前i个元素中是否可以找到和为j的子集，dp[j] = dp[j] or dp[j - nums[i]]
4. follow up 1: 如果要求这两个子集各自的和，尽可能接近呢？
5. follow up 2: 如果要求这两个子集各自的和，尽可能接近，然后返回这两个子集
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        暴力DFS方法
        """
        def dfs(nums, target, curr, i):
            """
            从nums挑选出子集path
            判断子集的和curr是否等于target
            当前正在遍历nums[i]
            只有三种情况True: 未选取则已经相等，跳过当前后相等，选取当前后相等
            """
            if curr > target or i >= len(nums):
                return False
            if curr == target or dfs(nums, target, curr, i + 1) or dfs(nums, target, curr + nums[i], i + 1):
                return True
            else:
                return False
        # =============================
        ssum = sum(nums)
        if nums == [] or ssum % 2 == 1:
            return False
        nums.sort()
        return dfs(nums, ssum // 2, 0, 0)
	
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
		传统背包方法，带空间优化
        """
        ssum = sum(nums)
        if nums == [] or ssum % 2 == 1:
            return False
        row, col = len(nums), ssum // 2
        dp = [0] * (col + 1)
        for i in range(1, row + 1):
            w = v = nums[i - 1]
            for j in range(col, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
        return dp[-1] == ssum // 2

    def canPartition(self, nums: List[int]) -> bool:
        """
        优化版的01背包
        """
        ssum = sum(nums)
        if nums == [] or ssum % 2 == 1:
            return False
        row, col = len(nums), ssum // 2
        dp = [True] + [False] * col
        for i in range(row):
            for j in range(col, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]