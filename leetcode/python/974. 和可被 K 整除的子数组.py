#!/bin/bash python
"""
974. 和可被 K 整除的子数组

思路：
1. 基本思路：暴力二重循环，判断和整除
2. 前缀和 + 哈希，每次遍历当前元素的时候，前向查找hash
   但是存在的问题是，对curr，需要查找多个值，如curr+k, curr-k, curr+2*k, curr-2*k, ...
   因为比较笨拙的方法是更新min,max，然后在这个范围内查找
   这种方式已经是O(n^2)了，不具备优越性
3. 取模优化
"""

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        使用前缀和来快速获取子数组和
        使用hash来进行前向查找
        (A - B) % m == 0
        A % k == B % k
        因此不存储ssum，而是存储ssum%k
        """
        cnt, ssum, d = 0, 0, {0: 1}
        for num in nums:
            ssum += num
            mod = ssum % k
            cnt += d.get(mod, 0)
            d[mod] = 1 + d.get(mod, 0)
        return cnt

