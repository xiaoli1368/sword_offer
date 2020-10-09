#!/bin/bash python
"""
876. 链表的中间结点

双指针法，快慢指针
"""

class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        当偶数时，返回后一个节点
        """
        p = q = head
        while q and q.next:
            p = p.next
            q = q.next.next
        return p
    
    def middleNode2(self, head):
        """
        当偶数时，返回前一个节点
        """
        p = q = head
        while q and q.next and q.next.next:
            p = p.next
            q = q.next.next
        return p