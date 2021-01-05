#!/bin/bash python
"""
830. 较大分组的位置

思路：
滑窗，遍历每个连续相同字符的窗口，保存符合要求的情况
其实就是一次遍历，使用双指针来保存两端信息
"""

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        滑窗法
        找到所有连续字符的窗口，保留长度大于等于3的情况
        """
        # 特殊情况
        n, ret = len(s), []
        if n < 3:
            return ret

        l = h = 0 # 定义[l, h]区间当前正在检测的区间
        while h < n:
            # 移动右指针
            while h + 1 < n and s[l] == s[h + 1]:
                h += 1
            # 保存结果
            if h - l >= 2:
                ret.append([l, h])
            # 移动左右指针
            h += 1
            l = h
        return ret