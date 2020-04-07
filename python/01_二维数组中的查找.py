#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():

    def Find(self, target, array):
        """
        这一版比较低级
        """
        i = 0
        j = 0
        dire = 0
        ilen = len(array)
        jlen = len(array[0])
        while (i < ilen and j < jlen and i >= 0 and j >= 0):
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

    def Find2(self, target, array):
        i = 0
        j = len(array[0]) - 1
        while (i <= len(array) and j >= 0):
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1
        return False


def main():
    target = 26
    array = [[1,  4,   7, 11, 15],
             [2,  5,   8, 12, 19],
             [3,  6,   9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]]
    s = Solution()
    print(s.Find(target, array))
    print(s.Find2(target, array))


if __name__ == "__main__":
    main()
