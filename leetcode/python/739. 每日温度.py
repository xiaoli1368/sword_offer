#!/bin/bash python
"""
739. 每日温度

思路：单调栈
"""

class Solution:
    def dailyTemperatures(self, vec: List[int]) -> List[int]:
        """
        单调递减栈
        """
        if vec == []:
            return []
        
        stack = []
        ret = [0] * len(vec)

        for i in range(len(vec)):
            while stack and vec[stack[-1]] < vec[i]:
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        
        return ret

    # ===== 优化版 =====
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        获取当前元素到右侧最近更大值得下标距离
        单调递减栈，存储下标
        """
        n = len(T)
        stack, ret = [], [0] * n
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                top = stack.pop()
                ret[top] = i - top 
            stack.append(i)
        return ret