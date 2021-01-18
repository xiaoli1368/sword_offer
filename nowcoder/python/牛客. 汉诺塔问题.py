#!/bin/bash python
"""
牛客. 汉诺塔问题

思路：
1. 主要是明确递归，最终跳出的条件，以及分解出子问题
2. 注意保存各个位置上盘子的多少其实没有意义，多此一举了
"""

# -*- coding:utf-8 -*-

class Solution:
    def getSolution(self, n):
        # write code here
        def move(ret, a, b, c, n):
            """
            借助b，将a上的n个圆盘按顺序移动到c上
            """
            # 特殊情况
            if n <= 0:
                return
            # 处理子问题，把a上的n-1个圆盘借助c移动到b
            if n > 1:
                move(ret, a, c, b, n - 1)
            # 直接移动a上仅有的一个圆盘到c
            ret.append("move from {} to {}".format(a, c))
            # 递归，把b上的n-1个圆盘借助a移动到c
            move(ret, b, a, c, n - 1)
            return
        
        ret = []
        move(ret, "left", "mid", "right", n)
        return ret

if __name__ == "__main__":
    n = 10
    s = Solution()
    ret = s.getSolution(n)
    for i in ret:
        print(i)
    print("when n = {}, all moves = {}".format(n, len(ret)))