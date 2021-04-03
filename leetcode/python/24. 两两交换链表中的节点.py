#!/bin/bash python
"""
24. 两两交换链表中的节点

两种思路：递归法和迭代法
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        递归法
        """
        if head == None or head.next == None:
            return head
        newHead = head.next
        SkipTwo = head.next.next
        newHead.next = head
        head.next = self.swapPairs(SkipTwo)
        return newHead

    def swapPairs2(self, head):
        """
        迭代法，存在优化空间
        """
        if head == None or head.next == None:
            return head

        # 使用头节点统一接口
        newHead = ListNode(0, head)
        last, p, q = newHead, head, head.next

        while p and q:
            skipTwo = q.next
            last.next = q
            q.next = p
            p.next = skipTwo
            if skipTwo == None:
                break
            last, p, q = p, skipTwo, skipTwo.next

        return newHead.next

    def swapPairs3(self, head):
        """
        迭代法，优化版
        last表示待交换的两个节点的上一个节点
        curr表示待交换的两个节点中的第一个
        """
        newHead = ListNode(0, head)
        last, curr = newHead, head
        while curr and curr.next:
            skipTwo = curr.next.next
            last.next = curr.next
            last.next.next = curr
            curr.next = skipTwo
            last, curr = curr, skipTwo
        return newHead.next

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代法
        last ----> head ----> next1 ---->next2
        """
        newHead = last = ListNode(0, head) 
        while head and head.next:
            # 穿针引线
            next1, next2 = head.next, head.next.next
            last.next = next1
            next1.next = head
            head.next= next2
            # 更新指针
            last = head
            head = head.next
        return newHead.next