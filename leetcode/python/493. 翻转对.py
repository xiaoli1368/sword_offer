#!/bin/bash python
"""
493. 翻转对

基本上是归并排序的框架
核心问题是：在归并两个有序数组的时候，如何找到满足 nums[i] > 2*nums[j] 的情况

暴力方法是另行遍历一遍
更加高效一点的方法是二分查找
"""

class Solution(object):
    def merge(self, vec, l, m, h):
        """
        归并合并函数
        """
        # 一次遍历找到重要翻转对（可以使用二分查找优化）
        p, q = l, m + 1
        while p <= m and q <= h:
            if vec[p] > 2 * vec[q]:
                self.cnt += m - p + 1
                q += 1
            else:
                p += 1
        # 一次遍历合并两个有序数组
        tmp = vec[l:h+1]
        p, q = l, m + 1
        for i in range(l, h + 1):
            if p <= m and (q > h or tmp[p - l] <= tmp[q - l]):
                vec[i] = tmp[p - l]
                p += 1
            else:
                vec[i] = tmp[q - l]
                q += 1
        return
    
    def mergeSort(self, vec, l, h):
        """
        归并排序
        """
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(vec, l, m)
        self.mergeSort(vec, m + 1, h)
        self.merge(vec, l, m, h)
        return

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        self.cnt = 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt