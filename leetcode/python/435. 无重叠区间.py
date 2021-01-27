#!/bin/bash python
"""
435. 无重叠区间

思路：
先对区间结尾按由小到大排序，区间开头按照由大到小排序
也就是区间结尾越小，区间开头越大，则区间越靠前，越容易被保留下来
因为这样的区间长度最短，可以给其它区间更多选择的可能
然后优先保留结尾较小且和前一个不重合的区间

思考：其实只需要对结尾排序即可，因为是否对其实排序并不影响区间个数
		但是如果要求尽可能保留较大区间数量，并且要求总区间长度尽可能大
		那么对区间开头的排序就有意义了
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if intervals == []:
            return 0
        
        intervals.sort(key=lambda x: (x[1], -x[0]))

        cnt = last = 0
        for curr in range(1, len(intervals)):
            if intervals[curr][0] >= intervals[last][1]:
                last = curr
            else:
                cnt += 1
        return cnt

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        对区间结尾排序，从小到大
        """
        if intervals == []:
            return 0
        
        intervals.sort(key=lambda x : x[1])

        cnt = 0
        x1, y1 = intervals[0]
        for i in range(1, len(intervals)):
            x2, y2 = intervals[i]
            if x2 < y1: # 如果有重叠，移除当前
                cnt += 1
            else: # 没有重叠则更新
                x1, y1 = x2, y2
        return cnt