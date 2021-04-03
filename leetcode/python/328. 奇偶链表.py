#!/bin/bash python
"""
328. 奇偶链表
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        新建两个头节点，分别用来存储奇偶节点
        """
        odd = curr_odd = ListNode()
        even = curr_even = ListNode()
        while head:
            # 存储奇数节点
            curr_odd.next = head
            curr_odd = curr_odd.next
            head = head.next
            # 存储偶数节点
            if head:
                curr_even.next = head
                curr_even = curr_even.next
                head = head.next
        curr_even.next = None
        curr_odd.next = even.next
        return odd.next