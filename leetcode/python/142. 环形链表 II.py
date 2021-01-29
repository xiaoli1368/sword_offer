#!/bin/bash python
"""
142. 环形链表 II

双指针法
慢指针p每次移动一步，快指针q每次移动两步，当二者相遇时即确定有环
此时将慢指针p移动到头节点head处，q仍保持在相遇处，两指针同速遍历
二者相遇的位置即为环的入口（可以通过画图推断数学关系得到）
"""

class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle1(self, head):
        """
        双指针
        首先需要处理空或者单节点的特殊情况
        """
        if head == None or head.next == None:
            return None
        # 快慢指针遍历
        p = q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                break
        # 确定是否有环
        if p != q:
            return None
        # 有环确定入口
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p
    
    def detectCycle2(self, head):
        """
        双指针法，将特殊情况的判断放在中间位置
        """
        # 快慢指针遍历
        p = q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                break
        # 确定是否有环
        if p != q or (p and p.next == None):
            return None
        # 有环确定入口
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p