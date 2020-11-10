#!/bin/bash python
"""
347. 前 K 个高频元素

由于是提取前K个所有元素，因此需要堆排序
"""
class Solution(object):
    def heapify(self, vec, n, i):
        """
        堆化下沉函数，保证大顶堆
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and vec[l][1] > vec[largest][1]:
            largest = l
        if r < n and vec[r][1] > vec[largest][1]:
            largest = r
        if largest != i:
            vec[i], vec[largest] = vec[largest], vec[i]
            self.heapify(vec, n, largest)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 使用字典统计元素和次数
        d = dict()
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        # 转换为数组，内部元素为元组
        vec = []
        for key, value in d.items():
            vec.append((key, value))
        
        # 进行堆排序，提取前k个最大值
        ret = []
        n = len(vec)
        for i in range(n - 1, -1, -1):
            self.heapify(vec, n, i)
        for i in range(n - 1, n - k - 1, -1):
            ret.append(vec[0][0])
            vec[0], vec[i] = vec[i], vec[0]
            self.heapify(vec, i, 0)
        
        return ret
	
	# ===== 另一种方式 =====
    def partition(self, vec, l, h):
        """
        快排分区函数，从大到小
        """
        start = l - 1
        for i in range(l, h):
            if vec[i][1] > vec[h][1]:
                start += 1
                vec[i], vec[start] = vec[start], vec[i]
        start += 1
        vec[h], vec[start] = vec[start], vec[h]
        return start
    
    def quickSort(self, vec, l, h):
        """
        快排递归函数
        """
        if l >= h:
            return
        m = self.partition(vec, l, h)
        self.quickSort(vec, l, m - 1)
        self.quickSort(vec, m + 1, h)
        return

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        先获取频次字典，然后修正为元组列表，排序
        """
        if nums == [] or k > len(nums):
            return []
        
        # 获取频次字典
        d = dict()
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        
        # 转换为频次元素列表
        ret = [(num, fre) for num, fre in d.items()]

        # 二分找到第k大元素的位置，找到后对之前的排序
        index = k - 1
        l, h = 0, len(ret) - 1
        while l <= h:
            m = self.partition(ret, l, h)
            if m == index:
                self.quickSort(ret, 0, index)
                break
            elif m > index:
                h = m - 1
            elif m < index:
                l = m + 1
        
        # 返回结果
        return [x[0] for x in ret[:k]]