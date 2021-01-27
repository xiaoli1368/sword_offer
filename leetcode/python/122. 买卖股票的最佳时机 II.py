#!/bin/bash python
"""
122. 买卖股票的最佳时机 II

思路：
本质是统计递增段的最高度
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        dp[i]表示在第i天获取的最大利益，未必当天卖出
        遍历之前交易某个具备更低价格的节点j
        dp[i] = max(dp[i - 1], dp[j - 1] + prices[i] - prices[j])
        """
        if prices == []:
            return 0
        
        n = len(prices)
        dp = [0] * n
        mmax = 0
        mmin = prices[0] # 记录[0:i+1]的最小值

        for i in range(1, n):
            dp[i] = dp[i - 1] if i >= 1 else 0
            # 如果之前没有最小值，则跳过
            mmin = min(mmin, prices[i])
            if mmin == prices[i]:
                continue
            # 向左遍历，寻找可以进行多次交易的结果
            for j in range(i - 1, -1, -1):
                if prices[j] < prices[i]:
                    last = dp[j - 1] if j >= 1 else 0
                    dp[i] = max(dp[i], last + prices[i] - prices[j])
                    
        return dp[-1]
	
    def maxProfit(self, prices: List[int]) -> int:
        """
        统计连续递增的子区间即可
        """
        if prices == []:
            return 0
        
        ret = 0
        l = h = 0
        n = len(prices)

        while h < n:
            # 找到连续递增的区间
            while h + 1 < n and prices[h] < prices[h + 1]:
                h += 1
            # 累计结果
            ret += prices[h] - prices[l]
            # 更新指针
            h += 1
            l = h
        
        return ret

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        直接一维遍历，统计相邻两个元素的差值
        累加正差值，也就是相邻两天连续卖出
		这应该是最简写的写法了吧
        """
        ret, last = 0, float("+inf")
        for curr in prices:
            ret += max(0, curr - last)
            last = curr
        return ret