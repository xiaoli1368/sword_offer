#!/bin/bash python
"""
312. 戳气球

思路：
递归或者动态规划
"""

class Solution(object):
	# ===== 原始递归方法 =====
    def maxScore(self, nums, l, h, left, right):
        """
        把nums[l:h]闭区间内所有气球戳破得到的最大分数
        left, right表示左右边界外部相邻元素
        1. 如果n==0，返回0
        2. 否则选定一个位置最后戳破，则分数由三部分构成
           左侧max得分，右侧max得分，当前最后一个位置得分（由 left * curr * right 得到）
        """
        ret = 0
        if l <= h:
            for i in range(l, h + 1):
                curr = nums[i]
                leftScore = self.maxScore(nums, l, i - 1, left, curr)
                rightScore = self.maxScore(nums, i + 1, h, curr, right)
                ret = max(ret, leftScore + left * curr * right + rightScore)
        return ret

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        分治法思路：
        遍历最后选择戳破的气球，在此之前递归分别得到左右两侧的最大收益
        """
        vec = [1] + nums + [1]
        return self.maxScore(vec, 1, len(vec) - 2, 1, 1)

    # ===== 记忆化搜索 =====
    def maxScore(self, d, nums, l, h):
        """
        记忆化搜索，记录某个区间的最大值
        """
        curr = (l, h)
        if curr not in d:
            d[curr] = 0
            if l <= h:
                for i in range(l, h + 1):
                    leftScore = self.maxScore(d, nums, l, i - 1)
                    rightScore = self.maxScore(d, nums, i + 1, h)
                    d[curr] = max(d[curr], leftScore + nums[l - 1] * nums[i] * nums[h + 1] + rightScore)
        return d[curr]

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        分治法思路：
        遍历最后选择戳破的气球，在此之前递归分别得到左右两侧的最大收益
        """
        d, vec = dict(), [1] + nums + [1]
        return self.maxScore(d, vec, 1, len(vec) - 2)

    # ===== 动态规划 =====
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划
        """
        n = len(nums) + 2
        nums = [1] + nums + [1]
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j])
        return dp[1][n-2]