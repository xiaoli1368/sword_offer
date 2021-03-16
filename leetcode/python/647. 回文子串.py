#!/bin/bash python
"""
647. 回文子串

思路：
1. 暴力思路：三重循环会超时
2. 中心延拓法，两重循环
3. 动态规划，需要额外空间，两重循环
"""

class Solution(object):
    def countsubStrings(self, s):
        """
        暴力法
        """
        ret = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                flag = 1
                while l < r:
                    if s[l] != s[r]:
                        flag = 0
                        break
                    l += 1
                    r -= 1
                ret += flag
        return ret
    
    # ======================================

    def getLength(self, s, l, r):
        """
        获取以l,r为中心的回文串的个数
        其实得到最长回文串后处理一下即可
        """
        if r >= len(s) or s[l] != s[r]:
            return 0
        while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
            l -= 1
            r += 1
        return (r - l) // 2 + 1
    
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
        中心拓展法（优化版）
        """
        ret = 0
        for i in range(len(s)):
            ret += self.getLength(s, i, i) + self.getLength(s, i, i + 1)
        return ret
    
    # =====================================
    
    def countsubStrings4(self, s):
        """
        动态规划
        dp[i][j]表示区间[i:j]是否为回文子串
        if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1]
        if s[i] != s[j]: dp[i][j] = False
        综上所述有：dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
        从递推方程可以看出遍历方式为：i从大到小，j从小到大
        为了保证i+1和j-1不越界，有i<n-1, j>0，因此不计算对角线上的元素，最终加上n即可
        全部初始化为True，遍历时保证i<j，如果i>j表示区间为空，True串
        """
        ret, n = 0, len(s)
        dp = [[True] * n for _ in range(n)] 
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                ret += 1 if dp[i][j] else 0
        return ret + n


if __name__ == "__main__":
    ss = "aaacccbbb"
    s = Solution()
    print(s.countsubStrings(ss))
    print(s.countsubStrings2(ss))
    print(s.countsubStrings3(ss))
    print(s.countsubStrings4(ss))