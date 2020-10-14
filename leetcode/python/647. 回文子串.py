#!/bin/bash python
"""
647. 回文子串

与第5题相同，三种思路

思路一：
暴力法（会超时）

思路二：
中心匹配法

思路三：
动态规划（效果一般，不如思路二）
"""

class Solution(object):
    def countsubStrings(self, s):
        """
        暴力法
        """
        ret = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                if self.judge(s, l, r):
                    ret += 1 
        return ret
    
    def countsubStrings2(self, s):
        """
        中心拓展法
        """
        ret = 0
        for i in range(2 * len(s) - 1):
            center = i // 2
            if i % 2 == 0:
                ret += self.getLength(s, center, center)
            else:
                ret += self.getLength(s, center, center + 1)
        return ret
    
    def countsubStrings3(self, s):
        """
        动态规划
        dp[i][j]表示s[i:j+1]是否为回文子串
        """
        if s == "":
            return 0
        
        ret, n = 0, len(s)
        dp = [[False] * n for _ in range(n)] 

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i <= j and s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if i + 1 <= j - 1 else True
                if dp[i][j]:
                    ret += 1
        return ret

    # 一些工具函数

    def judge(self, s, l, r):
        """
        判断s[l:r+1]是否回文
        """
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def getLength(self, s, l, r):
        """
        获取以l,r为中心的回文串的个数
        其实得到最长回文串后处理一下即可
        """
        if s[l] != s[r]:
            return 0
        while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
            l -= 1
            r += 1
        return (r - l) // 2 + 1


if __name__ == "__main__":
    ss = "aaacccbbb"
    s = Solution()
    print(s.countsubStrings(ss))
    print(s.countsubStrings2(ss))
    print(s.countsubStrings3(ss))