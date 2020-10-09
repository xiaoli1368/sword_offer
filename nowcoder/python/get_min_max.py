#!/bin/bash python
"""
无序数组，同时查找最大值和最小值
"""

import time

class Solution(object):
	def getMinMax1(self, num):
		"""
		直接法，时间复杂度为O(n)，比较次数为2n
		"""
		if num == []:
			return 0, 0
		mmin = mmax = num[0]
		for i in num:
			if i < mmin:
				mmin = i
			elif i > mmax:
				mmax = i
		return mmin, mmax
	
	def getMinMax2(self, num):
		"""
		每次取两个数，先自行比较，然后较小值和上一次min比较，较大值和上一个max比较
		时间复杂度为O(n/2)，比较次数为n/2 * 3 = 1.5n
		"""
		if num == []:
			return 0, 0
		mmin = mmax = num[0]
		for i in range(len(num) // 2):
			curr_min = min(num[2*i], num[2*i+1])
			curr_max = max(num[2*i], num[2*i+1])
			mmin = min(mmin, curr_min)
			mmax = max(mmax, curr_max)
		# 处理长度为奇数的情况
		if len(num) % 2 == 1:
			mmin = min(mmin, num[-1])
			mmax = max(mmax, num[-1])
		return mmin, mmax
	
	def getMinMax3(self, num):
		"""
		递归法，类似归并排序，时间复杂度O(log2n)，比较次数是log级别的
		其实对应的物理意义就是两两分组pk，得出min和max
		然后依次进行...，32强，16强，...，4强，2强的淘汰赛
		"""
		def getMinMaxWithIndex(num, l, h):
			if l == h:
				return num[l], num[h]
			m = l + (h - l) // 2
			lmin, lmax = getMinMaxWithIndex(num, l, m)
			hmin, hmax = getMinMaxWithIndex(num, m + 1 ,h)
			return min(lmin, hmin), max(lmax, hmax)
		if num == []:
			return 0, 0
		return getMinMaxWithIndex(num, 0, len(num) - 1)

	def test(self, num):
		"""
		测试函数
		"""
		func_vec = [self.getMinMax1,
		            self.getMinMax2,
					self.getMinMax3]
		for func in func_vec:
			start = time.time()
			result = func(num)
			end = time.time()
			print("result: {}, times(us): {:>.5f}".format(result, (end - start)*10**6))

if __name__ == "__main__":
	num = [3, 0, 5, 8, 3, 3, 4, 9, 1]
	print(num)
	s = Solution()
	s.test(num)