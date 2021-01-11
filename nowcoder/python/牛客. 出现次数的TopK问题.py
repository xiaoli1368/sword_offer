#!/bin/bash python
"""
牛客. 出现次数的TopK问题

思路：
正常的大顶堆topk
"""
#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
class Solution:
    def heapify(self, vec, n, i):
        """
        堆化下沉函数，大顶堆
        次数越大，字典序越小，越靠前
        """
        largest, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and (vec[l][0] > vec[largest][0] or (vec[l][0] == vec[largest][0] and vec[l][1] < vec[largest][1])):
            largest = l
        if r < n and (vec[r][0] > vec[largest][0] or (vec[r][0] == vec[largest][0] and vec[r][1] < vec[largest][1])):
            largest = r
        if largest != i:
            vec[i], vec[largest] = vec[largest], vec[i]
            self.heapify(vec, n, largest)
    
    def topKstrings(self , strings , k):
        # write code here
        # 特殊情况
        if strings == [] or k <= 0:
            return []
        # 确定每个字符串出现的次数
        d = dict()
        for s in strings:
            d[s] = 1 + d.get(s, 0)
        # 转换字典为数组，每个元素为(次数，字符串)
        vec = [(cnt, s) for s, cnt in d.items()]
        # 建立大顶堆
        n = len(vec)
        for i in range(n//2-1, -1, -1):
            self.heapify(vec, n, i)
        # 进行堆排序，获取前k大元素，放置到数组后k个位置和ret
        ret = []
        for i in range(n - 1, n - 1 - k, -1):
            cnt, s = vec[0]
            ret.append([s, str(cnt)])
            vec[0], vec[i] = vec[i], vec[0]
            self.heapify(vec, i, 0)
        # 返回结果
        return ret