#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def LeftRotateString(self, s, n):
        """
        借助下标操作的解法
        """
        if s == "" or n == 0:
            return s
        
        return s[n:] + s[0:n]

    def str_reverse(self, s, l ,h):
        """
        对s[l:h]实现翻转
        """
        tmp = list(s)
        while l < h:
            tmp[l], tmp[h] = tmp[h], tmp[l]
            l += 1
            h -= 1
        s = str(tmp)

    def LeftRotateString2(self, s, n):
        if s == "" or n == 0:
            return s
        
        # 没有对输入的s进行保护
        self.str_reverse(s, 0, n - 1)
        self.str_reverse(s, n, len(s) - 1)
        self.str_reverse(s, 0, len(s) - 1)
        return s


def main():
    s = Solution()
    ss = "absXYZdef"

    print(ss)
    print(s.LeftRotateString(ss, 3))
    print(s.LeftRotateString2(ss, 3))


if __name__ == "__main__":
    main()