#!/bin/bash python
"""
1002. 查找常用字符

思路一：
暴力法，先随意选择字符串
然后遍历该字符串里每个字符，检测这个字符是否在其它字符串中都出现了
如果出现了则需要remove掉
注意如果有字符串的遍历完了则需要break

思路二：
构建一个整体的hash，key是所有可能的字符，value是一个list
记录了每个字符串中出现该字符的次数，注意可以为0次
最终每个字符的输出次数为min(value)
"""

class Solution(object):
	def commonChars(self, a):
		"""
		: type a: list[str]
		: return : list[str]
		"""
		if a == "":
			return []
		ret = []
		b = [list(i) for i in a]
		for i in range(len(b[0])):
			appendFlag = True
			char = b[0][i]
			for j in range(1, len(b)):
				if char not in b[j]:
					appendFlag = False
					break
				b[j].remove(char)
			if appendFlag:
				ret.append(char)
		return ret
	
	def commonChars2(self, a):
		"""
		构建hash，key, value = char, []
		"""
		ret, d = [], dict()
		for i in range(len(a)):
			for j in range(len(a[i])):
				char = a[i][j]
				if char not in d:
					d[char] = [0] * len(a)
				d[char][i] += 1
		for key, value in d.items():
			ret += key * min(value)
		return ret

if __name__ == "__main__":
	s = Solution()
	a = ["bella", "label", "roller"]
	print(s.commonChars(a))
	print(s.commonChars2(a))