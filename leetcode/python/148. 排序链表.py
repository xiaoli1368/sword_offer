#!/bin/bash python
"""
148. 排序链表

使用归并排序的思路，核心步骤如下：
1. 找到链表的中点，并且拆分为两个链表
2. 两个有序链表的merge函数
3. 整体的递归框架

后续添加了插入排序，以及链表快排：
1. 单链表快速排序和数组的快速排序差不多。选一个枢轴然后进行一次划分把数字交换到枢轴的两边。
2. 链表的交换就有两种方法，一个是交换节点，一个是直接交换节点的val值。交换val值比较方便。

链表快排和数组快排的最大区别：
1. 遍历量表方式，由于不能从单链表的末尾向前遍历，因此使用两个指针分别向前向后遍历的策略，失效。
2. 取而代之的就是一趟遍历的方式，将较小的元素放到单链表的左边。具体方法为：
    1) 定义两个指针start，curr，其中start指向较小部分的链表末尾，每次在start后进行新增，注意start的初始化
	2) curr指向当前的节点，使用curr遍历单链表，每遇到一个比支点小的元素，就令start=start->next，然后和curr进行数据交换。
	3) 最终需要和tail进行交换，并且注意输出的节点定义（最好是参考节点的前驱节点）

分析一下链表快排性能较差的原因：
1. 最大的问题就是无法保证随着取值，无法达到nlogn
"""

class ListNode(object):
	def __init__(self, x, next=None):
		self.val = x
		self.next = next


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

	def findMiddle_advanced(self, head):
		"""
		加强版
		"""
		lastp = p = q = head
		while q and q.next:
			lastp = p
			p = p.next
			q = q.next.next
		lastp.next = None
		return p
    
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

	def sortList2(self, head):
		"""
		插入排序
		虽然插排的时间复杂度为O(n^2)，但是面试有可能考察
		因此这里加上，但是显然会超时
		"""
		newHead = ListNode(float("-inf"))
		newHead.next = head
		lastp, p = newHead, head
		while p:
			nextp = p.next
			q = newHead # 表示待插入位置的前一个节点
			while q and q.next and q.next.val < p.val:
				q = q.next
			if q == lastp:
				lastp = p
				p = nextp
				continue
			tmp = q.next
			q.next = p
			p.next = tmp
			lastp.next = nextp
			p = nextp
		return newHead.next
	
	# ===== 链表快排 =====

	def partition(self, head, tail):
		"""
		快排分区函数，返回middle节点的前驱节点
		"""
		# 新建一个头节点，初始化start和curr
		curr = head
		start = ListNode(0, head)
		# 循环进行分区
		while curr:
			if curr.val < tail.val:
				start = start.next
				curr.val, start.val = start.val, curr.val
			curr = curr.next
		midLeft = start
		start = start.next
		tail.val, start.val = start.val, tail.val
		return midLeft
	
	def quickSort(self, head, tail):
		"""
		快排递归函数
		"""
		if head == tail or tail.next == head:
			return
		midLeft = self.partition(head, tail)
		self.quickSort(head, midLeft)
		self.quickSort(midLeft.next.next, tail)
		return

	def sortList3(self, head):
		# 特殊情况处理
		if head == None:
			return None
		# 找到非空的末尾节点
		tail = head
		while tail and tail.next:
			tail = tail.next
		# 进行快排并返回结果
		self.quickSort(head, tail)
		return head