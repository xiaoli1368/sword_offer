#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def StrToInt(self, s):
        """
        个人解法，考虑int32溢出
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

        if tsum >= 2**31 or tsum < -2**31:
            return 0
        else:
            return tsum
    
    def test(self, s):
        """
        测试函数
        """
        start = time.time()
        result = self.StrToInt(s)
        end = time.time()
        print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))

        
def main():
    strs = ["-123",
            "+456",
            "54354",
            "-2147483649",
            "-2147483648",
            "+2147483647",
            "+2147483648"]

    s = Solution()
    for ss in strs:
        s.test(ss)


if __name__ == "__main__":
    main()