#!/bin/bash python
"""
1248. 统计「优美子数组」

思路:
前缀和
"""

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        对奇数的个数进行前缀和，同时在生成前缀和hash的时候，前向查询-k
        """
        cnt, ssum, d, = 0, 0, {0: 1}
        for num in nums:
            if num % 2 == 1:
                ssum += 1 
            if ssum - k in d:
                cnt += d[ssum - k]
            d[ssum] = 1 + d.get(ssum, 0)
        return cnt