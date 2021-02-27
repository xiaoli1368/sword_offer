#!/bin/bash python
"""
1771. 由子序列构造的最长回文串的长度

思路：
可以理解为：
1. 先把word1和word2拼接得到完整的字符串
2. 然后找到最长的回文子序列

三重循环：
1. 遍历长度，由length到1，找到满足要求结果则终止
2. 遍历回文子序列的中心，从0到length-1，注意可以根据左右两侧是否越界，提前终止
3. 中心延拓法，判断是否为回文子序列，注意到当不等的时候，存在越过的空间（复杂度很大）
	(1) 保留左侧
	(2) 保留右侧
	(3) 两个都跳过

递归/动态规划：
1. 两端相同：lps(0, n-1) = 2 + lps(1, n-2)
2. 两端不同：lps(0, n-1) = max(lps(1, n-1), lps(0, n-2))
优化空间：
从底向上进行dp，注意必须保证从两个子串中提取的是非空子序列，因此需要增加额外的判断
dp[i][j]表示目标字符串中区间[i, j]可以得到的回文子序列的最大长度，两端闭区间，i <= j
最终要求的是dp[0][n-1]，所以是倒三角遍历，dp[i][j]依赖于dp[i+1][j-1]
因此i从大往小遍历，j从小往大遍历
"""

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        这道题目的基础是516.最长回文子序列
        需要注意的是保证从两个str中选出的非空子序列
        最终的结果未必在dp[0][n-1]中获取，需要max获取
        """
        if word1 == "" or word2 == "":
            return 0
        
        ret = 0
        s = word1 + word2
        n1, n = len(word1), len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # 更新dp
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    # 只有此时才可以更新ret
                    if i < n1 <= j:
                        ret = max(ret, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return ret