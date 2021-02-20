#!bin/bash python
"""
697. 数组的度

思路：
一开始想成滑窗了，实际上直接一次hash就可以
"""

class Solution(object):
    # ===== 错解 =====
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        明确度的定义，一个连续数组内元素频数的最大值
        问题的求解：最短连续子数组，与整体同度
        1. nums的度一定是最大的，待求子数组的度也应该是最大的
        2. 如何保证待求子数组最短，需要优先保证度最大的情况下，取更短的路径

        最终的输出是一个长度值，因此只要确定[l, h]即可，滑窗法
        1. 移动右指针，如果度增大，则更新ret（注意此时度只可能增大或者不变）
        2. 在度增大后，缩窗以获取最短的子数组长度
        使用hash记录当前窗口内元素出现的情况，如何快速求解滑窗/缩窗后的度的变化？
        整体上看，右指针遍历一遍，左指针遍历一遍，复杂度为：时间O(2n) + 空间O(n)

        其它思路：
        1. 直接遍历找到最大的度，以及最高频元素
        2. 待求的最短连续子数组满足：左右两端都是相同的最高频元素
        3. 优化：初次遍历的时候，除了记录每个元素的度，还要记录每个元素出现的索引
        注意，最高频元素可能有多个
        """

        if nums == []:
            return 0
        length, valSet, d = 0, set(), dict()
        for index, val in enumerate(nums):
            # 更新hash
            if val not in d:
                d[val] = [0]
            d[val][0] += 1 
            d[val].append(index)
            # 更新最大频次信息
            if d[val][0] > length:
                length = d[val][0]
                valSet.clear()
                valSet.add(val)
            elif d[val][0] == length:
                valSet.add(val)

        ret = float("+inf")
        for val in valSet:
            for right in range(length, len(d[val])):
                left = right - length + 1
                ret = min(ret, d[val][right] - d[val][left] + 1)
        return ret

    # ===== 正解（究极优化版）=====
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        同一个元素必然只有一个度，因此最短的意义在于，当不同元素的度相同时取最短的长度
        当度最大时，区间一定是val所有index的最左侧和最右侧
        因此不需要记录所有的index，只要左右两端即可
        字典d保存的元素：[freq, left, right]
        """
        maxFre, minLen, d = 0, 0, dict()
        for index, val in enumerate(nums):
            # 更新hash
            if val not in d:
                d[val] = [0, index, index]
            d[val][0] += 1
            d[val][2] = index
            freq, left, right = d[val]
            # 更新长度，记录结果，优先取最高频的长度，再取相同频率下的更小长度
            if freq >= maxFre:
                currLen = right - left + 1
                minLen = currLen if freq > maxFre else min(minLen, currLen)
                maxFre = freq
        return minLen