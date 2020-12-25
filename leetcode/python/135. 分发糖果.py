#!/bin/bash python
"""
135. 分发糖果

思路：
贪心，先初始化每个元素为全1
然后调整左右两个方向，使其满足要求
先从左往右遍历，保证每个元素大于左侧
再从右往左遍历，每个元素大于右侧，且不能比之前的值小
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        ret = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                ret[i] = ret[i - 1] + 1 
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ret[i] = max(ret[i], ret[i + 1] + 1)
        
        return sum(ret)