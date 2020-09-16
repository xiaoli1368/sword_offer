#!/bin/bash/ python3
#-*- coding:utf-8 -*-

class Solution:
    def isNumeric1(self, s):
        """
        牛客网版本，已经AC
        注意s是字符串
        """
        if s == None or len(s) == 0:
            return False
        
        e_cnt = 0
        dot_cnt = 0
        has_value = False
        
        i = 0 if s[0] != "+" and s[0] != "-" else 1
        for j in range(i, len(s)):
            if s[j] >= "0" and s[j] <= "9":
                has_value = True
            else:
                has_value = False
                if s[j] == "." and e_cnt == 0:
                    dot_cnt += 1
                elif s[j] == "e" or s[j] == "E":
                    e_cnt += 1
                elif (s[j] == "+" or s[j] == "-") and (s[j-1] == "e" or s[j-1] == "E"):
                    continue
                else:
                    return False
                
                if e_cnt >= 2 or dot_cnt >= 2:
                    return False
        
        return has_value

    def isNumeric2(self, s):
        """
        投机取巧解法
        """
        try:
            ss = float(s)
            return True
        except:
            return False

    def test(self, s):
        """
        测试函数
        """
        result1 = self.isNumeric1(s)
        result2 = self.isNumeric2(s)
        print("result1: {:d}, result2: {:d}, string: {:s}".format(result1, result1, s))


def main():
    strs = ["+100", "5e2", "-123", "3.1416", "0123",
            "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4",
            "0", " 0.1", "abc", "1 a", "2e10", " -90e3",
            " 1e", "e3", " 6e-1", " 99e2.5", "53.5e93",
            " --6", "-+3", "95a54e53"]

    s = Solution()
    for ss in strs:
        s.test(ss)


if __name__ == "__main__":
    main()