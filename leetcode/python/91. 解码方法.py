#!/bin/bash python
"""
91. 解码方法

思路：
DP
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        动态规划
        dp[i]表示以索引i结尾的字符串s[:i]，解码方法总数
        a = s[i]是否合法，b = s[i-1:i]是否合法
        if a：
            dp[i] += dp[i - 1]
        if b:
            dp[i] += dp[i - 2]
        注意为了计算方便，dp[i]增加前导1，因此整体dp索引+1
        """
        if s == "":
            return 0
        dp = [1] + [0] * len(s)
        for i in range(len(s)):
            if i >= 0 and s[i] >= "1":
                dp[i + 1] += dp[i]
            if i >= 1 and s[i - 1] != "0" and s[i-1:i+1] <= "26":
                dp[i + 1] += dp[i - 1]
            if dp[i + 1] == 0:
                break
        return dp[-1]