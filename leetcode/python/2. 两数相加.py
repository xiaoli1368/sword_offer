#!/bin/bash python
"""
链表版的两数相加，顺序方式（低位位于表头）
可以使用递归或者迭代的方式实现
需要思考进位，几个特殊情况以及退出的条件：
1. 三数之和（两个链表和进位）
2. 两数之和（一个链表和进位）
3. 一数之和（进位）
4. 退出条件（两个链表都是空，且进位为0）
"""

"""
class Node():
    def __init__(self, x):
        # 初始化
        self.val = x
        self.next = None
"""

from ListNode import ListNode

class Solution():
	def addTwoNumbers1(self, p, q):
		"""
		递归版，多函数法，存在优化空间
		"""
		def addOne(s):
			# 只有进位的加法
			if s == 0:
				return None
			else:
				return ListNode(s)
		def addTwo(p, s):
			# 单链表和进位的加法
			if p == None:
				return addOne(s)
			value = p.val + s
			if value >= 10:
				value -= 10
				s = 1
			else:
				s = 0
			head = ListNode(value)
			head.next = addTwo(p.next, s)
			return head
		def addThree(p, q, s):
			# 两个链表和进位的加法
			if p == None:
				return addTwo(q, s)
			if q == None:
				return addTwo(p, s)
			value = p.val + q.val + s
			if value >= 10:
				value -= 10
				s = 1
			else:
				s = 0
			head = ListNode(value)
			head.next = addThree(p.next, q.next, s)
			return head
		# 调用自行编写的函数
		return addThree(p, q, 0)

	def addTwoNumbers2(self, p, q):
		"""
		递归版，高效写法
		"""
		def add(p, q, s):
			# 带进位s的两数之和
			if p == None and q == None and s == 0:
				return None
			if p:
				s += p.val
				p = p.next
			if q:
				s += q.val
				q = q.next
			head = ListNode(s % 10)
			head.next = add(p, q, s // 10)
			return head
		# 调用自行编写的函数
		return add(p, q, 0)

	def addTwoNumbers3(self, p, q):
		"""
		迭代版，高效写法
		"""
		s = 0
		head = ListNode(0)
		curr = head
		while p or q or s:
			if p:
				s += p.val
				p = p.next
			if q:
				s += q.val
				q = q.next
			curr.next = ListNode(s % 10)
			curr = curr.next
			s //= 10
		return head.next