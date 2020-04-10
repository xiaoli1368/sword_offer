#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == [] or k > len(tinput):
            return []

        tinput.sort()
        return tinput[0:k]


def main():
    s = Solution()
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    result = s.GetLeastNumbers_Solution(tinput, 4)

    print(tinput)
    print(result)


if __name__ == "__main__":
    main()