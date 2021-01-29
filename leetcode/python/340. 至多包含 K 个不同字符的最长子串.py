#!/bin/bash python
"""
340. 至多包含 K 个不同字符的最长子串

题目要求：
给定一个字符串s，找出至多包含k个不同字符的最长子串T，返回T的长度

示例1：
INPUT : s = "eceba", k = 2
OUTPUT: 3

示例2：
INPUT : s = "aa", k = 1
OUTPUT: 2

思路：
典型的滑窗法，当初面试pony的原题，可惜没有AC。
"""

class Solution(object):
	def lengthOfLongestSubstringKDistinct(self, s, k):
		"""
		input s: str
		input k: int
		output : int
		"""
		# 特殊情况
		if s == [] or k <= 0:
			return 0
		# 初始化，区间为[l, h)
		n = len(s)
		d = dict()
		l = h = ret = 0
		# 滑窗法
		while h < n:
			# 移动右指针
			while h < n and len(d) <= k:
				d[s[h]] = 1 + d.get(s[h], 0)
				h += 1
			# 更新结果，注意到len(d)的不同情况取值
			curr = h - l - 1 if len(d) == k + 1 else h - l
			ret = max(ret, curr)
			# 移动左指针，直到不满足要求
			while l < h and len(d) >= k:
				d[s[l]] -= 1
				if d[s[l]] == 0:
					del d[s[l]]
				l += 1
		# 返回结果
		return ret


if __name__ == "__main__":
	s = Solution()
	print(s.lengthOfLongestSubstringKDistinct("eceba", 2))
	print(s.lengthOfLongestSubstringKDistinct("aa", 1))