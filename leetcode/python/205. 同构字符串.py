#!/bin/bash python
"""
205. 同构字符串

思路：
两个hash结构，分别判断两个字符串中是否已经出现重复字符
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d = dict()      # 记录由s到t的映射
        visited = set() # 记录t中已访问过的元素

        for i in range(len(s)):
            si, ti = s[i], t[i]
            if si not in d:
                if ti in visited:
                    return False
                else:
                    d[si] = ti 
                    visited.add(ti)
            else:
                if d[si] != ti:
                    return False
        return True