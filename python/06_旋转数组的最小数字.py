#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def minNumberInRotateArray(self, array):
        if array == []:
            return 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return array[i + 1]
        return array[0]

    def minNumber(self, array, low, high):
        """
        输入一个数组，返回最小值
        """
        tmp = array[low]
        while low <= high:
            if array[low] < tmp:
                tmp = array[low]
            low += 1
        return tmp

    def minNumberInRotateArray2(self, array):
        length = len(array)
        if length == 0:
            return 0
        
        low = 0
        high = length - 1
        while low < high:
            middle = (low + high) // 2
            if array[low] == array[middle] and array[middle] == array[high]:
                return self.minNumber(array, low, high)
            elif array[middle] >= array[high]:
                low = middle + 1
            else:
                high = middle
        return array[low]


def main():
    s = Solution()
    array = [3, 4, 5, 1, 2]
    array = [1, 1, 1, 0, 1]
    print(s.minNumberInRotateArray(array))
    print(s.minNumberInRotateArray2(array))


if __name__ == "__main__":
    main()