#!/bin/bash python
"""
139. 单词拆分

思路：
DP，当前也可以DFS
对于DP，存在两种遍历方式
内部在s上遍历，外部会使用额外的hash，时间复杂度上未必优势（只有在s很短，wordDict很多时才有优势）
内部在wordDict上遍历，除了上述特殊情况，整体具备优势
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        先建立hash，方便快速查找
        dp[i]表示以s[i]为结尾的字符串能否拆分表示
        dp[i] = dp[i] or (dp[j] and s[j:i] in wordDict)
        为了方便，dp增加前导True
        """
        # 特殊情况
        if s == "" or wordDict == []:
            return False
        
        # 初始化
        wdict = set(wordDict)
        dp = [True] + [False] * len(s)

        # 动态规划
        for i in range(len(s)):
            for j in range(i + 1):
                if dp[j] and s[j:i+1] in wdict:
                    dp[i + 1] = True
                    break
        return dp[-1]

    # ===== 另一种遍历方式（非常高效） =====
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
		内部直接对wordDict遍历
        """
        # 特殊情况
        if s == "" or wordDict == []:
            return False
        
        # 初始化
        dp = [True] + [False] * len(s)

        # 动态规划
        for i in range(len(s)):
            for word in wordDict:
                j = i + 1 - len(word)
                if j >= 0 and dp[j] and s[j:i+1] == word:
                    dp[i + 1] = True
                    break
        return dp[-1]