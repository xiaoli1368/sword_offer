#!/bin/bash python
"""
409. 最长回文串

思路：
哈希统计
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        直接hash统计即可，统计两个变量
        一是可以配对的字符总个数，二是是否存在单独的字符形成中心
        """
        ret, center, d = 0, 0, dict()
        for char in s:
            d[char] = 1 + d.get(char, 0)
        for char, cnt in d.items():
            if cnt % 2 == 0:
                ret += cnt
            elif cnt % 2 == 1:
                ret += cnt - 1
                center = 1
        return ret + center