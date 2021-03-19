#!/bin/bash python
"""
496. 下一个更大元素 I

思路：
使用hash以及单调栈1
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        对num2使用单调递减栈
        """
        if nums1 == [] or nums2 == []:
            return []
        
        d = dict()
        n = len(nums1)
        ret = [-1] * n
        stack = []

        # 建立nums1中从val到index的映射
        for ind, val in enumerate(nums1):
            d[val] = ind
        
        # 主循环，这里stack存值即可
        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                if val in d:
                    ret[d[val]] = num
            stack.append(num)
        
        return ret

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        其它思路，先使用栈，后使用字典
        """
        d = dict()
        stack = [] # 存值，而不是索引
        for i in range(len(nums2) + 1):
            while stack != [] and (i == len(nums2) or nums2[i] > stack[-1]):
                top = stack.pop()
                d[top] = nums2[i] if i < len(nums2) else -1
            if i < len(nums2):
                stack.append(nums2[i])
        
        ret = [0] * len(nums1)
        for i in range(len(ret)):
            ret[i] = d[nums1[i]]
        
        return ret

    # ===== 优化版 =====
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        使用单调递减栈，获取当前元素的右侧最近更大值
        同时需要一个hash记录待求val的下标，并且初始化为全-1
        """
        n1, n2 = len(nums1), len(nums2)
        d, stack, ret = dict(), [], [-1] * n1
        for i in range(n1):
            d[nums1[i]] = i
        for val in nums2:
            while stack and stack[-1] < val:
                num = stack.pop()
                if num in d:
                    ret[d[num]] = val
            stack.append(val)
        return ret