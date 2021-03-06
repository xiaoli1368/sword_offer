#!/bin/bash python
"""
322. 零钱兑换

思路：
动态规划
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        由于每种硬币数量无限，所以是多重背包
        1. 是否可以组合得到target
        2. 在可以组合得到target的情况，要求所需元素个数最少

        dp[i][j]表示前i个元素，在能够凑成容量为j的情况下，所用最少元素个数，如果不能凑成则为-1
        dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - nums[i]])，注意保证 j >= nums[i]
        而且 dp[i][j - nums[i]] == -1 时，dp[i][j]取min也会等于-1
        状态压缩：dp[j] = min(dp[j], 1+ dp[j - nums[i]]), 并且j依赖本次的j-nums[i]，故正向遍历
        注意边界：dp[j] = 0, 其它初始化为float("+inf")
        """
        dp = [0] + [amount + 1] * amount
        for coin in coins:
            for j in range(coin, len(dp)):
                dp[j] = min(dp[j], 1 + dp[j - coin])
        return -1 if dp[-1] > amount else dp[-1]