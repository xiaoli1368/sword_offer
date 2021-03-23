#!/bin/bash python
"""
532. 数组中的 k-diff 数对

思路：
本质是hash
"""

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        1. 暴力思路：两重循环找到所有配对，判断是否diff=k，并且使用set去重
        2. 其它思路：使用hash从左到右遍历，在当前元素curr中，判断curr-k, curr+k
                    是否出现了，注意特殊情况curr之前出现过，或者k=0
                    curr出现，k!=0, 跳过
                    curr出现，k==0, cnt += d[curr]
                    curr未出现，寻找+-k，防止k重复
                    例子1：[1, 1, 4, 4] k = 3
                    例子2：[1, 1, 4, 4] k = 0
        """
        cnt, d = 0, dict()
        for curr in nums:
            if curr in d and k == 0:
                cnt += 1 if d[curr] == 1 else 0
            elif curr not in d:
                cnt += 1 if curr - k in d else 0
                if k != 0:
                    cnt += 1 if curr + k in d else 0
            d[curr] = 1 + d.get(curr, 0)
        return cnt

    # ===== 优化版 =====
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        优化版
        """
        cnt, d = 0, dict()
        for curr in nums:
            if curr in d and d[curr] == 1 and k == 0: # [curr, curr]
                cnt += 1
            if curr not in d and curr - k in d: # [curr - k, curr]
                cnt += 1
            if curr not in d and k != 0 and curr + k in d: #[ curr + k, curr]
                cnt += 1
            d[curr] = 1 + d.get(curr, 0)
        return cnt