#!/bin/bash python
"""
123. 买卖股票的最佳时机 III

思路：
不太好想到，DP
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
		错解：双指针，统计两个递增的区间
        例如：[2, 6, 0, 3, 1, 7], 2
        上升段为：[4, 3, 6]，选取2段最大和为：4 + 6 = 10
        但是完全可以错开选择，也就是在原数组中选取 [2 -> 6, 0 -> 7]
        最终最大和为： 4 + 7 = 11
        """
        n = len(prices)
        ret = last = l = h = 0
        while h < n:
            # 寻找严格递增的区间
            while h + 1 < n and prices[h] < prices[h + 1]:
                h += 1
            # 更新结果
            curr = prices[h] - prices[l]
            ret = max(ret, last + curr)
            last = curr if curr > 0 else last
            # 更新指针
            h += 1
            l = h
        return ret

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        动态规划 + 状态机
        在第i天时只有5种状态：
            - 没有一次买卖
            - 进行了一次买，buy1
            - 进行了一次卖，sell1
            - 进行了一个买卖，然后第二次买，buy2
            - 进行了两次买卖，sell2
        由于第一种情况没有利润，因此考虑4种状态，同时每次必须进行买卖
        dp[i]表示第i天在4种状态下的最大收益，注意收益最大意味着：高价卖出，低价买入
            - buy1[i] = min(buy1[i - 1], prices[i])，维持buy1状态，尝试今天的更低价买入
            - sell1[i] = max(sell1[i - 1], prices[i] - buy1)，今天第一次卖出是否收益更大
            - buy2[i] = min(buy2[i], prices[i] - sell1[i])，第二次买入需要考虑第一次的获益
                        也就是说本意是用更低的价格来进行第二次买入，但是由于第一次进行获利了
                        因此第二次买入后的实际花费更少，这样引入sell1[i]后，第二次买卖会统计到
                        第一次的收益
            - sell2[i] = max(sell2[i], prices[i] - buy2[i])
        考虑初始化情况，在i=0天，如果分别完成了两次买卖，则收益都为0，如果两次买入，都是prices[0]
        """
        if prices == []:
            return 0
        sell1 = sell2 = 0
        buy1 = buy2 = prices[0]
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        return sell2