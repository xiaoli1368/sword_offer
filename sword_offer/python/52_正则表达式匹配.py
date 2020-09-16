#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def match1(self, s, pattern):
        """
        第一次的解法，递归
        s, pattern都是字符串
        """
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) == 0:
            return False
        elif len(s) == 0  and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match1(s, pattern[2:])
            else:
                return False
        else: # 二者都非空
            if len(pattern) == 1 or pattern[1] != "*": # 后一位不是 *
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match1(s[1:], pattern[1:])
                else:
                    return False
            else: # 后一位是 *
                if s[0] != pattern[0] and pattern[0] != ".":
                    return self.match1(s, pattern[2:])
                else:
                    return self.match1(s[1:], pattern) or self.match1(s, pattern[2:])

    # 递归回溯法
    def match2(self, s, pattern):
        """
        递归回溯法，优化版
        """
        if len(pattern) == 0:
            return len(s) == 0
        
        # 此时pattern非空
        first_match = False
        if len(s) != 0 and (s[0] == pattern[0] or pattern[0] == "."):
            first_match = True
        
        # 此时pattern长度为1或者后一个元素不是"*"
        if len(pattern) == 1 or pattern[1] != "*":
            return first_match and self.match2(s[1:], pattern[1:])
        else: # 此时pattern后一个元素为"*"
            return self.match2(s, pattern[2:]) or (first_match and self.match2(s[1:], pattern))
    
    def match3(self, s, p):
        """
        动态规划版本
        注意错误的二维list赋值方式，浅拷贝引用：
        dp = [[False] * (n + 1)] * (m + 1)
        """
        if p == "":
            return s == ""
        
        m = len(s)
        n = len(p)
        
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        if m != 0 and (p[0] == "." or p[0] == s[0]):
            dp[1][1] = True
        if p[0] == "*":
            dp[0][1] = True
        for i in range(n):
            if p[i] == "*" and dp[0][i - 1] == True:
                dp[0][i + 1] = True

        for i in range(m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == "*":
                    if s[i] != p[j - 1] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j - 1])
        
        return dp[m][n]

    def test(self, s, p):
        """
        测试函数
        """
        fun_vec = [self.match1, self.match2, self.match3]
        print("=====")
        for func in fun_vec:
            start = time.time()
            result = func(s, p)
            end = time.time()
            print("time(us): {:>5.2f}, result: {:d}, str: {}, pat: {}".format((end - start)*10**6,
                                                                               result, s, p))

def main():
    data = [("aaa", "a*a"),
            ("bbb", "aaa"),
            ("aaa", "a*"),
            ("aab", "c*a*b"),
            ("mississippi", "mis*is*p*."),
            ("asjkldf", ".*"),
            ("aaa", "*")]
    
    s = Solution()
    for i in data:
        s.test(i[0], i[1])
    

if __name__ == "__main__":
    main()