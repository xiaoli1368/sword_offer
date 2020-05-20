#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def ReverseSentence1(self, s):
        """
        pythonic解法
        """
        if s == "":
            return s

        tmp = s.split(" ")
        tmp.reverse()
        return " ".join(tmp)

    def ReverseSentence2(self, s):
        """
        字符串翻转法
        """
        if s == "":
            return s

        l = 0
        h = 0
        length = len(s)
        tmp = list(s)

        while l <= h and h <= length:
            if h == length or s[h] == " ":
                self.str_reverse(tmp, l, h - 1)
                l = h + 1
            h += 1
        self.str_reverse(tmp, 0, length - 1)

        return "".join(tmp)

    def str_reverse(self, s, l, h):
        """
        工具函数，字符串翻转
        注意s是一个列表
        """
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
        
    def test(self, s):
        """
        测试函数
        """
        func_vec = [self.ReverseSentence1, self.ReverseSentence2]
        print("=====\n")
        for func in func_vec:
            start = time.time()
            result = func(s)
            end = time.time()
            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    strs = ["",
            "Student. a am I",
            "the sky is blue",
            "  hello world! ",
            "a good   example"]
    
    s = Solution()
    for ss in strs:
        s.test(ss)


if __name__ == "__main__":
    main()