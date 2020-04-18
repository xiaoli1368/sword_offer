#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def Sum_Solution(self, n):
        """
        递归解法
        """
        tmp = n and self.Sum_Solution(n - 1)
        return n + tmp

    def Sum_Solution2(self, n):
        return sum(list(range(1, n + 1)))

    def Sum_Solution3(self, n):
        return (n**2 + n) >> 1


def main():
    s = Solution()
    print(s.Sum_Solution(10))
    print(s.Sum_Solution2(10))
    print(s.Sum_Solution3(10))


if __name__ == "__main__":
    main()