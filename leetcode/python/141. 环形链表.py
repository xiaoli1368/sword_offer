#!/bin/bash python
"""
141. 环形链表

两种思路：哈希表，双指针
"""

class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle1(self, head):
        """
        哈希表方法
        """
        s = set()
        while head:
            if head in s:
                return True
            else:
                s.add(head)
                head = head.next
        return False
    
    def hasCycle2(self, head):
        """
        设置标志位方法，缺点是会修改链表节点
        """
        while head:
            if head.val == 666:
                return True
            else:
                head.val = 666
                head = head.val
        return False
    
    def hasCycle3(self, head):
        """
        双指针法，快慢指针
        """
        p = q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False