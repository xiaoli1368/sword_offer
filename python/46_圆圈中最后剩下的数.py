#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def LastRemaining_Solution(self, n, m):
        """
        数组遍历方法
        """
        if n <= 0 or m <= 0:
            return -1

        sign = [0] * n
        count = n
        i = -1
        step = 0

        while count >= 1:
            # i = 0 if i + 1 >= n else i + 1
            i = (i + 1) % n
            if sign[i] == 1:
                continue
            else:
                step += 1
                if step == m:
                    sign[i] = 1
                    step = 0
                    count -= 1
        
        return i 

    def LastRemaining_Solution2(self, n, m):
        """
        公式法
        """
        if n <= 0 or m <= 0:
            return -1
        
        tsum = 0
        for i in range(2, n + 1):
            tsum = (tsum + m) % i

        return tsum

    def LastRemaining_Solution3(self, n, m):
        """
        递归法
        """
        if n <= 0 or m <= 0:
            return -1
        
        if n == 1:
            return 0

        return (self.LastRemaining_Solution3(n - 1, m) + m) % n


def main():
    s = Solution()
    print(s.LastRemaining_Solution(10, 4))
    print(s.LastRemaining_Solution2(10, 4))
    print(s.LastRemaining_Solution3(10, 4))


if __name__ == "__main__":
    main()