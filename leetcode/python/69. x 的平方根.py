#!/bin/bash python
"""
69. x 的平方根

思路：
1. 常规二分
2. 牛顿法
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        m是满足 m^2 <= x 的最大整数
        """
        if x <= 0:
            return 0
        
        l, h = 0, x
        while l < h:
            m = (l + h + 1) // 2
            if m**2 > x:
                h = m - 1
            elif m**2 <= x:
                l = m
        return l

    def mySqrt(self, b: int) -> int:
        """
        一阶梯度下降
        损失函数: f(x) = (x^2-b)^2，加平方表示距离
        一阶梯度: f'(x) = 2*(x^2-b)*2x = x*(x^2-b)
        起始：x = b
        参数：alpha = 9e-5
        更新：x = x - alpha * f'(x)

        二阶牛顿法
         损失函数: f(x) = (x^2-b)^2，加平方表示距离
        一阶梯度: f'(x) = 2*(x^2-b)*2x = 4*x*(x^2-b)
        二阶梯度：f''(x) = 4*(1*(x^2-b) + x*(2*x)) = 4*(3*x^2 - b) = 12*x^2 -4*b
        起始：x = b
        更新：x = x - f'(x)/f''(x)

        """
        # 梯度下降，如果终止循环是个问题
        """
        x = b
        alpha = 9e-5
        for i in range(300):
            x = x - alpha * x * (x**2 - b)
        return x
        """
        # 牛顿法
        """
        x = b
        for i in range(100):
            x = x - 4*x*(x**2 - b)/(12*x**2 - 4*b)
            print(x)
        return x
        """
        # 正向迭代的牛顿法
        x = b
        while x**2 > b:
            x = (x + b // x) // 2
        return x