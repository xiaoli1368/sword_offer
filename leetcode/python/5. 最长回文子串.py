#!bin/bash python
"""
5. 最长回文子串

思路一：暴力法
工具函数（对于vec的两个索引l和r，判断vec[l:r+1]是否是回文串）
然后二重循环，遍历每个配对的l和r即可
时间复杂度很大，O(n^3)

思路二：中心延拓法
工具函数（对于vec的两个索引，判断从l和r分别向两端延拓，可以得到最长回文串的边界l,r）

思路三：动态规划
"""

class Solution(object):
	def judge(self, vec, l, r):
		"""
		判断vec[l:r+1]是否为回文
		"""
		while l < r:
			if vec[l] != vec[r]:
				return False
			l += 1
			r -= 1
		return True
	
	def longestPalidrome(self, s):
		"""
		暴力法
		"""
		maxLen = lastl = lastr = 0
		for l in range(len(s)):
			for r in range(l + 1, len(s)):
				if self.judge(s, l, r) and maxLen < r - l + 1:
					maxLen = r - l + 1
					lastl, lastr = l, r
		return s[lastl:lastr+1]
	
	def getLength(self, vec, l, r):
		"""
		获取vec[l]和vec[r]向两端延拓得最长回文串边界l,r
		"""
		if vec[l] != vec[r]:
			return r, l
		while l - 1 >= 0 and r + 1 < len(vec) and vec[l - 1] == vec[r + 1]:
			l -= 1
			r += 1
		return l, r

	def longestPalidrome2(self, s):
		"""
		中心延拓法
		"""
		maxLen = lastl = lastr = 0
		for i in range(2 * len(s) - 1):
			center = i // 2
			if i % 2 == 0:
				l, r = self.getLength(s, center, center)
			else:
				l, r = self.getLength(s, center, center + 1)
			if maxLen < r - l + 1:
				maxLen = r - l + 1
				lastl, lastr = l, r
		return s[lastl:lastr+1]

if __name__ == "__main__":
	s = Solution()
	ss = "babad"
	print(s.longestPalidrome(ss))
	print(s.longestPalidrome2(ss))