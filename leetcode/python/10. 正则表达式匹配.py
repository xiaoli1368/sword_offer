#!/bin/bash python
"""
10. 正则表达式匹配

思路：
递归或者动态规划
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
           ""  c  *  a  *  b
        ""  1  0  1  0  1  0
        a   0  0  0  1  1  0
        a   0  0  0  0  1  0
        b   0  0  0  0  0  1
        二维dp，使用s来匹配p
        初始化，[0, 0]位置为1，第一列为0，第一行只有当前为*时有 dp[i][j] = dp[i][j - 2]
        dp[i][j] = dp[i - 1][j - 1], if p[j] == "." 使用.相等或者严格字符相等
        dp[i][j] = dp[i][j - 2], if p[j] == "*" 选取出现0次
                   dp[i][j - 1], if p[j] == "*" 选取出现1次
                   (s[i]与p[j - 1]匹配) and dp[i - 1][j], if p[j] == "*" 选取出现多次
        注意题干中防止了出现**的情况
		可以再优化优化，但是这个版本是最好理解的（因为按部就班来写的）
        """
        row, col = len(s), len(p)
        dp = [[False] * (col + 1) for _ in range(row + 1)]
        for i in range(row + 1):
            for j in range(col + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif j == 0: # 第一列
                    dp[i][j] = False 
                elif i == 0: # 第一行
                    if p[j - 1] == "*":
                        dp[i][j] = dp[i][j - 2]
                else: # 非第一行第一列
                    if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == "*":
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or ((s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j])
        return dp[row][col]

    # ===== 优化版 =====
    def match(self, a, b):
        """
        判断a与b是否可以匹配，包括严格匹配或者.匹配，不包含*匹配
        """
        return b == "." or a == b

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
		优化版
		dp[i][j]最终只能从4个地方取到
		dp[i][j] = dp[i - 1][j - 1], if s[i]与p[j]匹配，包括严格匹配和.匹配
		dp[i][j] = dp[i][j - 2], if p[j]为*，且s[i]和p[j-1]无法匹配，包括严格匹配和.匹配
		dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j], if p[j]为*，且可以s[i]和p[j-1]可以匹配，包括严格匹配和.匹配
        """
        row, col = len(s), len(p)
        dp = [[False] * (col + 1) for _ in range(row + 1)]
        for j in range(col + 1):
            if j == 0:
                dp[0][0] = True
            elif p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if self.match(s[i - 1], p[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*" and not self.match(s[i - 1], p[j - 2]):
                    dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == "*" and self.match(s[i - 1], p[j - 2]):
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j]
        return dp[row][col]