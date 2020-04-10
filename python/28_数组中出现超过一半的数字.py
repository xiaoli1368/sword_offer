#!/bin/bash python3 
#-*- coding:utf-8 -*-

class Solution():
    def MoreThanHalfNum_Solution(self, number):
        number.sort()

        length = len(number)
        first = 0
        end = first + length // 2

        while end < length:
            if number[first] == number[end]:
                return number[first]

            first += 1
            end += 1
        
        return 0


def main():
    s = Solution()
    number = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    result = s.MoreThanHalfNum_Solution(number)

    print(number)
    print(result)


if __name__ == "__main__":
    main()