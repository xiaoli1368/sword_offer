#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def jumpFloorII(self, n):
        """
        循环计算法
        """
        if n == 0:
            return 0
        
        tmp = 1
        for i in range(n - 1):
            tmp *= 2
        return tmp

    def jumpFloorII2(self, n):
        """
        直接计算法

        """
        if n == 0:
            return 0
        else:
            return 2**(n - 1)

    def jumpFloorII3(self, n):
        """
        一行方法
        """
        return 0 if n == 0 else 2**(n - 1)


def main():
    s = Solution()
    print(s.jumpFloorII(9))
    print(s.jumpFloorII2(9))
    print(s.jumpFloorII3(9))


if __name__ == "__main__":
    main()