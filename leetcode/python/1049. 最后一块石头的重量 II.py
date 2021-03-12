#!/bin/bash python
"""
1049. 最后一块石头的重量 II

思路：
一开始以为跟之前那个题没区别，直接贪心处理top2，结果错了
无法解决的用例是：[31,26,33,21,40]，正解为：40-21=19, 33-31=2, 26-19=7, 7-2=5
由贪心引发的优化方法有两种：；一是DFS回溯，二是动态规划
"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        贪心的方法是错误的
        考虑分成两堆，相撞后的结果，求最小可能重量
        也就是分割等和子集，01背包，背包容量为sum(stones)//2，重量和价值都是stones[i]
        dp[i][j]是对前i个物品当容量为j的时候最大重量
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        空间压缩：dp[j] = max(dp[j], dp[j - w] + v)，对j从后往前遍历
        """
        ssum = sum(stones)
        dp = [0] * (ssum // 2 + 1)
        for stone in stones:
            for j in range(len(dp) - 1, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return ssum - 2 * dp[-1]