#!/bin/bash python
"""
140. 单词拆分 II

思路：
DFS回溯法
普通的回溯会超时，需要增加记忆化搜索
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s == "" or wordDict == []:
            return []

        # 回溯法
        def backTracking(ret, path, notok, s, wordDict, i):
            """
            i表示之前的单词都满足，从第i位开始搜索
            notok，记录此处不通的位置
            返回值表示是否可以完成表示
            """
            if i == len(s):
                ret.append(" ".join(path[:]))
                return True
            for j in range(i, len(s)):
                if j not in notok and s[i:j+1] in wordDict:
                    path.append(s[i:j+1])
                    if not backTracking(ret, path, notok, s, wordDict, j + 1):
                        notok.append(j + 1)
                    path.pop()
            return True

        ret = []
        path = []
        notok = []
        backTracking(ret, path, notok, s, wordDict, 0)
        return ret

    # ===== 普通DFS优化版（还是超时了） =====
    # 测试用例：
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        DFS回溯法
        对wordDict遍历
        """
        def dfs(ret, path, s, wordDict, i):
            if i >= len(s):
                ret.append(" ".join(path))
                return
            for word in wordDict:
                j = i + len(word)
                if j <= len(s) and s[i:j] == word:
                    path.append(word)
                    dfs(ret, path, s, wordDict, j)
                    path.pop()
            return
        # ===============================
        # 特殊情况
        if s == "" or wordDict == []:
            return []
        ret, path, pos = [], [], set()
        dfs(ret, path, pos, s, wordDict, 0)
        return ret

    # ===== 记忆化DFS（AC）=====
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        DFS回溯法
        返回是否可以到达终点
        记忆化搜索，增加无解的点
        """
        def dfs(ret, path, pos, s, wordDict, i):
            found = False
            if i >= len(s):
                ret.append(" ".join(path))
                return True
            for word in wordDict:
                j = i + len(word)
                if j <= len(s) and j not in pos and s[i:j] == word:
                    path.append(word)
                    if dfs(ret, path, pos, s, wordDict, j):
                        found = True
                    path.pop()
            if not found:
                pos.add(i)
            return found
        # ===============================
        # 特殊情况
        if s == "" or wordDict == []:
            return []
        ret, path, pos = [], [], set()
        dfs(ret, path, pos, s, wordDict, 0)
        return ret