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

	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		从后往前合并，增加提前退出的机制
		当n指针用完后直接退出即可
		"""
		m -= 1
		n -= 1
		for i in range(m + n + 1, -1, -1): # 注意m/n值已改变，所以要+1
			if n < 0:
				break
			elif m >= 0 and nums1[m] >= nums2[n]:
				nums1[i] = nums1[m]
				m -= 1
			else:
				nums1[i] = nums2[n]
				n -= 1
		return

if __name__ == "__main__":
	m, n = 3, 3
	num1 = [1, 2, 3, 0, 0, 0]
	num2 = [2, 5, 6]
	s = Solution()
	s.merge(num1, m, num2, n)
	print(num1)