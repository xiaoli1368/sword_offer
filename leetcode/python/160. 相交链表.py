#!/bin/bash python
"""
160. 相交链表

思路：
暴力hash或者快慢指针迭代
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        1. 暴力方法：哈希
        2. 迭代方法：双指针，快慢指针
                    一开始二者长度不同，顺序遍历一定不会相交
                    但是经过终点转换后会将差距补上，最终会相遇
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p != None else headB
            q = q.next if q != None else headA
        return p if p == q else None