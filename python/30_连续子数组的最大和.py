#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return 0

        length = len(array)
        if length == 1:
            return array[0]

        curr_sum = array[0]
        curr_max = array[0]

        for i in range(1, length):
            if curr_sum >= 0:
                curr_sum += array[i]
            else:
                curr_sum = array[i]

            if curr_sum > curr_max:
                curr_max = curr_sum

        return curr_max


def main():
    s = Solution()
    array = [6, -3, -2, 7, -15, 1, 2, 2]
    result = s.FindGreatestSumOfSubArray(array)

    print(array)
    print(result)


if __name__ == "__main__":
    main()