#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def LeftRotateString1(self, s, n):
        """
        pythonic
        借助下标操作的解法
        """
        if s == "" or n <= 0 or n >= len(s):
            return s
        
        return s[n:] + s[0:n]

    def LeftRotateString2(self, s, n):
        """
        两两部分翻转，然后整体翻转
        """
        if s == "" or n <= 0 or n >= len(s):
            return s
        
        tmp = list(s)
        self.str_reverse(tmp, 0, n - 1)
        self.str_reverse(tmp, n, len(s) - 1)
        self.str_reverse(tmp, 0, len(s) - 1)
        return "".join(tmp)
    
    def LeftRotateString3(self, s, n):
        """
        两个相同字符串拼接，然后取自串
        """
        if s == "" or n <= 0 or n >= len(s):
            return s
        
        tmp = s + s
        return tmp[n:n+len(s)]

    def str_reverse(self, s, l ,h):
        """
        对s[l:h]实现翻转
        注意s是一个列表
        """
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
    
    def test(self, s, n):
        """
        测试函数
        """
        func_vec = [self.LeftRotateString1,
                    self.LeftRotateString2,
                    self.LeftRotateString3]
        print("=====")
        for func in func_vec:
            tmp_s = s[:]
            start = time.time()
            result = func(tmp_s, n)
            end = time.time()
            print("tims(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    str1 = "abcdefg"
    str2 = "abcXYZdef"
    str3 = "lrloseumgh"
 
    s = Solution()
    s.test(str1, 2)
    s.test(str2, 3)
    s.test(str3, 6)


if __name__ == "__main__":
    main()