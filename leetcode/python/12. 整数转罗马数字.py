#!/bin/bash python
"""
12. 整数转罗马数字

贪心法
构建映射表后，遍历即可
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        贪心法
        """
        d = [(1000, "M"),
             (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
             (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
             (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        ret = ""
        for pair in d:
            n, s = pair
            while num >= n:
                ret += s
                num -= n
        
        return ret