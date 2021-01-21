#!/bin/bash python
"""
135. 分发糖果

思路：
贪心，先初始化每个元素为全1
然后调整左右两个方向，使其满足要求
先从左往右遍历，保证每个元素大于左侧
再从右往左遍历，每个元素大于右侧，且不能比之前的值小

举一反三：
1. 如果修改为比身旁孩子高，则必须获取比身旁孩子至少多2的糖果呢？
2. 如果比较的范围，扩大为周五半径为2的孩子，也就是左右各比较两个孩子。例如：
   grades: [1, 10, 1, 3, 2, 1]
   assign: [1,  2, 1, 3, 2, 1]
   当比较半径为2时，上述最优显然不满足要求了，所以需要改动贪心的策略，每次换滑窗半径为2.
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