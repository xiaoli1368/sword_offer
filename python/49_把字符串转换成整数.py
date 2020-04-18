#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def StrToInt(self, s):
        """
        个人解法
        """
        if s == "":
            return 0

        sign = 1
        tsum = 0
        for i in range(0, len(s)):
            if i == 0 and s[i] == "-":
                sign = -1
                continue
            if i == 0 and s[i] == "+":
                continue
            if s[i] < "0" or s[i] > "9":
                return 0
            tsum  = tsum * 10 + ord(s[i]) - ord("0")
        tsum *= sign

        if tsum >= 2**15 or tsum < -2**15:
            return 0
        else:
            return tsum
        
def main():
    s = Solution()
    print(s.StrToInt("-217483649"))
    print(s.StrToInt("+456"))
    print(s.StrToInt("-123"))


if __name__ == "__main__":
    main()