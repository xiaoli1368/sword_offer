#!/bin/bash python
"""
594. 最长和谐子序列
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        由于是子序列，所以可以不连续
        那么最长的和谐子序列长度就是：freq(a) + freq(a+1)
        就是相邻两个val的出现次数总和，注意必须保证两个val相差为1
        """
        cnt, d = 0, dict()
        for num in nums:
            d[num] = 1 + d.get(num, 0)
            if num + 1 in d:
                cnt = max(cnt, d[num] + d[num + 1])
            if num - 1 in d:
                cnt = max(cnt, d[num] + d[num - 1])
        return cnt