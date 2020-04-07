#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def jumpFloor(self, n):
        if n < 3:
            return n
        else:
            a = 1
            b = 2
            c = 3
            for i in range(n - 2):
                c = a + b
                a = b
                b = c
            return c


def main():
    s = Solution()
    print(s.jumpFloor(15))


if __name__ == "__main__":
    main()