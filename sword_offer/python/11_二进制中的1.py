#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def NumberOf1(self, n):
        """
        循环移位法
        注意与操作0xffffffff
        这样并不是获得了一个补码
        而是获得了一个正数，这个正数与n的补码具有相同个数的1
        python中，对负数右移会陷入死循环，因为负数的最高位最是保证为1
        因此python中对负数进行二进制操作时，先要使用0xffffffff化为等价的正数
        """
        result = 0
        if n < 0:
            n = n & 0xffffffff
        while n > 0:
            if n & 1 == 1:
                result += 1
            n = n >> 1
        return result

    def NumberOf1_easy(self, n):
        """
        依次找最后一位1
        """
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt

    def test(self, n):
        """
        测试函数
        """
        func_vec = [self.NumberOf1, self.NumberOf1_easy]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n)
            end = time.time()
            print("result: {:2d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    s.test(8)
    s.test(-7)
    s.test(-1)
    s.test(0x7fffffff)
    s.test(0xffffffff)


if __name__ == "__main__":
    main()