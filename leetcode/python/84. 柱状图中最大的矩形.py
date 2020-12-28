#!/bin/bash python
"""
84. 柱状图中最大的矩形

思路：
1. 中间选定高度，两边分别遍历，超时了
2. 单调栈（需要想清楚是递减还是递增），选择递增
   因为使用递增栈，当不满足递增条件时，会出现一个山峰数组，此时山峰位置可以求解一个最大矩形
   pop之后，向左判断还可以继续求解最大矩形。（然而使用递减栈，找到山谷形状后，两边还是无法确定边界）
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        中间选定高度，两边遍历
        超时了
        """
        ret = 0
        for mid in range(len(heights)):
            left = right = mid
            while left - 1 >= 0 and heights[left - 1] >= heights[mid]:
                left -= 1
            while right + 1 < len(heights) and heights[right + 1] >= heights[mid]:
                right += 1
            ret = max(ret, heights[mid] * (right - left + 1))
        return ret

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调递增栈，保存下标，对应元素是递增的
        最大矩形面积，等于区间极值，高度为区间中的最小值，宽度为区间宽度
        使用单调递增栈，一旦不满足要求，则左侧会出现一个求值区间
        注意特殊情况，需要遍历到右侧数组外的一个位置
        """
        ret = 0
        stack = []

        for i in range(len(heights) + 1):
            while stack != [] and (i == len(heights) or heights[i] < heights[stack[-1]]):
                top = stack.pop()
                left = stack[-1] if stack else -1
                ret = max(ret, heights[top] * (i - left - 1))
            if i < len(heights):
                stack.append(i)
        
        return ret