#!/bin/bash python
"""
452. 用最少数量的箭引爆气球

思路：
一开始的思路
贪心，排序（首元素从大到小排序，然后末元素同样从大到小排序）
然后依次合并区间，直到不能合并，则需要发射一支新的箭
这里的合并区间其实是寻找更多的相交的区间
最终返回的是不同的相交区间的个数
"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        一开始的思路
        贪心，排序（首元素从大到小排序，然后末元素同样从大到小排序）
        然后依次合并区间，直到不能合并，则需要发射一支新的箭
        这里的合并区间其实是寻找更多的相交的区间
        最终返回的是不同的相交区间的个数
        """
        if points == []:
            return 0
        
        points.sort(key=lambda x : (x[0], x[1]))

        cnt = 0
        x1 = y1 = float("-inf")
        for i in range(len(points)):
            x2, y2 = points[i]
            if x2 <= y1: # 两个区间有交集
                x1, y1 = x2, min(y1, y2)
            else:
                cnt += 1
                x1, y1 = x2, y2
        
        return cnt