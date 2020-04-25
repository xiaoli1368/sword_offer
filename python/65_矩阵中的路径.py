#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path or rows <= 0 or cols <= 0:
            return False
        
        matrix = list(matrix)        # 原来是一维字符串
        flag = [False] * rows * cols # 表示全都没有遍历过
        
        for i in range(rows):
            for j in range(cols):
                if self.haha(matrix, rows, cols, i, j, path, 0, flag):
                    return True
        
        return False
    
    def haha(self, matrix, rows, cols, i, j, path, k, flag):
        index = i * cols + j
        
        if i < 0 or i >= rows or j < 0 or j >= cols or k >= len(path) or matrix[index] != path[k] or flag[index] == True:
            return False
        
        if k == len(path) - 1:
            return True
        
        flag[index] = True
        
        if self.haha(matrix, rows, cols, i - 1, j, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i + 1, j, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i, j - 1, path, k + 1, flag) or \
           self.haha(matrix, rows, cols, i, j + 1, path, k + 1, flag):
            return True
        
        flag[index] = False
        return False