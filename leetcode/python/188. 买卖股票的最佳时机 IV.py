#!/bin/bash python
"""
188. 买卖股票的最佳时机 IV

思路：
动态规划
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        原数组一定是上升和下降交错分布的，最终要求提取k个上升段，要求和最大
        1. 提取出所有的上升段，并求总和
        2. 如果上升段个数小于k，则直接返回总和
        3. 否则从中提取k个元素，要求和最大，标准的01背包问题（当然也可以直接排序取topk大）
           dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + value)
           dp[j] = max(dp[j], dp[j - 1] + value)
        
        这种方式是错的：
        例如：[3,2,6,5,0,3,1,3,2,4,5,1,7,2,1,2,3,1], 4
        上升段为：[4, 3, 2, 3, 6, 2]
        选取4段最大和为：6 + 4 + 3 + 3 = 16
        但是完全可以错开选择，也就是在原数组中选取 [0, 5] = 5, 最终 4 + 5 + 6 + 2 = 17
        """
        if prices == [] or k <= 0:
            return 0
        
        # 滑窗法找递增区间（[3, 5, 9] 结果长度为 6），[l, h)
        l = h = ssum = 0
        ups, n = [], len(prices)
        while l < n:
            h = l + 1
            while h < n and prices[h] > prices[h - 1]:
                h += 1
            curr = prices[h - 1] - prices[l]
            if curr > 0:
                ssum += curr
                ups.append(curr)
            l = h
        #print(ssum, ups)

        if len(ups) <= k:
            return ssum
        
        dp = [0] * (k + 1)
        for up in ups:
            for j in range(k, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + up)
            #print(dp)
        return dp[-1]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        在两次交易的基础上拓展到k次，使用两个数组记录状态：buy[j], sell[j]
        已知i-1时刻的buy/sell，则i时刻的状态递推方程为：
        buy[j] = min(buy[j], price - sell[j - 1])
        sell[j] = max(sell[j], price - buy[j])
        考虑初始化：0时候所有的sell收益都为0，所有的buy都是prices[0]
        考虑特殊情况：k=1，则表示只有一次买卖buy其实就是统计price之前的最小值
                     k=100，可能最大只有10次交易，但是后续交易统计了之前的收益，因此不影响
        """
        if prices == [] or k <= 0:
            return 0
        sell, buy = [0] * k, [prices[0]] * k
        for price in prices:
            for j in range(k):
                lastSell = 0 if j == 0 else sell[j - 1]
                buy[j] = min(buy[j], price - lastSell)
                sell[j] = max(sell[j], price - buy[j])
        return sell[-1]