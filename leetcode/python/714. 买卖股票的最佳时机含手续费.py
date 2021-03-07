#!/bin/bash python
"""
714. 买卖股票的最佳时机含手续费

思路：
动态规划
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        由于引入了每笔交易的手续费用，因此即便是放开了交易次数，也不能无限交易了
        像极了生育政策，放开了二胎，但是房价重压下，人口增长率依然萎靡

        当前的两个状态：买入，卖出
            buy[i] = min(buy[i - 1], price - sell[i - 1])
            sell[i] = max(sell[i - 1], price - buy[i - 1] - fee)
        """
        if prices == []:
            return 0
        buy, sell = prices[0], 0
        for price in prices:
            buy = min(buy, price - sell)
            sell = max(sell, price - buy - fee)
        return sell