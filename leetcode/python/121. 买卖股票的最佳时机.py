#!/bin/bash python
"""
121. 买卖股票的最佳时机

思路：
动态规划
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i]表示以i元素结尾的情况下，获取的最大收益
        dp[i] = max(0, prices[i] - min)
        需要找到左侧的最小元素，因此需要一个遍历来迭代更新min
        空间优化：可以不使用dp数组，直接迭代
        """
        mmax, mmin = float("-inf"), float("+inf")
        for price in prices:
            mmin = min(mmin, price)
            mmax = max(mmax, price - mmin)
        return mmax