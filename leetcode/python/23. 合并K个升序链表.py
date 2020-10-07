#!/bin/bash python
"""
23. 合并K个升序链表
归并的思想
"""

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def mergeTwoLists(self, p, q):
		"""
		合并两个有序链表
		"""
		if not p:
			return q
		if not q:
			return p
		if p.val < q.val:
			p.next = self.mergeTwoLists(p.next, q)
			return p
		else:
			q.next = self.mergeTwoLists(p, q.next)
			return q

	def merge(self, lists, l, h):
		"""
		合并k个链表，使用索引确定合并区间
		"""
		if l > h:
			return None
		if l == h:
			return lists[l]
		m = l + (h - l) // 2
		p = self.merge(lists, l, m)
		q = self.merge(lists, m + 1, h)
		return self.mergeTwoLists(p, q)
	
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		return self.merge(lists, 0, len(lists) - 1)
