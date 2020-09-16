#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def jumpFloor(self, n):
        """
        动态规划
        """
        if n < 3:
            return n

        a, b, c = 1, 2, 3
        for i in range(n - 2):
            c = a + b
            a, b = b, c
        return c

    def test(self, n):
        """
        测试函数
        """
        start = time.time()
        result = self.jumpFloor(n)
        end = time.time()
        print("time(us): {:5.2f}, input: {:2d}, result: {:d}".format((end - start)*10**6, n, result))


def main():
    s = Solution()
    for i in range(0, 41, 10):
        s.test(i)


if __name__ == "__main__":
    main()