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
