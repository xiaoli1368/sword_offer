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