#!/bin/bash
"""
215. 数组中的第K个最大元素

思路：
快排，或者堆排序
"""

class Solution(object):
    def partition(self, vec, l, h):
        """
        快排分区函数，从大到小排序
        """
        start = l - 1
        for i in range(l, h):
            if vec[i] > vec[h]:
                start += 1
                vec[i], vec[start] = vec[start], vec[i]
        start += 1
        vec[h], vec[start] = vec[start], vec[h]
        return start

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        基于快排
        """
        if nums == [] or k > len(nums):
            return 0
        
        k -= 1
        l, h = 0, len(nums) - 1
        while l <= h:
            m = self.partition(nums, l, h)
            if m == k:
                return nums[m]
            elif m > k:
                h = m - 1
            elif m < k:
                l = m + 1
        
        return 0
	
	# ===== 另一种方法 =====
    def heapify(self, vec, n, i):
        """
        堆化函数，大顶堆
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and vec[l] > vec[largest]:
            largest = l
        if r < n and vec[r] > vec[largest]:
            largest = r
        if largest != i:
            vec[i], vec[largest] = vec[largest], vec[i]
            self.heapify(vec, n, largest)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == [] or k > len(nums):
            return 0
        n = len(nums)
        # 建立大顶堆
        for i in range(n//2-1, -1, -1):
            self.heapify(nums, n, i)
        # 移动topk到末尾，末尾最大
        for i in range(n - 1, n - k - 1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return nums[-k]