#!/bin/bash python
"""
978. 最长湍流子数组

思路：
双指针滑窗
"""

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        复杂度为O(n)，双指针滑窗法
        last, curr: 表示相邻的差值状态，后面减去前面
        last, curr: [0, 1, -1]，表示初始状态，后面更大，后面更小
        """
        l, last, ret, n = 0, 0, 1, len(arr)
        if n <= 1:
            return n

        for h in range(1, n):
            curr = arr[h] - arr[h - 1]
            if last * curr < 0 or (last == 0 and curr != 0): # 满足要求
                ret = max(ret, h - l + 1)
            else: # 不满足要求，移动左指针，分两种情况
                l = h if curr == 0 else h - 1
            last = curr
        return ret