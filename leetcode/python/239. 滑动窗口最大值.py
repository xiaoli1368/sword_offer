#!/bin/bash python
"""
239. 滑动窗口最大值

思路：
单调队列，因为需要最大值，所以维持单调递减队列，双端队列
这样每次左侧都是最大值，关于更新的策略如下：
1. 右侧添加元素，需要保持单调递减特性
2. 左侧超出滑窗范围时，需要左侧弹出
3. 当达到窗口大小时，才开始输出
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == [] or k <= 0 or k > len(nums):
            return []
        
        ret, queue = [], []
        for i in range(len(nums)):
            # 维护单调递减
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            # 如果头部滑出窗口了则删除
            if queue[0] + k <= i:
                queue.pop(0)
            # 当达到窗口大小的时候，更新结果
            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret