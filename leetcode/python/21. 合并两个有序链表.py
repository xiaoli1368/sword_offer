#!/bin/bash python
"""
21. 合并两个有序链表
有两种思路：递归法，迭代法
可以原地修改链接，或者new新的链表
以下是原地修改的方式（破坏了原始的链表）
"""

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def mergeTwoLists(self, p, q):
		"""
		递归法
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
	
	def mergeTwoLists2(self, p, q):
		"""
		迭代法
		"""
		if not p:
			return q
		if not q:
			return p
		newHead = ListNode()
		i, j, head = p, q, newHead
		while i and j:
			if i.val < j.val:
				head.next = i
				i = i.next
			else:
				head.next = j
				j = j.next
			head = head.next
		if i:
			head.next = i
		if j:
			head.next = j
		return newHead.next

    def mergeTwoLists(self, p, q):
        """
        :type p: ListNode
        :type q: ListNode
        :rtype: ListNode
        迭代的方式，经典
        """
        curr = newHead = ListNode(0)
        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        curr.next = p if p else q
        return newHead.next