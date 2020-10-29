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