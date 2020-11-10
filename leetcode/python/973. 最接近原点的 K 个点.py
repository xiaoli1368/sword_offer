#!/bin/bash python
"""
973. 最接近原点的 K 个点

思路：
堆排序，快排
"""

class Solution(object):
    def heapify(self, points, distances, n, i):
        """
        堆化函数（维护小顶堆，小元素上浮）
        """
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and distances[l] < distances[smallest]:
            smallest = l
        if r < n and distances[r] < distances[smallest]:
            smallest = r
        if smallest != i:
            points[i], points[smallest] = points[smallest], points[i]
            distances[i], distances[smallest] = distances[smallest], distances[i]
            self.heapify(points, distances, n, smallest)

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(points)
        if points == 0 or k >= n:
            return points
        
        # 获取对应的距离平方数组
        distances = [0] * n
        for i in range(n):
            distances[i] = points[i][0]**2 + points[i][1]**2
	
	# ===== 另一种方式 =====
    def partition(self, points, l, h):
        """
        快排分区函数
        """
        start = l - 1
        for i in range(l, h):
            if points[i][0]**2+points[i][1]**2 < points[h][0]**2+points[h][1]**2:
                start += 1
                points[i], points[start] = points[start], points[i]
        start += 1
        points[h], points[start] = points[start], points[h]
        return start
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        使用快排的思路
        """
        if points == [] or k > len(points):
            return points
        
        # 找到第k大的元素，索引为k-1
        l, h = 0, len(points) - 1
        while l < h:
            m = self.partition(points, l, h)
            if m == k - 1:
                break
            elif m > k - 1:
                h = m - 1
            elif m < k - 1:
                l = m + 1
        
        # 返回前k小的元素
        return points[:k]