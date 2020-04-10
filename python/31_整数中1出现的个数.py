#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def NumberOf1Between1AndN_Solution(self, n):
        """
        暴力求解
        """
        return "".join(map(str, range(n + 1))).count("1")

    def NumberOf1Between1AndN_Solution2(self, n):
        cnt = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            cnt += (a + 8) // 10 * m + (b + 1 if a % 10 == 1 else 0)
            m *= 10
        return cnt


def main():
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(12345))
    print(s.NumberOf1Between1AndN_Solution2(12345))



if __name__ == "__main__":
    main()