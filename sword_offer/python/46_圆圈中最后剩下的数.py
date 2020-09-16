#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def LastRemaining_Solution1(self, n, m):
        """
        暴力枚举
        """
        if n <= 0 or m <= 0:
            return -1

        i = -1
        step = 0
        count = n
        sign = [False] * n

        while count > 0:
            i = (i + 1) % n
            if sign[i]:
                continue
        
            step += 1
            if step == m:
                sign[i] = True
                step = 0
                count -= 1
    
        return i 

    def LastRemaining_Solution2(self, n, m):
        """
        递归法
        s(n)表示还剩下n个元素没有选中时的解
        递推公式： s(n) = (s(n-1) + m) % n
        """
        if n <= 0 or m <= 0:
            return -1
        
        if n == 1:
            return 0

        return (self.LastRemaining_Solution3(n - 1, m) + m) % n


    def LastRemaining_Solution3(self, n, m):
        """
        动态规划，反向迭代
        """
        if n <= 0 or m <= 0:
            return -1
        
        tsum = 0
        for i in range(2, n + 1):
            tsum = (tsum + m) % i

        return tsum

    def test(self, n, m):
        """
        测试函数
        """
        func_vec = [self.LastRemaining_Solution1,
                   self.LastRemaining_Solution2,
                   self.LastRemaining_Solution3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n, m)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    s.test(5, 3)
    s.test(10, 17)
    s.test(500, 300)
    s.test(2000, 4000) # 有些慢


if __name__ == "__main__":
    main()