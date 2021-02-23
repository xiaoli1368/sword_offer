#!/bin/bash python
"""
1052. 爱生气的书店老板

思路：
1. 累加和方法，复杂度：O(2n) + O(2n)
2. 滑窗法，复杂度：O(n)

举一反三：
思考在连续的时间段内，最多有多少的累加和满意度？
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        """
		累加和方法，将累加拆分为三段：左侧根据老板是否生气的实际累加Prat，中间使用技巧的直接累加，右侧实际累加
        感觉也可以尝试dp，dp[i]表示以i为结尾的最大满意数量，不使用技巧，使用技巧
        1 0 1 2 1 1 7 5
        0 1 0 1 0 1 0 1
        1 1 2 4 5 6 13 18 # 直接累加前缀和
        1 1 2 2 3 3 10 10 # 考虑生气前缀和
        注意要求的是整个数组的最大收益，而非是连续滑窗内的最大收益
        """
        # 特殊情况
        if customers == [] or grumpy == [] or x < 0:
            return 0
        
        # 累加前缀和
        n = len(grumpy)
        direSum = [0] * (n + 1)
        pratSum = [0] * (n + 1)
        for i in range(n):
            direSum[i + 1] = direSum[i] + customers[i]
            pratSum[i + 1] = pratSum[i] + (customers[i] if grumpy[i] == 0 else 0)

        # 特殊情况
        if x >= n:
            return direSum[n]

        # 获取整体最大值，当前使用技巧的窗口为 [i, j]
        ret = 0
        for i in range(n):
            j = i + x - 1
            if j + 1 <= n:
                curr = pratSum[i] + (direSum[j + 1] - direSum[i]) + (pratSum[-1] - pratSum[j + 1])
                ret = max(ret, curr)
        return ret

    # ===== 滑窗法 =====
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        """
        滑窗法
        固定滑窗统计两个数量即可
        一方面统计所有本来就不生气的累加和
        另一方面统计长度为x的窗口中最大可以挽回的累加和
        """
        # 特殊情况
        if customers == [] or grumpy == [] or x < 0:
            return 0
        # 滑窗法
        l = ssum = curr_extra = max_extra = 0
        for h in range(len(grumpy)):
            if h - l >= x: # 如果技巧脱离窗口
                if grumpy[l] == 1:
                    curr_extra -= customers[l]
                l += 1
            if grumpy[h] == 0: # 如果老板不生气
                ssum += customers[h]
            else: # 如果老板生气了，使用技巧解决
                curr_extra += customers[h]
                max_extra = max(max_extra, curr_extra)
        return ssum + max_extra

    # =====举一反三 =====
    # 思考在连续的时间段内，最多有多少的累加和满意度？（标准的滑窗法）
    def maxSatisfied(self, customers, grumpy, x):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        滑窗法，长度固定
        注意可以覆盖0的长度必须为x，但是连续1的长度可以大于x
        如果l为1，则可以继续延申
        如果l为0，则可以把右端x长度内的0视为1
        什么时候指针右移？当前位置为1，或者，当前位置为0，但在技巧范围内
        什么时候指针左移？

        感觉也可以尝试dp，dp[i]表示以i为结尾的最大满意数量，不使用技巧，使用技巧
        1 0 1 2 1 1 7 5
        0 1 0 1 0 1 0 1
        1 1 2 4 5 6 13 18 # 直接累加前缀和
        1 1 2 2 3 3 10 10 # 考虑生气前缀和
		DP不行

        注意这里要求的是是连续滑窗内的最大收益
        """
        # 特殊情况
        if customers == [] or grumpy == [] or x < 0:
            return 0
        
        # 滑窗法
        # 当前统计累加窗口：[l, h)
        # 当前使用技巧窗口：[l, l + x]
        n = len(grumpy)
        l = h = ret = ssum = 0
        while h < n:
            # 移动右指针并更新结果
            while h < n and (grumpy[h] == 1 or h - l < x):
                ssum += customers[h]
                ret = max(ret, ssum)
                h += 1
            # 移动左指针
            ssum -= customers[l]
            l += 1
        
        return ret