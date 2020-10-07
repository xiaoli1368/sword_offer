#!/bin/bash python
"""
88. 合并两个有序数组
因为题目假定了第一个数组后有足够的空间，因此
直接倒序原地归并即可
"""

class Solution(object):
	def merge(self, num1, m, num2, n):
		"""
		原地倒序归并
		"""
		m -= 1
		n -= 1
		for i in range(m + n + 1, -1, -1):
			if m >= 0 and (n < 0 or num1[m] >= num2[n]):
				num1[i] = num1[m]
				m -= 1
			else:
				num1[i] = num2[n]
				n -= 1

if __name__ == "__main__":
	m, n = 3, 3
	num1 = [1, 2, 3, 0, 0, 0]
	num2 = [2, 5, 6]
	s = Solution()
	s.merge(num1, m, num2, n)
	print(num1)