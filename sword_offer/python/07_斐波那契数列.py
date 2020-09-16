#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def Fibonacci(self, n):
        """
        递归，时间复杂度较大
        """
        if n < 2:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci2(self, n):
        """
        动态规划，使用列表存储并迭代
        """
        if n < 2:
            return n
        else:
            array = [0, 1]
            while len(array) - 1 < n:
                array.append(array[-2] + array[-1])
            return array[-1]

    def Fibonacci3(self, n):
        """
        动态规划，优化版
        """
        array = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                array[i%2] = array[0] + array[1]
        return array[n%2]

    def Fibonacci4(self, n):
        """
        动态规划，利用临时变量
        """
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for i in range(n-1):
            c = a + b
            a, b = b, c
        return c

    def test(self, n):
        """
        测试函数
        """
        func_vec = [self.Fibonacci,
                    self.Fibonacci2,
                    self.Fibonacci3,
                    self.Fibonacci4]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    for i in range(0, 39, 10):
        s.test(i)


if __name__ == "__main__":
    main()