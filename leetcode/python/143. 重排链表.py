#!/bin/bash/python
"""
143. 重排链表

思路一：
递归（超时）

思路二：
使用list保存所有节点
依次从首尾添加节点

思路三：
找到中间节点
把后半部分保存到list
依次插入到前半部分中

思路四：
找到中间节点
后半部分翻转链表
两个子链表从头归并
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        递归法
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        # 找到当前的非空尾节点和上一个节点
        p, q = head, head.next
        while q.next:
            p = p.next
            q = q.next
        # 重新排列
        p.next = None
        newHead = head.next
        head.next = q
        q.next = self.reorderList(newHead)
        return head

    def reorderList2(self, head):
        """
        全部保存法
        """
        # 使用list保留所有的节点
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        # 分别从前后取值
        newHead = ListNode()
        tmp = newHead
        index = 0
        while stack:
            tmp.next = stack.pop(index)
            tmp = tmp.next
            index = -1 - index
        tmp.next = None
        return newHead.next

    def reorderList3(self, head):
        """
        后一半保存，插入前一半
        好像不用返回值
        """
        if head == None:
            return None
        # 获取中间节点
        p = q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
        # 保存后半部分到栈
        stack = []
        while p:
            stack.append(p)
            p = p.next
        # 从头依次完成插入操作
        while head and len(stack) > 1:
            tmp = head.next
            head.next = stack.pop()
            head.next.next = tmp
            head = tmp
            if stack:
                stack[-1].next = None
    
    def reorderList4(self, head):
        """
        找中点，翻转，归并
        """
        if head == None and head.next == None:
            return
        # 找中点，断开
        mid = p = q = head
        while q and q.next:
            mid = p
            p = p.next
            q = q.next.next
        mid.next = None
        # 后半部分翻转
        newHead = None
        while p:
            tmp = p.next
            p.next = newHead
            newHead = p
            p = tmp
        # 两链表合并
        h = ListNode()
        while head or newHead:
            if head:
                h.next = head
                h = h.next
                head = head.next
            if newHead:
                h.next = newHead
                h = h.next
                newHead = newHead.next