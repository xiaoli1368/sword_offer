#!/bin/bash python
"""
206. 反转链表

思路：
迭代或者递归
递归的思路有点绕，关键是对head.next递归后，可以使用head.next获取下一层翻转后的尾节点
迭代的思路好理解，注意不需要额外的头节点了
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归，迭代
        """
        last = None
        while head:
            next = head.next
            head.next = last
            last = head
            head = next
        return last

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        curr = self.reverseList(head.next) # 下一层的头节点
        head.next.next = head # 注意head.next是下一层的尾节点
        head.next = None
        return curr

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归版本比较绕
        func：将head翻转，并且返回头节点
        head ----> head.next ----> tail
        head ----> head.next <---- newHead
        """
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead