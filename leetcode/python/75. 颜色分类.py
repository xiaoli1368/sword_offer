#!/bin/bash python
"""
75. 颜色分类

思路：
1. 计数排序，需要额外空间
2. 三指针法
3. 与三指针法基本一致，核心还是快排分区
  （注意到，因为这里只有三种元素0/1/2，因此快排分区对分区后的内部顺序没有影响）
  （但如果存在多个不同的元素，那么就有影响了，快排分区只能保证一个子区域内部稳定有序）
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
		两次快排，效率不高
        """
        if nums == []:
            return
        n = len(nums)
        
        # 两次快排分区
        t0 = -1
        for i in range(n):
            if nums[i] == 0:
                t0 += 1
                nums[i], nums[t0] = nums[t0], nums[i]
        
        t2 = n
        for i in range(n - 1, -1, -1):
            if nums[i] == 2:
                t2 -= 1
                nums[i], nums[t2] = nums[t2], nums[i]
        
        return

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        计数排序
        """
        if nums == []:
            return
        cnt = [0, 0, 0]
        for i in nums:
            cnt[i] += 1
        i = j = 0
        while j < len(cnt):
            while cnt[j] > 0:
                nums[i] = j
                cnt[j] -= 1
                i += 1
            j += 1
        return
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        三指针法
        """
        if nums == []:
            return
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1
        return

        """
        这个四指针的思路有问题
        问题在于对指针的定义不清晰，p0p2定义为了已排好序的0/2的下一个位置
        p0表示从左到右的第一个非0的位置
        p2表示从右到左的第一个非2的位置
        while l <= h:
            if nums[p0] == 0:
                p0 += 1
            if nums[p2] == 2:
                p2 -= 1

            if nums[l] == 2 and p2 > l:
                nums[l], nums[p2] = nums[p2], nums[l]
            else:
                l += 1

            if nums[h] == 0 and p0 < h:
                nums[h], nums[p0] = nums[p0], nums[h]
            else:
                h -= 1
        """
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        类似于快排分区，两端三指针
		这个效率最好，建议全文背诵
        p0表示已经排好的0的尾部，向右延申
        p2表示已经排好的2的尾部，向左延申
        p1表示当前正在遍历的元素
        """
        if nums == []:
            return
        p0, p1, p2 = -1, 0, len(nums)
        while p1 < p2:
            if nums[p1] == 1 or p1 == p0:
                p1 += 1
            elif nums[p1] == 0:
                p0 += 1
                nums[p1], nums[p0] = nums[p0], nums[p1]
            elif nums[p1] == 2:
                p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
        return