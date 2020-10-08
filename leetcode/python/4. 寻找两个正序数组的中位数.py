#!/bin/bash python
"""
4. 寻找两个正序数组的中位数

思路一：
直接将两个数组合并，排序，寻找中位数

思路二：
利用两个有序数组的条件，直接归并到额外的数组，当长度达到中位数即可

思路三：
在思路二的基础上，不借助额外的数组，只是移动两个指针即可

思路四：
利用中位数的性质，二分查找
"""

class Solution(object):
	def findMedianSortedArrays1(self, nums1, nums2):
		"""
		直接合并，排序，寻找中位数
		"""
		tmp = nums1 + nums2
		length = len(tmp)
		if length % 2 == 1:
			return tmp[length // 2]
		else:
			return (tmp[length // 2 - 1] + tmp[length // 2]) / 2

	def findMedianSortedArrays2(self, nums1, nums2):
		"""
		归并排序，得到前length//2个有序元素，寻找中位数
		"""
		tmp = []
		p = q = 0
		s1, s2 = len(nums1), len(nums2)
		length = s1 + s2
		for _ in range(length // 2 + 1):
			if p < s1 and (q >= s2 or nums1[p] <= nums2[q]):
				tmp.append(nums1[p])
				p += 1
			else:
				tmp.append(nums2[q])
				q += 1
		if length % 2 == 1:
			return tmp[-1]
		else:
			return (tmp[-1] + tmp[-2]) / 2

	def findMedianSortedArrays3(self, nums1, nums2):
		"""
		归并排序，不保存所有的元素，增加计数
		只有当找到第length//2-1和length//2个数时才保存
		只用保存两个数即可
		"""
		tmp = []
		cnt = p = q = 0
		s1, s2 = len(nums1), len(nums2)
		length = s1 + s2
		for _ in range(length // 2 + 1):
			cnt += 1
			if p < s1 and (q >= s2 or nums1[p] <= nums2[q]):
				curr = nums1[p]
				p += 1
			else:
				curr = nums2[q]
				q += 1
			if cnt >= length // 2 - 1:
				tmp.append(curr)
		if length % 2 == 1:
			return tmp[-1]
		else:
			return (tmp[-1] + tmp[-2]) / 2
		

	def findMedianSortedArrays4(self, nums1, nums2):
		"""
		利用中位数性质，二分查找
		"""
		pass

if __name__ == "__main__":
	s = Solution()
	nums1 = [1, 2]
	nums2 = [3, 4]
	print(s.findMedianSortedArrays1(nums1, nums2))
	print(s.findMedianSortedArrays2(nums1, nums2))
	print(s.findMedianSortedArrays3(nums1, nums2))
	print(s.findMedianSortedArrays4(nums1, nums2))