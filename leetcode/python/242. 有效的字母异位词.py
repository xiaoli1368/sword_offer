#!/bin/bash
"""
242. 有效的字母异位词

思路：
hash，或者使用char数组模拟hash
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        哈希
        """
        if len(s) != len(t): # 长度不等直接退出
            return False
        d = dict()
        for char in s:
            d[char] = 1 + d.get(char, 0)
        for char in t:
            if char in d:
                d[char] -= 1
            if char not in d or d[char] == -1:
                return False
        return True