#!/bin/bash python
"""
234. 回文链表
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseListNode(self, head):
        """
        翻转链表
        """
        last = None
        while head:
            next = head.next
            head.next = last
            last = head
            head = next
        return last
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路：找到中间节点，翻转后一半，然后从前后两端遍历
              注意后半部分可能个数少一
        """
        # 特殊情况
        if head == None or head.next == None:
            return True
        
        # 找到中间节点，并截断
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None

        # 后半段翻转
        p, q = head, self.reverseListNode(mid)

        # 判断两链表是否相同
        # 只有两种情况返回true: p到头，或者q到头且p下一个到头
        while p and q and p.val == q.val:
            p = p.next
            q = q.next
        return p == None or (q == None and p.next == None)