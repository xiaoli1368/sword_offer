#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def Sum_Solution1(self, n):
        """
        递归解法
        """
        tmp = n and self.Sum_Solution1(n - 1)
        return n + tmp

    def Sum_Solution2(self, n):
        """
        利用sum函数
        """
        return sum(list(range(1, n + 1)))

    def Sum_Solution3(self, n):
        """
        利用乘方
        """
        return (n**2 + n) >> 1

    def test(self, n):
        """
        测试函数
        """
        func_vec = [self.Sum_Solution1,
                    self.Sum_Solution2,
                    self.Sum_Solution3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    s.test(10)


if __name__ == "__main__":
    main()