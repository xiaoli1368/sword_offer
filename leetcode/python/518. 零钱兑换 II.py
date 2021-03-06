#!/bin/bash python
"""
518. 零钱兑换 II

思路：
动态规划
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        最先想到的是回溯法，先对coins排序，然后依次选取，注意每个元素可以选无限个
        由于数据量级为5000，因此DFS的复杂度很大

        思考完全背包问题
        dp[i][j]表示前i个元素可以凑成金额j的组合数，如果不能凑成则为0
        dp[i][j] = dp[i - 1][j] + dp[i][j - nums[i]]
        空间压缩：dp[j] = dp[j] + dp[j - nums[i]], j >= nums[i]，初始化为全0，但是dp[0]=1
        这样才能累加出结果，例如dp[1] = dp[1] + dp[1 - 1]
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin]
        return dp[-1]
