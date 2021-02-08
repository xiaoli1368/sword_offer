#!/bin/bash python
"""
784. 字母大小写全排列

思路：
DFS
"""

class Solution(object):
    def judge(self, char):
        """
        判断当前字符是否为字母
        """
        return "a" <= char <= "z" or "A" <= char <= "Z"
    
    def change(self, s, i):
        """
        改变s[i]的大小写
        """
        diff = ord("a") - ord("A")
        if "a" <= s[i] <= "z":
            s[i] = chr(ord(s[i]) - diff)
        elif "A" <= s[i] <= "Z":
            s[i] = chr(ord(s[i]) + diff)
        return
    
    def dfs(self, ss, ret, i):
        """
        dfs
        """
        # 越界
        if i >= len(ss):
            ret.append("".join(ss))
            return
        # 数字跳过，或者字母不改跳过
        self.dfs(ss, ret, i + 1)
        # 字母修改后进入下一层
        if self.judge(ss[i]):
            self.change(ss, i)
            self.dfs(ss, ret, i + 1)
            self.change(ss, i)
        return

    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        if s == "":
            return []
        ret, ss = [], list(s)
        self.dfs(ss, ret, 0)
        return ret