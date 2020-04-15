#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def FindNumbersWithSum(self, array, tsum):
        if array == []:
            return []

        l = 0
        h = len(array) - 1
        currSum = 0

        while l < h:
            currSum = array[l] + array[h]
            if currSum == tsum:
                return [array[l], array[h]]
            elif currSum < tsum:
                l += 1
            elif currSum > tsum:
                h -= 1

        return []


def main():
    s = Solution()
    array = [1, 2, 3, 4, 5, 6, 7]
    print(s.FindNumbersWithSum(array, 6))


if __name__ == "__main__":
    main()