#!/bin/bash python
"""
82. 删除排序链表中的重复元素 II
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
        前后都不存在重复才进行保存
        判断方法就是：curr != last and curr != curr.next
                 head
            last curr
        """
        last, curr = None, head
        new_head = new_curr = ListNode(0)
        while curr:
            next = curr.next
            if (last == None or last.val != curr.val) and (next == None or curr.val != next.val):
                new_curr.next = curr
                new_curr = new_curr.next
            last, curr = curr, curr.next
        new_curr.next = None
        return new_head.next