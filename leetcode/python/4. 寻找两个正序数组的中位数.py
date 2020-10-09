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
利用中位数的性质，二分查找，变化为求topk的问题，来自leetcode官方解答
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
O(log(m + n))

思路五：
改进版的思路四，来自leetcode官方解答
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
O(log(min(m, n)))
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
			if cnt >= length // 2:
				tmp.append(curr)
		if length % 2 == 1:
			return tmp[-1]
		else:
			return (tmp[-1] + tmp[-2]) / 2
	
	def getKth(self, nums1, nums2, m, n, k):
		"""
		获取两个有序数组中的第topk小的数
		m, n 分别表示 nums1, nums2 的长度
		index1, index2 分别表示两个数组当前的指针
		newIndex1, newIndex2 分别表示二分之后新的指针位置
		pivot1, pivot2 分别表示二分后两个指针处的值
		按照二分法，依次排序不是topk小的元素
		注意随着区间的缩小，k值也在缩小
		"""
		index1 = index2 = 0
		while True:
			# 特殊情况
			if index1 == m:
				return nums2[index2 + k - 1]
			if index2 == n:
				return nums1[index1 + k - 1]
			if k == 1:
				return min(nums1[index1], nums2[index2])
			# 正常情况
			newIndex1 = min(index1 + k // 2 - 1, m - 1)
			newIndex2 = min(index2 + k // 2 - 1, n - 1)
			pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
			if pivot1 <= pivot2:
				k -= newIndex1 - index1 + 1
				index1 = newIndex1 + 1
			else:
				k -= newIndex2 -index2 + 1
				index2 = newIndex2 + 1

	def findMedianSortedArrays4(self, nums1, nums2):
		"""
		利用中位数性质，二分查找
		奇偶合并，统一为求两个topk，k分别为left,right
		left有可能等于right，此时会计算两个相同的topk，可以优化
		"""
		m, n = len(nums1), len(nums2)
		totalLength = m + n
		left = self.getKth(nums1, nums2, m, n, (totalLength + 1) // 2)
		if totalLength % 2 == 1:
			right = left
		else:
			right = self.getKth(nums1, nums2, m, n, (totalLength + 2) // 2)
		return (left + right) / 2

	def findMedianSortedArrays5(self, nums1, nums2):
		"""
		二分查找的优化版
		利用分割线的思想，进行二分查找
		两分割线的和为定值，因此可以对任意一个数组的分割线进行二分
		二分的期望结果是分割线左侧所有元素都小于右侧所有元素
		"""
		# 保证 len(nums1) <= len(nums2)
		if len(nums1) > len(nums2):
			return self.findMedianSortedArrays5(nums2, nums1)
		# 初始化
		inf = 2**40                   # 定义无穷值，用于比较
		m, n = len(nums1), len(nums2) # 两数组长度
		left, right, ansi = 0, m, -1  # 对第一数组二分时的区间，以及分割线位置
		median1, median2 = 0, 0       # 前一部分最大值，后一部分最小值
		# 二分的主循环
		while left <= right:
			i = (left + right) // 2  # i表示数组1的二分点
			j = (m + n + 1) // 2 - i # j表示数组2的二分点，二者总和固定
			# nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i - 1], nums1[i], nums2[j - 1], nums2[j]
			nums_im1 = (-inf if i == 0 else nums1[i - 1])
			nums_i = (inf if i == m else nums1[i])
			nums_jm1 = (-inf if j == 0 else nums2[j - 1])
			nums_j = (inf if j == n else nums2[j])
			# 进行区间放缩
			if nums_im1 <= nums_j:
				ansi = i
				median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
				left = i + 1
			else:
				right = i - 1
		# 输出结果
		return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1

if __name__ == "__main__":
	s = Solution()
	nums1 = [1, 2]
	nums2 = [3, 4]
	print(s.findMedianSortedArrays1(nums1, nums2))
	print(s.findMedianSortedArrays2(nums1, nums2))
	print(s.findMedianSortedArrays3(nums1, nums2))
	print(s.findMedianSortedArrays4(nums1, nums2))
	print(s.findMedianSortedArrays5(nums1, nums2))