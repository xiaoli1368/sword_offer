#!/bin/bash python
"""
680. 验证回文字符串 Ⅱ

思路：
正常按部就班遍历即可
优化的地方在于代码量，而非复杂度
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        1. 暴力方法：依次尝试删除每次字母，剩下的判断是否回文，O(n^2)
        2. 双指针法：直接左右双指针遍历，遇到不同时，分两种情况删除，然后判断
        """
        if s == "":
            return True
        
        # 判断是否回文，且找到不等的字符
        n = len(s)
        l, h = 0, n - 1
        while l < h and s[l] == s[h]:
            l += 1
            h -= 1
        
        # 如果本来就是回文串
        if l >= h:
            return True
        
        # 遇到了不同的字符，跳过l
        ll, hh = l + 1, h
        while ll < hh and s[ll] == s[hh]:
            ll += 1
            hh -= 1
        
        # 如果此时回文
        if ll >= hh:
            return True
        
        # 尝试跳过hh
        ll, hh = l, h - 1
        while ll < hh and s[ll] == s[hh]:
            ll += 1
            hh -= 1
        return ll >= hh

    def validPalindrome(self, s: str) -> bool:
        """
        先定位到第一个不同的位置，然后讨论两种跳过的情况是否回文
        """
        def check(s, l, h):
            # 进行回文串判断，并返回最终双指针的位置
            while l < h and s[l] == s[h]:
                l += 1
                h -= 1
            return l >= h, l, h
        # ===== 主函数 =====
        l, h = 0, len(s) - 1
        ret, l, h = check(s, l, h)
        return True if ret else check(s, l + 1, h)[0] or check(s, l, h - 1)[0]