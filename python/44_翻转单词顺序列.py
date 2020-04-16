#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def ReverseSentence(self, s):
        """
        pythonic解法
        """
        if s == "":
            return s

        tmp = s.split(" ")
        tmp.reverse()
        return " ".join(tmp)

    def str_reverse(self, s, l, h):
        tmp = list(s)
        while l < h:
            tmp[l], tmp[h] = tmp[h], tmp[l]
            l += 1
            h -= 1
        s = str(tmp)
        
    def ReverseSentence2(self, s):
        """
        字符串翻转法
        """
        if s == "":
            return s

        l = 0
        h = 0
        length = len(s)

        while l <= h and h <= length:
            if h == length or s[h] == " ":
                self.str_reverse(s, l, h - 1)
                l = h + 1
            h += 1
        self.str_reverse(s, 0, length - 1)

        return s


def main():
    s = Solution()
    s1 = "Student a am I"
    s2 = s1[:]
    print(s1)
    print(s.ReverseSentence(s1))
    print(s2)
    print(s.ReverseSentence2(s2))


if __name__ == "__main__":
    main()