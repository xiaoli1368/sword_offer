#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def PrintMinNumber(self, numbers):
        """
        把数组排成最小的数
        """
        if numbers == []:
            return ""

        length = len(numbers)
        num = [str(x) for x in numbers]

        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if num[i] + num[j] > num[j] + num[i]: 
                    num[i], num[j] = num[j], num[i]

        return "".join(num)
        

def main():
    s = Solution()
    numbers = [3, 32, 321]

    print(numbers)
    print(s.PrintMinNumber(numbers))


if __name__ == "__main__":
    main()