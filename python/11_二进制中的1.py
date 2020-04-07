#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def NumberOf1(self, n):
        """
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
        高效解法
        """
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt
            

def main():
    s = Solution()
    print(s.NumberOf1(8))
    print(s.NumberOf1(-7))

    print(s.NumberOf1_easy(8))
    print(s.NumberOf1_easy(-7))


if __name__ == "__main__":
    main()