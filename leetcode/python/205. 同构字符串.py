#!/bin/bash python
"""
205. 同构字符串

思路：
hash
"""

class Solution:
    # ===== 第一版 =====
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

    # ===== 第二版 =====
    def isIsomorphic2(self, s, t):
        """
        需要两个hash
        """
        ss, tt = dict(), set()
        for i in range(len(s)):
            si, ti = s[i], t[i]
            if si not in ss and ti not in tt:
                ss[si] = ti
                tt.add(ti)
            elif si not in ss and ti in tt:
                return False
            elif si in ss and ti != ss[si]:
                return False
        return True