#!/bin/bash python
"""
获取第k个最大值（注意是一个数）

思路一：
无脑排序，取topk

思路二：
冒泡k次

思路三：
快排的思想

思路四：
堆排序的思想
（暂略去，见求所有topk的脚本）
"""

import time

class Solution(object):
	def getTopK1(self, num, k):
		"""
		无脑排序版本
		"""
		if len(num) < k:
			return -1
		num = sorted(num)
		return num[-k]
	
	def getTopK2(self, num, k):
		"""
		冒泡k次版本
		"""
		if len(num) < k:
			return -1
		for i in range(k):
			for j in range(len(num) - i - 1):
				if num[j] > num[j + 1]:
					num[j], num[j + 1] = num[j + 1], num[j]
		return num[-k]

	def partition(self, num, l, h):
		"""
		快排分区函数
		"""
		start = l - 1
		for i in range(l, h):
			if num[i] < num[h]:
				start += 1
				num[i], num[start] = num[start], num[i]
		start += 1
		num[h], num[start] = num[start], num[h]
		return start

	def getTopK3(self, num, k):
		"""
		快排版本
		注意需要将topk最大值，转换为partition输出的正向目标索引
		"""
		if len(num) < k:
			return -1
		l, h, k = 0, len(num) - 1, len(num) - k
		while l <= h:
			m = self.partition(num, l, h) # 注意m是下标
			if m == k:
				return num[m]
			elif m < k:
				l = m + 1
			else:
				h = m - 1

	def test(self, num, k):
		"""
		测试函数
		"""
		func_vec = [self.getTopK1,
		            self.getTopK2,
					self.getTopK3]
		for func in func_vec:
			num_tmp = num[:] # 提前拷贝，防止引用改变值
			start = time.time()
			result = func(num_tmp, k)
			end = time.time()
			print("result: {}, times(us): {:>5.2f}".format(result, (end - start)*10**6))

if __name__ == "__main__":
	k = 5
	num = [3, 0, 5, 8, 3, 3, 4, 9, 1]
	s = Solution()
	s.test(num, k)