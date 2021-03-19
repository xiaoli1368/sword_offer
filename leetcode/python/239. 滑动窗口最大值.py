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

    # ===== 优化版 =====
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        思路：
        1. 暴力方法：一重循环遍历左侧起始位置，然后向右遍历k个位置，期间更新最大值
                    时间复杂度O(n * k)
        2. 高效思路：由于滑动窗口，右侧添加元素，左侧弹出元素，所以可以使用队列模拟
                    如果窗口内出现[a, b] b < a 的情况，那么向右滑动时a总是无效的
                    因此需要弹出a，添加b，由此形成了类似于单调递减栈的结构
                    由于左侧只有弹出，由于存在弹出和添加两种情况，因此使用双端队列
                    并且队列保存单调递减，左侧总是max
        """
        from collections import deque
        ret, deque = list(), deque()
        for i in range(len(nums)):
            # 维护队列的单调递减特性
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            # 添加当前元素
            deque.append(i)
            # 弹出头部元素
            if i - deque[0] >= k:
                deque.popleft()
            # 添加到结果中
            if i >= k - 1:
                ret.append(nums[deque[0]])
        return ret