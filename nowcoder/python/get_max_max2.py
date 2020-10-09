#!/bin/bash python
"""
获取最大值和次大值

思路一：
直接排序，找top2

思路二：
冒泡排序，两次冒泡即可

思路三：
归并递归

"""

import time

class Solution(object):
	def getMaxOneAndTwo1(self, num):
		"""
		排序法
		"""
		if num == []:
			return 0, 0
		elif len(num) == 1:
			return num[0], num[0]
		tmp = sorted(num)
		return tmp[-1], tmp[-2]
	
	def getMaxOneAndTwo2(self, num):
		"""
		两次冒泡
		"""
		if len(num) == 0:
			return 0, 0
		elif len(num) == 1:
			return num[0], num[0]
		tmp = num[:]
		for i in range(2):
			for j in range(len(num) - i - 1):
				if tmp[j] > tmp[j + 1]:
					tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
		return tmp[-1], tmp[-2]
	
	def getMaxOneAndTwo3(self, num):
		"""
		归并
		"""
		def mergeGetTwoMax(num, l, h):
			"""
			归并得到最大值和次大值
			"""
			if l == h:
				return num[l], float("-inf")
			if l + 1 == h:
				return max(num[l:h+1]), min(num[l:h+1])
			m = l + (h - l) // 2
			lmax, lmax2 = mergeGetTwoMax(num, l, m)
			hmax, hmax2 = mergeGetTwoMax(num, m + 1, h)
			if lmax > hmax:
				return lmax, max(hmax, lmax2)
			else:
				return hmax, max(lmax, hmax2)
		if len(num) == 0:
			return 0, 0
		elif len(num) == 1:
			return num[0], num[0]
		return mergeGetTwoMax(num, 0, len(num) - 1)

	def test(self, num):
		"""
		测试函数
		"""
		func_vec = [self.getMaxOneAndTwo1,
		            self.getMaxOneAndTwo2,
					self.getMaxOneAndTwo3]
		for func in func_vec:
			start = time.time()
			result = func(num)
			end = time.time()
			print("result: {}, times(us): {:>.5f}".format(result, (end - start)*10**6))

if __name__ == "__main__":
	s = Solution()
	num = [3, 0, 5, 8, 3, 3, 4, 9, 1]
	print(num)
	s.test(num)