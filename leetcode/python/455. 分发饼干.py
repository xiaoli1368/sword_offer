#!/bin/bash python
"""
455. 分发饼干

思路：
贪心思路，先保证胃口小的孩子吃饱
先对g/s排序，双指针p/q分别指向s/g
依次遍历s，g中存在满足的则q自增，如果当前的g不满足，则后续也不可能满足
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        贪心思路，先保证胃口小的孩子吃饱
        先对g/s排序，双指针p/q分别指向s/g
        依次遍历s，g中存在满足的则q自增，如果当前的g不满足，则后续也不可能满足
        """
        if s == [] or g == []:
            return 0
        
        s.sort()
        g.sort()
        p = q = 0

        while p < len(s) and q < len(g):
            if s[p] >= g[q]:
                q += 1
            p += 1
        return q