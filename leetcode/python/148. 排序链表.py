#!/bin/bash python
"""
148. 排序链表

使用归并排序的思路，核心步骤如下：
1. 找到链表的中点，并且拆分为两个链表
2. 两个有序链表的merge函数
3. 整体的递归框架
"""

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def findMiddle(self, head):
		"""
		找到链表的中点，并且进行拆分
		返回第二个链表的头节点
		注意while条件中添加了q.next.next，可以保证中点为 (h + l) / 2
		如果不加，选择的中点即为(h + l) / 2 + 1
		"""
		if head == None or head.next == None:
			return None
		p = q = head
		while q and q.next and q.next.next:
			p = p.next
			q = q.next.next
		midHead = p.next
		p.next = None
		return midHead
    
	def mergeTwo(self, p, q):
		"""
		合并两个有序链表
		"""
		if not p:
			return q
		if not q:
			return p
		if p.val < q.val:
			p.next = self.mergeTwo(p.next, q)
			return p
		else:
			q.next = self.mergeTwo(p, q.next)
			return q

	def sortList(self, head):
		"""
		单链表排序
		"""
		if head == None or head.next == None:
			return head
		midHead = self.findMiddle(head)
		p = self.sortList(head) # 注意排序后head未必是头节点
		q = self.sortList(midHead)
		return self.mergeTwo(p, q)