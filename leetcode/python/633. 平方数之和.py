#!/bin/bash python
"""
633. 平方数之和

"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        有序数组，双指针，两端查找
        1. 非负整数，包括0
        2. 两个整数可以相等
        3. 可以提前使用sqrt(c)放缩查找区间
        """
        if c < 0:
            return False
        
        l, h = 0, round(c**0.5) + 1
        while l <= h:
            tmp = l**2 + h**2
            if tmp == c:
                return True
            elif tmp < c:
                l += 1
            else:
                h -= 1
        return False