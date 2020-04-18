#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def Add(self, a, b):
        """
        递归法
        特别注意，python对负数进行二进制处理比较麻烦
        需要转换形式，并且注意是否溢出
        """
        tmp = a if b == 0 else self.Add((a^b) & 0xffffffff,
                                        ((a&b) << 1) & 0xffffffff)
        return tmp if tmp < 0x7fffffff else ~(tmp ^ 0xffffffff)

    def Add2(self, a, b):
        """
        循环
        """
        while b != 0:
            tmp = (a ^ b) & 0xffffffff
            b = ((a & b) << 1) & 0xffffffff
            a = tmp if tmp < 0x7fffffff else ~(tmp ^ 0xffffffff)
        return a


def main():
    s = Solution()
    print(s.Add(10 ,-12))
    print(s.Add2(10, -12))


if __name__ == "__main__":
    main()