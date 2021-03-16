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
判断s[i:j+1]是否为回文串
if i <= j and s[i] == s[j]:
    f(i, j) = f(i + 1, j - 1) if i + 1 <= j - 1 else True
else:
	f(i, j) = False
注意可以发现f(i, j)的状态需要f(i + 1, j - 1)来确定
因此i要从大到小遍历，j要从小到大遍历
"""

class Solution(object):
    # ===== 暴力法 =====
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

    # ===== 中心延拓法 =====
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
    
    # ===== 中心延拓法（优化版）=====
    def findLength(self, s, l, h):
        """
        对字符串s，以[l:h]为中心进行延拓，找到最长结果
        并且尝试进行更新全局最长结果
        """
        if h < len(s) and s[l] == s[h]:
            while l - 1 >= 0 and h + 1 < len(s) and s[l - 1] == s[h + 1]:
                l -= 1
                h += 1
            if h - l + 1 > self.length:
                self.length, self.l, self.h = h - l + 1, l, h
        return

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        中心延拓法
        """
        self.length = self.l = self.h = 0
        for i in range(len(s)):
            self.findLength(s, i, i)
            self.findLength(s, i, i + 1)
        return s[self.l:self.h+1]
    
    # ===== 动态规划 =====

	def longestPalidrome3(self, s):
		"""
		二维dp
		dp[i][j]表示s[i:j+1]是否为回文串
		"""
		if s == "":
			return

		n = len(s)
		maxLen = l = r = 0
		dp = [[False] * n for _ in range(n)]

		for i in range(n - 1, -1, -1):
			for j in range(n):
				if i <= j and s[i] == s[j]:
					dp[i][j] = dp[i + 1][j - 1] if i + 1 <= j - 1 else True
				if dp[i][j] and maxLen < j - i + 1:
					maxLen = j - i + 1
					l, r = i, j
		return s[l:r+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        动态规划优化版
        """
        n, low, high = len(s), 0, 0
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j] and j - i > high - low:
                    low, high = i, j
        return s[low:high+1]


if __name__ == "__main__":
	s = Solution()
	ss = "babadabsadfl"
	print(s.longestPalidrome(ss))
	print(s.longestPalidrome2(ss))
	print(s.longestPalidrome3(ss))