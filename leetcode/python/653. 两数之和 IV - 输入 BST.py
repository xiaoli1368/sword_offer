#!/bin/bash/python
"""
653. 两数之和 IV - 输入 BST

思路一：
中序遍历生成hashSet

思路二：
中序遍历生成有序数组，双指针

思路三：
直接递归（待补充）
"""

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def findTarget(self, root, k):
		"""
		hashSet
		"""
		d = dict()
		def mid(root):
			if root == None:
				return
			d[root.val] = True
			mid(root.left)
			mid(root.right)
		mid(root)
		for key in d:
			if key * 2 != k and (k - key) in d:
				return True
		return False
	
	def findTarget2(self, root):
		"""
		中序遍历生成有序数组+双指针
		"""
		node = []
		def mid(root):
			if root == None:
				return
			mid(root.left)
			node.append(root.val)
			mid(root.right)
		mid(root)
		l, r = 0, len(node) - 1
		while l < r:
			ssum = node[l] + node[r]
			if ssum == k:
				return True
			elif ssum < k:
				l += 1
			else:
				r -= 1
		return False