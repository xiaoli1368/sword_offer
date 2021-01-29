#!/bin/bash python
"""
76. 最小覆盖子串

思路：
滑窗法
这道题较难，需要考虑缩窗时候的策略
1. 如果正常缩窗减少一个字符，则无法得到最短的窗口，因为存在非目标字符占位
2. 如果每次缩窗到减少一个目标字符，且变为不匹配，则需要考虑最优解位于最右端的特殊情况
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
		来自labuladong的参考解
        """
        start = 0
        minLen = float("+inf")
        left = right = valid = 0

        window = dict()
        need = dict()
        for i in t:
            need[i] = 1 + need.get(i, 0)

        while right < len(s):
            char = s[right]
            right += 1
            if need.get(char):
                window[char] = 1 + window.get(char, 0)
                if need[char] == window[char]:
                    valid += 1
            
            while valid == len(need):
                if right - left < minLen:
                    minLen = right - left
                    start = left
                char = s[left]
                left += 1
                if need.get(char):
                    if need[char] == window[char]:
                        valid -= 1
                    window[char] -= 1

        return "" if minLen == float("+inf") else s[start:start+minLen]

    def minWindow(self, s: str, t: str) -> str:
        """
		错解，每次只缩减一个字符，不能保证获取最短的滑窗
        """
        # 特殊情况
        if s == "" or t == "":
            return ""
        
        # 初始化
        d = dict()
        for char in t:
            d[char] = 1 + d.get(char, 0)
        n, cnt = len(s), len(d)
        
        # 滑窗法
        l = h = 0
        ll, hh = 0, n + 1
        while h < n:
            # 移动右指针，直到完成匹配
            while h < n and cnt > 0:
                if s[h] in d:
                    d[s[h]] -= 1
                    if d[s[h]] == 0:
                        cnt -= 1
                h += 1
            # 更新结果
            if cnt == 0 and h - l < hh - ll:
                ll, hh = l, h
            # 移动左指针，减少一个字符
            if s[l] in d:
                d[s[l]] += 1
                if d[s[l]] == 1:
                    cnt += 1
            l += 1
        
        # 返回结果
        return s[ll:hh] if hh <= n else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        正解，缩窗需要使用循环，且需要考虑末尾的特殊情况
        1. 滑窗法：[l, h)表示当前的窗口
        2. 统计量：cnt表示当前窗口还需匹配字符的个数
                  d表示当前窗口内每个字符还需要匹配的个数
        """
        # 特殊情况
        if s == "" or t == "":
            return ""
        
        # 初始化
        d = dict()
        for char in t:
            d[char] = 1 + d.get(char, 0)
        n, cnt = len(s), len(d)
        
        # 滑窗法
        l = h = 0
        ll, hh = 0, n + 1
        while h < n:
            # 移动右指针，直到完成匹配
            while h < n and cnt > 0:
                if s[h] in d:
                    d[s[h]] -= 1
                    if d[s[h]] == 0:
                        cnt -= 1
                h += 1
            # 更新结果
            if cnt == 0 and h - l < hh - ll:
                ll, hh = l, h
            # 移动左指针，直到不匹配且当前字符在目标范围内
            while l < h and (cnt == 0 or s[l] not in d):
                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] == 1:
                        cnt += 1
                l += 1
                if cnt == 0 and h - l < hh - ll: # 处理末尾特殊情况
                    ll, hh = l, h
        
        # 返回结果
        return s[ll:hh] if hh <= n else ""

    def minWindow(self, s: str, t: str) -> str:
        """
        优化版
        1. 滑窗法：[l, h)表示当前的窗口
        2. 统计量：cnt表示当前窗口还需匹配字符的个数
                  d表示当前窗口内每个字符还需要匹配的个数
        """
        # 特殊情况
        if s == "" or t == "":
            return ""
        
        # 初始化
        d = dict()
        for char in t:
            d[char] = 1 + d.get(char, 0)
        n, cnt = len(s), len(d)
        
        # 滑窗法
        l = h = 0
        ll, hh = 0, n + 1
        while h < n:
            # 移动右指针，直到完成匹配
            while h < n and cnt > 0:
                if s[h] in d:
                    d[s[h]] -= 1
                    if d[s[h]] == 0:
                        cnt -= 1
                h += 1
            # 移动左指针，直到不匹配且当前字符在目标范围内
            # 同时在内部先更新结果
            while l < h and (cnt == 0 or s[l] not in d):
                if cnt == 0 and h - l < hh - ll:
                    ll, hh = l, h
                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] == 1:
                        cnt += 1
                l += 1
        
        # 返回结果
        return s[ll:hh] if hh <= n else ""