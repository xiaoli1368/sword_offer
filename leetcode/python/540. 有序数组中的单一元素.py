#!/bin/bash python
"""
540. 有序数组中的单一元素

思路：
这题还挺麻烦的，详解见代码注释，后续补充。
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        注意没有说明是递增还是递减
        """
        # 异或法，O(n) + O(1)
        """
        ret = 0
        for i in nums:
            ret ^= i
        return ret
        """
        # 二分法，O(logn) + O(1)
        # 在发生缺失之前，必然是偶奇索引处元素相同
        # 在发生缺失之后，必然是奇偶索引处元素相同
        # 缺失元素一定位于某个偶数索引上，所以如果某个偶数索引，前后都不等，得出结果
        # 与后面相等，则发生在缺失之前
        # 与前面相等，则发生在缺失之后
        if nums == []:
            return 0
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h + 1) // 2
            if m % 2 == 1: # 奇数调整为偶数
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        return nums[l]