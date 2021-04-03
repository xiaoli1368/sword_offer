#!/bin/bash python
"""
83. 删除排序链表中的重复元素
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        新建额外的头节点，对原链表进行一次遍历
        保留每个重复单元的第一个节点
        判断方法就是：curr != last
                 head
            last curr
        """
        last, curr = None, head
        new_head = new_curr = ListNode(0)
        while curr:
            if last == None or last.val != curr.val:
                new_curr.next = curr
                new_curr = new_curr.next
            last, curr = curr, curr.next
        new_curr.next = None
        return new_head.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        这道题，用和82相同的模板便于记忆
        但是单独写更加精简
        顺序遍历，只要和后一个相等，则跳过后一个节点
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head