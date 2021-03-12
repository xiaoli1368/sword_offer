#!/bin/bash python
"""
1046. 最后一块石头的重量

思路：
使用堆来提取每次的最大值
注意默认的heapq是小顶堆
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if stones == []:
            return 0

        import heapq as hp
        vec = [-x for x in stones]
        hp.heapify(vec) # 小顶堆

        while len(vec) > 1:
            y = hp.heappop(vec)
            x = hp.heappop(vec)
            if x != y:
                hp.heappush(vec, y - x) # 注意压入负数
        
        return -vec[0] if vec else 0

    # ===== 手动实现大顶堆 =====
    def shift_down(self, vec, n, i):
        """
        大顶堆下沉函数
        """
        largest, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and vec[l] > vec[largest]:
            largest = l
        if r < n and vec[r] > vec[largest]:
            largest = r
        if largest != i:
            vec[i], vec[largest] = vec[largest], vec[i]
            self.shift_down(vec, n, largest)
        return
    
    def shift_up(self, vec, i):
        """
        大顶堆上浮函数
        """
        while i > 0:
            parent = (i - 1) // 2
            if vec[parent] < vec[i]:
                vec[parent], vec[i] = vec[i], vec[parent]
                i = parent
            else:
                break
        return
    
    def heapify(self, vec):
        """
        建立大顶堆
        """
        n = len(vec)
        for i in range(n//2-1, -1, -1):
            self.shift_down(vec, n, i)
        return
        
    def heappop(self, vec):
        """
        弹出堆顶，恢复排序
        """
        if vec:
            vec[0], vec[-1] = vec[-1], vec[0]
            self.shift_down(vec, len(vec) - 1, 0)
            return vec.pop()
    
    def heappush(self, vec, val):
        """
        插入元素，恢复排序
        """
        vec.append(val)
        self.shift_up(vec, len(vec) - 1)

    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        每次操作后需要快速获取最大值和次大值
        因此数据结构是大顶堆，涉及的操作有两个：
        1. 弹出最大值y，重建堆
        2. 再次弹出最大值x，重建堆
        3. 计算y-x，如果是0则不操作，非0则插入堆
        4. 根据堆是否为空，返回0或者最后一个元素
        """
        self.heapify(stones)
        while len(stones) >= 2:
            y = self.heappop(stones)
            x = self.heappop(stones)
            if y - x > 0:
                self.heappush(stones, y - x)
        return 0 if stones == [] else stones[0]