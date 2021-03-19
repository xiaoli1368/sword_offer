#!/bin/bash python
"""
503. 下一个更大元素 II

思路：
单调栈，区别在于循环两次，使用取余转换索引
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        依旧是单调递减栈
        """
        if nums == []:
            return []
        
        n = len(nums)
        ret = [-1] * n
        stack = []

        for i in range(2 * n):
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()
                ret[j] = nums[i]
            stack.append(i)
        
        return ret

    # ===== 优化版 =====
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        单调递减栈循环两次
        这里需要存储的是下标
        """
        n = len(nums)
        stack, ret = [], [-1] * n
        for i in range(n * 2):
            j = i % n
            while stack and nums[stack[-1]] < nums[j]:
                ret[stack.pop()] = nums[j]
            stack.append(j)
        return ret