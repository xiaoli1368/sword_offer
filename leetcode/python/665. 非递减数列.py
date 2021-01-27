#!/bin/bash python
"""
665. 非递减数列

思路：
1. 个人思路：寻找存在逆序（递减）的情况进行计数统计，如果多于一对，则无法满足要求
            而在调整逆序对到非递减情况时，优先调整第一个元素，否则尝试调整第二个元素
2. 参考思路：
     * 见CPP
     * 1.遍历累加相邻两点递减次数，设为d。
     * 2.遍历累加间隔一点的前后两点递减次数，设为g。
     * 3.如果d或g为2，则为False，反之为True。
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        统计存在多少个相邻的逆序（严格递减）
        当出现逆序对时，优先尝试减小第一个元素
        如果不成功，则尝试增大第二次个元素
        """
        if nums == []:
            return True
        
        cnt = 0
        for i in range(len(nums)):
            # 如果出现了逆序对
            if i - 1 >= 0 and nums[i - 1] > nums[i]:
                cnt += 1
                # 尝试减小第一个数
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i] # 注意这里不能选择nums[i-1] = num[i-2]，因为i-2可能越界
                else: # 尝试减小第二个数
                    nums[i] = nums[i - 1]
            # 判断逆序对个数
            if cnt > 1:
                return False
        return True