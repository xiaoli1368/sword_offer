#!/bin/bash python
"""
125. 验证回文串

思路：
正常遍历即可，注意需要保证只选择数字和字母，并且字母忽略大小写
"""

class Solution(object):
    def getASCII(self, char):
        """
        获取一个字符的ASCII码
        特别的，对于小写字母获取大写字母的ASCII码
        其它字符，返回-1
        """
        tmp = ord(char)
        if 0x30 <= tmp <= 0x39: # 数字
            return tmp
        elif 0x41 <= tmp <= 0x5A: # 大写字母
            return tmp
        elif 0x61 <= tmp <= 0x7A: # 小写字母
            return tmp - 0x20
        else:
            return -1

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, h = 0, len(s) - 1
        while l < h:
            while l < h and self.getASCII(s[l]) < 0:
                l += 1
            while l < h and self.getASCII(s[h]) < 0:
                h -= 1
            if self.getASCII(s[l]) == self.getASCII(s[h]):
                l += 1
                h -= 1
            else:
                break
        return l >= h