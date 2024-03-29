#!/bin/bash python
"""
1438. 绝对差不超过限制的最长连续子数组

思路：
见注释
"""

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        思路：
        暴力枚举：两层循环确定区间，内层循环找到该区间的最大绝对差
        思考如何获取一个子数组的最大绝对差，能否使用迭代的方式：
        已知[a, b]区间的最大绝对差，最大值，最小值
        此时添加一个新的元素c，那么如何update最大绝对差
        ret = max(ret, abs(a-c), abs(b-c))
        因此得出一个结论：一个区间的最大绝对差，只和min/max有关
        问题在于当区间变更时，如何update区间的min/max

        暴力方法：
        外层遍历a，内层遍历b，然后可以遍历所有的区间，其中更新min/max
        整体的时间复杂度是：O(n^2)，当 n = 10^5 时，超时

        需要优化到O(n)的方法：
        动态规格，或者双指针滑窗
        如果是一维dp，得到dp[i]之后，无法递归得到dp[i+1]
        如果是滑窗法，需要思考滑窗可以覆盖所有的情况：
        1. 右指针正常移动，不满足要求时更新长度
        2. 左指针进行移动，最关键的是移动缩窗后能够快速得到min/max

        所以最终的算法是：
        滑窗法 + 单调栈，O(2n) + O(2n)
        """
        if nums == [] or limit < 0:
            return 0
        
        # 当前区间为：(l, h]
        maxLen, l = 0, -1
        minStack, maxStack = [], []
        for h in range(len(nums)):
            # 维护最小栈，单调递增
            while minStack and minStack[-1] > nums[h]:
                minStack.pop()
            # 维护最大值，单调递减
            while maxStack and maxStack[-1] < nums[h]:
                maxStack.pop()
            # 更新最小值，最大值
            minStack.append(nums[h])
            maxStack.append(nums[h])
            # 如果不满足要求，则缩窗直到满足要求
            while l < h and maxStack[0] - minStack[0] > limit:
                l += 1
                if nums[l] == maxStack[0]:
                    maxStack.pop(0)
                if nums[l] == minStack[0]:
                    minStack.pop(0)
            # 满足要求后更新长度
            maxLen = max(maxLen, h - l)
        return maxLen

    # ===== 优化版 =====
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        思路：
        1. 暴力方法：一重循环确定左侧边界，然后向右延申遍历，期间更新min/max，更新长度
                    时间复杂度O(n^2)
        2. 滑窗方法：当达到最大长度后，一定是两个端点不满足需求，此时需要移动左端点滑窗
                    右端点是一个极值，但是然后注意之后仍然需要内部遍历来获取另一个
                    min/max极值
        3. 优化方法：注意到本题的本质是获取滑动窗口的min/max，参考239.滑动窗口的最大值
                    可得需要两个双端队列来分别维持min/max
                    注意min/max的取值在滑动窗口后未必一定在两端
        """
        from collections import deque
        l, ret, mindq, maxdq = 0, 0, deque(), deque()
        for h in range(len(nums)):
            # 引入当前元素后更新两个单调序列
            while mindq and mindq[-1] > nums[h]:
                mindq.pop()
            while maxdq and maxdq[-1] < nums[h]:
                maxdq.pop()
            mindq.append(nums[h])
            maxdq.append(nums[h])
            # 进行滑窗直到满足limit要求，注意弹出左侧的元素
            while l < h and maxdq[0] - mindq[0] > limit:
                if nums[l] == maxdq[0]:
                    maxdq.popleft()
                if nums[l] == mindq[0]:
                    mindq.popleft()
                l += 1
            ret = max(ret, h - l + 1)
        return ret