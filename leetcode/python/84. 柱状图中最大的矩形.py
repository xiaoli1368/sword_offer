#!/bin/bash python
"""
84. 柱状图中最大的矩形

思路：
1. 中间选定高度，两边分别遍历，超时了
2. 单调栈（需要想清楚是递减还是递增），选择递增
   因为使用递增栈，当不满足递增条件时，会出现一个山峰数组，此时山峰位置可以求解一个最大矩形
   pop之后，向左判断还可以继续求解最大矩形。（然而使用递减栈，找到山谷形状后，两边还是无法确定边界）

当前区间的最大矩形，与区间长度以及区间最小值有关
暴力法是：中间选定高度，两端遍历，后者事先记录好每个元素两侧的最大值最小值
高效方法是：单调栈，因为要取最小值，因此维持一个单调递增的栈
每次只要满足单调性就push，不满足则说明出现了一个可以确定的状态
当前矩形的高度可以确定，宽度就是高度位置的在单调递增栈中的左右两侧
因为此时，左侧一定是小的，右侧因此还没push且也是小的，因此可以确定宽度
注意：左侧有可能为空，需要指定左侧的索引为-1，右侧有可能到头，因此需要控制多循环一次
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

    # ===== 优化版 =====
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        区间[i:j]的最大矩形面积 = 区间宽度 * 最低高度
        每个高度需要找到左右最近的更低高度x,y，这样区间[x+1:y-1]就是[i:j]
        因此使用单调递增栈, 内部存储下标用来计算宽度
        为了保证所有的情况都会遍历，必须增加后导的0，来清空单调递增栈，例如[1, 2, 3]
        同时stack必须增加前导的-1，来表示左侧的宽度边界，如[2, 1, -2]
        """
        heights.append(0)
        ret, stack = 0, [-1]
        for i in range(len(heights)):
            while len(stack) >= 2 and heights[stack[-1]] > heights[i]:
                min_height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ret = max(ret, width * min_height)
            stack.append(i)
        return ret