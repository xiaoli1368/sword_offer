#!/bin/bash python
"""
20. 有效的括号

思路：
见注释
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        使用栈
        遇到 ( [ { 就push
        遇到 ) ] } 就尝试配对pop，如果无法配对则为False
        """
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in d:
                stack.append(char)
            elif stack and d[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return stack == []