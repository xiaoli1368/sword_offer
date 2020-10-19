#!/bin/bash python
"""
19. 删除链表的倒数第N个节点

两个注意的点：
1. 双指针找到倒数第k个节点
2. 新建节点，用来处理头节点
"""

class ListNode(object):
	def __init__(self, x):
		self.x = x
		self.next = next

class Solution(object):
	def removeNthFromEnd(self, head, n):
		newHead = ListNode(0)
		newHead.next = head
		cnt = 0
		p = q = newhead
		while q:
			q = q.next
			if cnt > n:
				p = p.next
			cnt += 1
		p.next = p.next.next
		return newHead.next