#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def Power(self, base, exponent):
        """
        直接使用内置运算符号
        """
        return base**exponent

    def Power2(self, base, exponent):
        """
        自行实现
        """
        if exponent == 0:
            return 1.0
        
        sign = False
        if exponent < 0:
            sign = True
            exponent = -exponent

        result = 1.0
        for i in range(exponent):
            result *= base

        if sign:
            result = 1 / result

        return result


def main():
    s = Solution()
    print(s.Power(2, 3))
    print(s.Power(2, -3))
    print(s.Power2(2, 3))
    print(s.Power2(2, -3))


if __name__ == "__main__":
    main()