#!/bin/bash python
"""
567. 字符串的排列

思路：
滑窗+hash
注意匹配的方式，可以借助数据结构，这样编码方便一些
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
		暴力滑窗法，这个方法中关于匹配的方式比较麻烦
        """
        left = right = valid = 0
        need = dict()
        window = dict()
        for i in s1:
            need[i] = 1 + need.get(i, 0)
        
        while right < len(s2):
            c = s2[right]
            right += 1
            if need.get(c, None):
                window[c] = 1 + window.get(c, 0)
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                else:
                    d = s2[left]
                    left += 1
                    if need.get(d, None):
                        if window[d] == need[d]:
                            valid -= 1
                        window[d] -= 1

        return False
	
	# ===== 高效的方式 =====
	def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        注意到必须是子串，也就是连续的
        1. 先统计s1的hash
        2. 然后判断什么时候完全匹配：所有hash完全匹配上
        3. 如何遍历所有情况：暴力枚举，滑窗
        并且可以发现窗口应该是固定长度的
        这里可以取巧，直接使用dict相等来判断匹配
        """
        if s1 == "":
            return True
        if s2 == "":
            return False
        
        # 初始化
        table = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        d1 = dict.fromkeys(table, 0)
        d2 = dict.fromkeys(table, 0)
        for char in s1:
            d1[char] += 1

        # 双指针滑窗
        n1, n2 = len(s1), len(s2)
        for h in range(n2):
            d2[s2[h]] += 1
            if h >= n1:
                d2[s2[h - n1]] -= 1
            if d1 == d2:
                return True
        return False
