#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def Power1(self, base, exponent):
        """
        暴力循环法，时间复杂度O(exponent)
        """
        if base == 0:
            return 0
        if base == 1 or exponent == 0:
            return 1
        
        sign = 1
        if exponent < 0:
            sign = -1
            exponent = -exponent

        ret = 1.0
        for i in range(exponent):
            ret *= base

        return ret if sign == 1 else 1 / ret
    
    def Power2(self, base, exponent):
        """
        快速幂方法
        需要处理符号
        """
        if base == 0:
            return 0
        
        ret = 1.0
        sign = True
        if exponent < 0:
            sign = False
            exponent = - exponent

        while exponent != 0:
            if exponent & 1 == 1:
                ret *= base
            base *= base
            exponent >>= 1
        
        return ret if sign else 1 / ret

    def Power3(self, base, exponent):
        """
        直接使用内置运算符号
        """
        return base**exponent

    def test(self, base, exponent):
        """
        测试函数
        """
        func_vec = [self.Power1, self.Power2, self.Power3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(base, exponent)
            end = time.time()
            print("time(us): {:>5.2f}, result: {:e}".format((end - start)*10**6, result))


def main():
    s = Solution()
    s.test(0, 0)
    s.test(0, 2)
    s.test(2, 0)
    s.test(1, 10086)
    s.test(2, 3)
    s.test(2, -3)
    s.test(3, 500)
    #s.test(4, 5000)    # int过大无法转为float
    #s.test(5, 6000000) # int过大无法转为float


if __name__ == "__main__":
    main()