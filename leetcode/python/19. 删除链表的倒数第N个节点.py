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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        快慢指针
        要想删除倒数第N
        需要slow在倒数第N+1的时候停止
        特殊情况：
        1. N大于链表长度，没有删除节点（题目限定了 n < length）
        2. 刚好删除头节点
        """
        fast = slow = newHead = ListNode(0, head)
        while fast and fast.next:
            n -= 1
            fast = fast.next
            if n < 0:
                slow = slow.next
        slow.next = slow.next.next
        return newHead.next