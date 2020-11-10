#!/bin/bash python
"""
692. 前K个高频单词

思路：
快排，堆排序
"""

class Solution(object):
    def heapify(self, vec, n, i):
        """
        大顶堆，堆化函数
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and (vec[l][1] > vec[largest][1] or (vec[l][1] == vec[largest][1] and vec[l][0] < vec[largest][0])):
            largest = l
        if r < n and (vec[r][1] > vec[largest][1] or (vec[r][1] == vec[largest][1] and vec[r][0] < vec[largest][0])):
            largest = r
        if largest != i:
            vec[i], vec[largest] = vec[largest], vec[i]
            self.heapify(vec, n, largest)

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # hash统计不重复单词，以及各自出现的次数
        d = dict()
        for word in words:
            d[word] = 1 + d.get(word, 0)
        
        # 转换为list，内部保存了元组
        vec = [(key, value) for key, value in d.items()]
        n = len(vec)
        
        # 特殊情况
        if k <= 0 or k > n:
            return [x[0] for x in vec]
        
        # 建立大顶堆
        for i in range(n//2-1, -1, -1):
            self.heapify(vec, n, i)
        
        # 获取前k个最大值
        for i in range(n - 1, n - k - 1, -1):
            vec[0], vec[i] = vec[i], vec[0]
            self.heapify(vec, i, 0)
        
        # 返回结果
        return [x[0] for x in vec[-1:-k-1:-1]]
	
	# ===== 另一种方式 =====
    def partition(self, vec, l, h):
        """
        快排分区函数
        """
        start = l - 1
        for i in range(l, h):
            if vec[i][1] > vec[h][1] or (vec[i][1] == vec[h][1] and vec[i][0] < vec[h][0]):
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

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # 转换为频次字典
        d = dict()
        for word in words:
            d[word] = 1 + d.get(word, 0)

        # 转换为频次元组列表
        ret = [(num, fre) for num, fre in d.items()]
        
        # 特殊情况
        if k <= 0 or k > len(ret):
            return []
        
        # 二分查找topk，索引为k-1，找到后排序
        l, h = 0, len(ret) - 1
        while l <= h:
            m = self.partition(ret, l, h)
            if m == k - 1:
                self.quickSort(ret, 0, k - 1)
                break
            elif m > k - 1:
                h = m - 1
            elif m < k - 1:
                l = m + 1
        
        # 返回结果
        return [x[0] for x in ret[:k]]