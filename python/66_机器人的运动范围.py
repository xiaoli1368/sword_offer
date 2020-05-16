#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def __init__(self):
        self.count = 0
        self.flag = []

    # ===== 第一次的方式 =====

    def movingCount1(self, threshold, rows, cols):
        """
        递归回溯法，存在优化空间空间
        """
        self.count = 0
        if threshold > 0 and rows > 0 and cols > 0:
            flag = [[0 for i in range(cols)] for j in range(rows)]
            self.findway(threshold, rows, cols, 0, 0, flag)
        return self.count

    def findway (self, threshold, rows, cols, i, j, flag):
        if i < 0 or i >= rows or j < 0 or j >= cols or flag[i][j] == 1:
            return
        
        if self.my_sum(i) + self.my_sum(j) > threshold:
            return
        
        flag[i][j] = 1
        self.count += 1
        
        self.findway(threshold, rows, cols, i + 1, j, flag)
        self.findway(threshold, rows, cols, i - 1, j, flag)
        self.findway(threshold, rows, cols, i, j - 1, flag)
        self.findway(threshold, rows, cols, i, j + 1, flag)
        return

    # ===== 优化版 =====

    def movingCount(self, threshold, rows, cols):
        """
        递归回溯，优化版
        只用搜索上方和右方
        """
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        
        self.count = 0
        self.flag = [[0 for i in range(cols)] for j in range(rows)]

        self.checkPath(threshold, rows, cols, 0, 0)
        return self.count

    def checkPath(self, threshold, rows, cols, i, j):
        """
        搜索函数
        """
        index = i * cols + j
        if i >= rows or j >= cols or self.flag[i][j] or self.my_sum(i) + self.my_sum(j) > threshold:
            return
        
        self.flag[i][j] = 1
        self.count += 1

        self.checkPath(threshold, rows, cols, i + 1, j)
        self.checkPath(threshold, rows, cols, i, j + 1)
        return

    # ===== 工具函数 =====

    def my_sum(self, a):
        """
        求取整数a的各个数位数字的和
        另一种求和方式为：
        tmp = list(map(int, list(str(a))))
        return sum(tmp)
        """
        ret = 0
        while a != 0:
            ret += a % 10
            a //= 10
        return ret
    
    def plot(self):
        """
        画图显示最后一次的运动范围
        """
        import matplotlib.pyplot as plt
        plt.imshow(self.flag)
        plt.show()

    def test(self, threshold, rows, cols):
        """
        测试函数
        """
        func_vec = [self.movingCount1, self.movingCount]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(threshold, rows, cols)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))
        
 
def main():
    """
    注意网格不能设置过大，否则会报递归深度错误
    maximum recursion depth exceeded while calling a Python object
    """
    s = Solution()
    s.test(2, 2, 3)
    s.test(3, 1, 0)
    s.test(0, 3, 1)
    s.test(18, 30, 30)
    s.test(10, 40, 40)

    # 画图显示最后一次的结果
    s.plot()


if __name__ == "__main__":
    main()