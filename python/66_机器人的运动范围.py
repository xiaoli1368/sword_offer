#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
    
    def my_sum(self, a):
        ret = 0
        while a != 0:
            ret += a % 10
            a //= 10
        return ret
    
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
        
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold > 0 and rows > 0 and cols > 0:
            flag = [[0 for i in range(cols)] for j in range(rows)]
            self.findway(threshold, rows, cols, 0, 0, flag)
        return self.count

# 优化版，使用了多个全局变量，换一种方式求和：
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
        self.threshold = None
        self.rows = None
        self.cols = None
        self.flag = None
    
    def findway (self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or self.flag[i][j] == 1:
            return
        
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > self.threshold:
            return
        
        self.flag[i][j] = 1
        self.count += 1
        
        self.findway(i + 1, j)
        self.findway(i - 1, j)
        self.findway(i, j - 1)
        self.findway(i, j + 1)
        return
        
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold > 0 and rows > 0 and cols > 0:
            flag = [[0 for i in range(cols)] for j in range(rows)]
            self.threshold = threshold
            self.rows = rows
            self.cols = cols
            self.flag = flag
            self.findway(0, 0)
        return self.count