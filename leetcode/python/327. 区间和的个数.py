#!/bin/bash python
"""
327. 区间和的个数

思路：
1. 转换为前缀和（所有i和j的差值满足条件的计数），注意前缀和数组多一个0元素，且整体未必有序
2. 对前缀和进行归并排序
3. 归并两个有序数组，其中统计a[i] - b[j]满足差值的情况（遍历每个i，定义双指针left和right，从b数组的头部开始遍历，left找到左边界，right找到有边界，对下一个i，left和right在上一次的基础上移动即可）
"""

class Solution(object):
    def merge(self, vec, l, m, h, lower, upper):
        """
        归并合并函数
        """
        # 统计结果，定义[left, right)区间为满足要求
        left = right = m + 1
        for j in range(l, m + 1):
            while left <= h and vec[left] - vec[j] < lower:
                left += 1 
            while right <= h and vec[right] - vec[j] <= upper:
                right += 1
            self.cnt += right - left
        # 排序
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
    
    def mergeSort(self, vec, l, h, lower, upper):
        """
        归并递归函数
        """
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(vec, l, m, lower, upper)
        self.mergeSort(vec, m + 1, h, lower, upper)
        self.merge(vec, l, m, h, lower, upper)
        return

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # 特殊情况
        if nums == []:
            return 0
        # 获取前缀和，注意多一位
        n = len(nums)
        vec = [0] * (n + 1)
        for i in range(1, n + 1):
            vec[i] = vec[i - 1] + nums[i - 1]
        # 归并排序并统计个数
        self.cnt = 0
        self.mergeSort(vec, 0, n, lower, upper)
        return self.cnt