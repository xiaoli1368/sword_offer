#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def cutRope1(self, n):
        """
        递归法
        """
        if n <= 3:
            return n - 1
        
        ret = 0
        for i in range(2, n // 2 + 2):
            ret = max(ret, max(i*(n-i), i*self.cutRope1(n-i)))
        
        return ret
    
    def cutRope2(self, n):
        """
        动态规划
        """
        dp = [i for i in range(n+2)]
        for i in range(3, n + 1):
            for j in range(2, i // 2 + 2):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        
        return dp[n]

    def cutRope3(self, n):
        """
        贪心法
        """
        if n <= 3:
            return n - 1
        cnt3 = n // 3 - 1 if n % 3 == 1 else n // 3
        cnt2 = (n - cnt3 * 3) // 2
        return 2**cnt2 * 3**cnt3
    
    def test(self, n):
        """
        测试函数
        """
        func_vec = [self.cutRope1,
                    self.cutRope2,
                    self.cutRope3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    s.test(10)
    s.test(20)
    s.test(30)


if __name__ == "__main__":
    main()