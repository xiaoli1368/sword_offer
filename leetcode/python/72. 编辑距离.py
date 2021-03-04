#/bin/bash python
"""
72. 编辑距离

思路：
动态规划
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划
        dp[i][j] = dp[i-1][j-1], if word1[i] == word2[j]
        dp[i][j] = 1 + dp[i-1][j], 1 + dp[i][j-1], 1 + dp[i-1][j-1]
                   把当前删除       在当前后边插入    把当前字符替换
                 = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        将horse转换为ros
            ""  h  o  r  s  e
        ""  0   1  2  3  4  5
        r   1   1  2  2  3  4
        o   2   2  1  2  3  4
        s   3   3  2  3  2  3
        """
        col, row = len(word1), len(word2)
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row + 1):
            for j in range(col + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = 1 + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = 1 + dp[i - 1][j]
                elif word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]

    def minDistance(self, p, q):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        二维dp解决编辑距离，优化版
        """
        dp = [[0] * (len(q) + 1) for _ in range(len(p) + 1)]
        for i in range(len(p) + 1):
            for j in range(len(q) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    d = 0 if p[i - 1] == q[j - 1] else 1
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + d)
        return dp[-1][-1]