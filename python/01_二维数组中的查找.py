#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def Find1(self, target, array):
        """
        暴力枚举
        """
        if array == []:
            return False
        
        for i in array:
            for j in i:
                if target == j:
                    return True
        return False

    def Find2(self, target, array):
        """
        高效一些的暴力枚举
        """
        if array == []:
            return False
        
        for i in array:
            if target in i:
                return True
        return False

    def Find3(self, target, array):
        """
        第一次解法，从左上角开始查找的低级思路
        从左上角开始查找，相等则退出
        更大时则优先向右移动，遇到边界开始向下移（使用flag记录比较的方向，向右还是向下）
        变小时向下移动
        如果是连续两次都是变小，此时根据flag则应进行左移动
        """
        i = 0
        j = 0
        dire = 0
        ilen = len(array)
        jlen = len(array[0])
        while i < ilen and j < jlen and i >= 0 and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j] and j + 1 < jlen:
                j += 1
                dire = 0
            elif target > array[i][j] and j + 1 >= jlen:
                i += 1
                dire = 1
            elif target < array[i][j] and dire == 0:
                i += 1
                j -= 1
                dire = 1
            elif target < array[i][j] and dire == 1:
                j -= 1
        return False

    def Find4(self, target, array):
        """
        从左下角开始查找的方式
        """
        i = len(array) - 1
        j = 0
        while j < len(array[0]) and i >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                i -= 1
            else:
                j += 1
        return False

    def Find(self, target, array):
        """
        最终优化版，从右上开始查找
        """
        i = 0
        j = len(array[0]) - 1
        while i < len(array) and j >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1
        return False

    def test(self, target, array):
        """
        测试函数
        """
        func_vec = [self.Find1, self.Find2, self.Find3, self.Find4, self.Find]
        for func in func_vec:
            # 这里可以直接使用引用
            start = time.time()
            result = func(target, array)
            end = time.time()

            print("result: {}, time: {}".format(result, end - start))


def main():
    target = 26
    array = [[1,  4,   7, 11, 15],
             [2,  5,   8, 12, 19],
             [3,  6,   9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]]

    s = Solution()
    s.test(target, array)
    print("==========")
    s.test(29, array)


if __name__ == "__main__":
    main()