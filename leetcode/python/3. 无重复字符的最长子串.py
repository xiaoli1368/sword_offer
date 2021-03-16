#!/bin/bash python
"""
3. 无重复字符的最长子串

思路：
滑窗法
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑窗法
        """
        # 特殊情况
        if s == "":
            return 0
        # 滑窗，定义[l, h)为满足条件的子串
        d = dict()
        l = h = ret = 0
        while h < len(s):
            # 移动右指针
            while h < len(s) and d.get(s[h], 0) == 0:
                d[s[h]] = 1
                h += 1
            # 更新结果
            ret = max(ret, h - l)
            # 移动左指针
            while l < len(s) and h < len(s) and d[s[h]] != 0:
                d[s[l]] -= 1
                l += 1
        # 返回结果
        return max(ret, h - l)

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        滑窗法（优化版）
        定义滑窗区间为[l, h]，初始化 l = h = 0
        右指针不断移动，并且更新ret长度，直到不满足要求，此时移动左指针
        需要一个hash记录当前窗口内出现过的字符
        """
        ret, l, visited = 0, 0, set()
        for h in range(len(s)):
            if s[h] not in visited:
                ret = max(ret, h - l + 1)
            else:
                while s[h] in visited:
                    visited.remove(s[l])
                    l += 1
            visited.add(s[h])
        return ret