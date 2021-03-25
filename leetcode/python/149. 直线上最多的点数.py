#!/bin/bash python
"""
149. 直线上最多的点数

思路：
hash，这题挺有意思的，有点工程题目的意思了
参考链接：https://leetcode-cn.com/problems/max-points-on-a-line/solution/zhi-jie-fa-bu-kao-lu-xie-lu-bu-cun-zai-d-6tho/
"""

class Solution(object):
    def getGCD(self, a, b):
        """
        获取两个正数的最大公约数
        """
        if b == 0:
            return a
        else:
            return self.getGCD(b, a % b)

    def getHash(self, p1, p2):
        """
        p1 = (x1, y1), p2 = (x2, y2)
        (y - y1) * (x1 - x2) = (x - x1) * (y1 - y2)
        (x1-x2)*y + (y2-y1)*x + x1*(y1-y2)+y1*(x2-x1) = 0
        (y1-y2)*x + (x2-x1)*y + (x1y2 - x2y1) = 0
        由两点确定一条直线的hash
        返回(A, B)
        """
        x1, y1 = p1
        x2, y2 = p2
        A, B = y1 - y2, x2 - x1
        if A == 0:
            B = 1
        if B == 0:
            A = 1
        if abs(A) > 1 and abs(B) > 1: # 只有在二者都非0/1的时候才约分
            gcd = self.getGCD(abs(A), abs(B))
            A //= gcd
            B //= gcd
        return (A, B) if A >= 0 else (-A, -B)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        1. 暴力方法：二重循环，遍历所有的两点组合，得到所有的直线hash
                    然后一重循环，将所有的点分配到直线key中，进行计数
        2. 高效方法：在进行二重循环的时候，存在不同的点组合映射到了一条直线上
                    例如一条直线上仅有3个点，但是在二重循环遍历的时候，会有3个两点组合
                    因此在二重循环的时候，就对当前直线key的次数进行计数，得到的是C(n, 2)
                    最终由C(n, 2)反解出n来即可。
                    如何对一条直线进行hash映射？y = kx + b，存在无穷斜率的情况
                    Ax + By + C = 0，则需要归一化，否则参数不唯一，因为可以等比例放缩
        3. 存在问题：直线hash中涉及除法，得到的浮点数并不准确，由此可能导致误差
                    因此line的hash不唯一
        ======================================
        4. 暴力解法：三重循环O(n^3)，遍历两个点确定一条直线，然后判断第3点是否在直线上
        5. 优化方法：设计一个hash，可以用来记录直线方程，优化复杂度到O(n^2)
                    外层遍历固定第一个点，内层遍历确定第二个点，同时两点确定斜率
                    判断有多少个点具备相同的斜率，斜率的表示方法，Ax + By + C
                    其中A为正数，AB为最约分正整数
        """
        if points == []:
            return 0
        ret, n, d = 1, len(points), dict()
        for i in range(n):
            d.clear()
            for j in range(i + 1, n):
                key = self.getHash(points[i], points[j])
                d[key] = 1 + d.get(key, 1)
                ret = max(ret, d[key])
        return ret