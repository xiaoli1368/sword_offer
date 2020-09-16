#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def NumberOf1Between1AndN_Solution1(self, n):
        """
        暴力枚举法
        """
        if n <= 0:
            return 0
        
        ret = 0
        for i in range(n + 1):
            while i != 0:
                if i % 10 == 1:
                    ret += 1
                i //= 10
        
        return ret

    def NumberOf1Between1AndN_Solution2(self, n):
        """
        暴力求解，pythonic
        """
        return "".join(map(str, range(n + 1))).count("1")
    
    def NumberOf1Between1AndN_Solution3(self, n):
        """
        高效解法：直接版，易于理解
        """
        if n <= 0:
            return 0
        
        ret = 0
        digit = 1

        while digit <= n:
            # 分解数位
            curr = (n // digit) % 10
            high = n // digit // 10
            low = n % digit

            #分类讨论
            if curr == 0:
                ret += high * digit
            elif curr == 1:
                ret += high * digit + low + 1
            else:
                ret += (high + 1) * digit
            
            digit *= 10
        
        return ret

    def NumberOf1Between1AndN_Solution4(self, n):
        """
        高效解法：优化版，不易于理解
        """
        cnt = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            cnt += (a + 8) // 10 * m + (b + 1 if a % 10 == 1 else 0)
            m *= 10
        return cnt
    
    def test(self, n):
        """
        测试函数
        """
        func_vec = [self.NumberOf1Between1AndN_Solution1,
                    self.NumberOf1Between1AndN_Solution2,
                    self.NumberOf1Between1AndN_Solution3,
                    self.NumberOf1Between1AndN_Solution4]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(n)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    s = Solution()
    s.test(13)
    s.test(120)
    s.test(41206)
    s.test(5041608)


if __name__ == "__main__":
    main()