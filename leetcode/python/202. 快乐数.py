#!/bin/bash python
"""
202. 快乐数

两种方法：哈希表，双指针
"""

class Solution(object):
    def getSum(self, n):
        """
        获取n各个数位元素的平方和
        """
        return sum([int(x)**2 for x in str(n)])

    def isHappy1(self, n):
        """
        哈希法
        """
        s = set()
        while True:
            tmp = self.getSum(n)
            if tmp == 1:
                return True
            elif tmp in s:
                return False
            else:
                s.add(tmp)
                n = tmp

    def isHappy2(self, n):
        """
        双指针破解循环出现
        """
        p = q = n
        while True:
            p = self.getSum(p)
            q = self.getSum(self.getSum(q))
            if p == 1 or q == 1:
                return True
            elif p == q:
                return False