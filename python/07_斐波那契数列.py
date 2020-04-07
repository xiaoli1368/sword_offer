#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def Fibonacci(self, n):
        """
        迭代的方式，花时间很长
        """
        if n < 2:
            return n
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci2(self, n):
        """
        使用列表存储并迭代的方式
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
        参考答案，更加高效的方式
        """
        array = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                array[i%2] = array[0] + array[1]
        return array[n%2]

    def Fibonacci4(self, n):
        """
        另一种方式
        """
        if n < 2:
            return n
        else:
            a = 0
            b = 1
            c = 0
            for i in range(n-1):
                c = a + b
                a = b
                b = c
            return c


def main():
    s = Solution()
    print(s.Fibonacci4(39))


if __name__ == "__main__":
    main()