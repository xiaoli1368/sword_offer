#!/bin/bash python
"""
524. 通过删除字母匹配到字典里最长单词

思路：
正常的字符串双指针匹配问题，好像没有优化空间
"""

class Solution(object):
    def check(self, s, ss):
        """
        判断s是否可以通过删除字符来与ss匹配
        """
        i = j = 0
        m, n = len(s), len(ss)
        if m < n:
            return False
        while i < m and j < n:
            if s[i] == ss[j]:
                j += 1
            i += 1
        return j == n 

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        1. 字典排序，长度越长且字典序越小的靠前
        2. 遍历字典，与字符串进行匹配
        """
        if s == "" or d == []:
            return ""
        
        d.sort(key=lambda x : (-len(x), x))

        for ss in d:
            if self.check(s, ss):
                return ss
        return ""