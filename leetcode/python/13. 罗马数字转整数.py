#!/bin/bash python
"""
13. 罗马数字转整数

同样也是贪心法
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        贪心法
        """
        d = [(1000, "M"),
             (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
             (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
             (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        n = 0 # 最终结果
        i = 0 # 字符串指针
        j = 0 # 映射集中的指针

        while i < len(s):
            num, sstr = d[j]
            if s.startswith(sstr, i):
                n += num
                i += len(sstr)
            else:
                j += 1
        
        return n