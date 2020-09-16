#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        第一次的方式，递归回溯
        matrix: 一维字符串
        path: 一维字符串
        """
        if not matrix or not path or rows <= 0 or cols <= 0:
            return False
        
        matrix = list(matrix)        # 原来是一维字符串
        flag = [False] * rows * cols # 表示全都没有遍历过
        
        for i in range(rows):
            for j in range(cols):
                if self.checkPath(matrix, rows, cols, i, j, path, 0, flag):
                    return True
        
        return False
    
    def checkPath(self, matrix, rows, cols, i, j, path, k, flag):
        index = i * cols + j
        
        if i < 0 or i >= rows or j < 0 or j >= cols or k >= len(path) or matrix[index] != path[k] or flag[index] == True:
            return False
        
        if k == len(path) - 1:
            return True
        
        flag[index] = True
        
        if self.checkPath(matrix, rows, cols, i - 1, j, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i + 1, j, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i, j - 1, path, k + 1, flag) or \
           self.checkPath(matrix, rows, cols, i, j + 1, path, k + 1, flag):
            return True
        
        flag[index] = False
        return False

    def test(self, matrix, rows, cols, path):
        """
        测试函数
        """
        print("=====")
        start = time.time()
        result = self.hasPath(matrix, rows, cols, path)
        end = time.time()
        print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    matrix = "aa"
    path = "aaa"

    matrix2 = "ABCESFCSADEE";
    path2 = "ABCCED"

    matrix3 = "abcd"
    path3 = "abcd"

    matrix4 = "abcesfcsadee"
    path4 = "fcsecbasadee"

    s = Solution()
    s.test(matrix, 1, 2, path)
    s.test(matrix2, 3, 4, path2)
    s.test(matrix3, 2, 2, path3)
    s.test(matrix4, 3, 4, path4)


if __name__ == "__main__":
    main()