#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def jumpFloorII(self, n):
        if n == 0:
            return 0
        else:
            return 2**(n-1)
        """
        更简单的方式：
        return 0 if n == 0 else 2**(n-1)
        """


def main():
    s = Solution()
    print(s.jumpFloorII(9))


if __name__ == "__main__":
    main()