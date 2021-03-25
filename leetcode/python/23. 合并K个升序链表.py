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

    # ===== 优化版 =====
    def mergeKLists_(self, lists, l, h):
        """
        合并lists[l:h]
        """
        if l > h:
            return None
        elif l == h:
            return lists[l]
        m = (l + h) // 2
        p = self.mergeKLists_(lists, l, m)
        q = self.mergeKLists_(lists, m + 1, h)
        newHead = curr = ListNode()
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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        类似归并排序
        """
        return self.mergeKLists_(lists, 0, len(lists) - 1)

    # ===== 使用优先队列 =====
    # 自定义实现小顶堆，其中内部元素不是int，而是listNode
    def smaller(self, a, b):
        """
        自定义小于函数 a < b
        """
        if a == None:
            return False
        if b == None:
            return True
        return a.val < b.val

    def shift_up(self, vec, i):
        """
        小顶堆上浮
        """
        while (i - 1) // 2 >= 0:
            parent = (i - 1) // 2
            if self.smaller(vec[i], vec[parent]):
                vec[parent], vec[i] = vec[i], vec[parent]
                i = parent
            else:
                break

    def shift_down(self, vec, n, i):
        """
        小顶堆下沉
        """
        while True:
            smalleset, l, r = i, 2 * i + 1, 2 * i + 2
            if l < n and self.smaller(vec[l], vec[smalleset]):
                smalleset = l
            if r < n and self.smaller(vec[r], vec[smalleset]):
                smalleset = r
            if smalleset != i:
                vec[smalleset], vec[i] = vec[i], vec[smalleset]
                i = smalleset
            else:
                break

    def heappush(self, vec, node):
        """
        压入新元素
        """
        vec.append(node)
        self.shift_up(vec, len(vec) - 1)

    def heappop(self, vec):
        """
        弹出堆顶
        """
        vec[0], vec[-1] = vec[-1], vec[0]
        vec.pop()
        self.shift_down(vec, len(vec), 0)

    def heapify(self, vec):
        """
        对vec建堆，注意vec是list，内部元素都是ListNode
        """
        n = len(vec)
        for i in range(n//2-1, -1, -1):
            self.shift_down(vec, n, i)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.heapify(lists)
        head = curr = ListNode()
        while lists and curr:
            curr.next = lists[0]
            curr = curr.next
            self.heappop(lists)
            if curr and curr.next:
                self.heappush(lists, curr.next)
        return head.next