#!/bin/bash python
"""
27. 移除元素

思路：
1. 快排分区，双指针，都是从前往后遍历，相当于把val和非val进行分区
2. 双指针，左右遍历，左指向值val的位置，右指向值非val的位置，交换

注意：
快排本身不是一个稳定的排序，但是可以保证单次分区的时候，半个区间有序
本题目中，另一个半区的值全为val，因此快排分区可以保证整体有序稳定
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        start = -1
        for i in range(len(nums)):
            if nums[i] != val:
                start += 1
                nums[i], nums[start] = nums[start], nums[i]
        return start + 1
    
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        l, h = 0, len(nums) - 1
        while l < h:
            while l < h and nums[l] != val:
                l += 1
            while l < h and nums[h] == val:
                h -= 1
            if l < h:
                nums[l], nums[h] = nums[h], nums[l]
        return l if nums[l] == val else l + 1 # 当数据长度为1时存在特殊情况处理