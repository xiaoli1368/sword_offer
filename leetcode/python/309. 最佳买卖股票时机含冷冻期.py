#!/bin/bash python
"""
309. 最佳买卖股票时机含冷冻期

思路：
动态规划

follow up:
1. 如果冷冻期变为k天则如何？
2. 如果运行买卖的次数变为k次则如何？
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        dp[i]表示在第i天的最大收益，dp有以下几种情况，因此构建状态机：
            - 什么也没有发生
            - 当前处于冷冻期，freeze
            - 完成了一次买入，buy
            - 完成了一次卖出，sell
        其中前两种状态没有收益，思考状态跳变方程：
            buy[i] = min(buy[i - 1], price - sell[i - 2])
                     以更低的价格来买入，同时累计上一次收益，注意由于冷冻期，所以上次收益为i-2
            sell[i] = max(sell[i - 1],  price - buy[i - 1])
        """
        if prices == []:
            return 0
        
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = prices[0]

        for i in range(1, n):
            lastSell = 0 if i < 2 else sell[i - 2]
            buy[i] = min(buy[i - 1], prices[i] - lastSell)
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1])
        return sell[-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        原版方程：（由3个之前的变量来更新当前的2个变量）
            buy[i] = min(buy[i - 1], price - sell[i - 2])
            sell[i] = max(sell[i - 1],  price - buy[i - 1])
        使用迭代的方式优化版，只需要记录5个变量:
            curr_buy, last_buy, curr_sell, last_sell, last2_sell
        迭代方式：
            curr_buy = min(last_buy, price - last2_sell)
            curr_sell = max(last_sell, price - last_buy)
            last_buy = curr_buy
            last2_sell = last_sell
            last_sell = curr_sell
        """
        if prices == []:
            return 0
        last_buy, last_sell, last2_sell = prices[0], 0, 0
        for price in prices:
            curr_buy = min(last_buy, price - last2_sell)
            curr_sell = max(last_sell, price - last_buy)
            last_buy, last2_sell, last_sell = curr_buy, last_sell, curr_sell
        return curr_sell