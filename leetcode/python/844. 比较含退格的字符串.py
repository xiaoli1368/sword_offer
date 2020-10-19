#!/bin/bash python
"""
844. 比较含退格的字符串

思路一：
使用堆栈来获取最终的字符串

思路二：
使用双指针进行从后往前的比较
"""

class Solution(object):
	def backspaceCompare(self, s, t):
		"""
		借助栈获取最终的字符串
		"""
		def getStrByStack(s):
			ss = []
			for char in s:
				if char != "#":
					ss.append(char)
				elif ss:
					ss.pop()
			return "".join(ss)
		ss = getStrByStack(s)
		tt = getStrByStack(t)
		return ss == tt
	
	def backspaceCompare2(self, s, t):
		"""
		双指针比较法
		"""
		def jump(s, p):
			"""
			获取字符串s在索引p之前的一个有效字符的索引
			"""
			skip = 0
			p -= 1
			while p >= 0:
				if s[p] == "#":
					skip += 1
					p -= 1
				elif skip > 0:
					p -= 1
					skip -= 1
				else:
					break
			return p
		p, q = len(s), len(t)
		while p >= 0 and q >= 0:
			p = jump(s, p)
			q = jump(t, q)
			if p >= 0 and q >= 0 and s[p] != t[q]:
				return False
		return p < 0 and q < 0

if __name__ == "__main__":
	s = Solution()
	s1 = "nzp#o#g"
	t1 = "b#nzp#o#g"
	print(s.backspaceCompare(s1, t1))
	print(s.backspaceCompare2(s1, t1))