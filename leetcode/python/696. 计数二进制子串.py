#!/bin/bash python
"""
696. 计数二进制子串

思路：
1. 暴力动态规划，O(n^2) + O(n^2)，超时了
2. 类似回文串中心延拓法，O(n^2)但是有剪枝，AC了
3. 最优解，一次遍历统计法，统计索引i之前，与s[i]相同的字符长度same，与s[i]不同的字符长度diff
   如果 diff >= same, 则会贡献1个满足要求的子串
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        动态规划
        dp[i][j]表示区间[i:j]是否为满足要求的子串
        if (j - i + 1) % 2 == 1: False 奇数长度必然不满足要求
        if i + 1 == j: dp[i][j] = s[i] != s[j]
        if i + 1 >= j - 1: dp[i][j] = dp[i+1][j-1] and dp[i] == dp[i+1] and dp[j] == dp[j-1]
        遍历方式：i从大到小，j从小到大，i < j
        """
        cnt, n = 0, len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 2):
                if i + 1 == j:
                    dp[i][j] = s[i] != s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[i+1] and s[j] == s[j-1]
                cnt += 1 if dp[i][j] else 0
        return cnt

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        中心延拓法
        选定[i,i+1]，当这两个元素不相等时（01或者10），开始中心延拓
        保证左侧s[i-1]等于s[i]，保证右侧s[i+1]等于s[i+2]
        """
        cnt, n = 0, len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                l, h, cnt = i, i + 1, cnt + 1
                while l >= 1 and h <= n - 2 and s[l] == s[l - 1] and s[h] == s[h + 1]:
                    l -= 1
                    h += 1
                    cnt += 1
        return cnt

    def countBinarySubstrings(self, s: str) -> int:
        """
        一次遍历统计法
        统计索引i之前，与s[i]相同的字符长度same，与s[i]不同的字符长度diff
        如果 diff >= same, 则会贡献了1个满足要求的子串
        """
        cnt, same, diff = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                same += 1
            else:
                diff = same
                same = 1
            if diff >= same:
                cnt += 1
        return cnt