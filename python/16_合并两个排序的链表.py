#!/bin/bash python3
#-*- coding:utf-8 -*-

"""
主要内容包括：
【１】构建链表结构，初始化，打印
【２】合并两个链表并且打印
"""

import copy
import pdb

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def init_ListNode(self, head, array):
        """
        使用列表初始化链表
        """
        if head == None:
            return
        for i in array:
            head.next = ListNode(i)
            head = head.next

    def print_ListNode(self, head):
        """
        打印输出整个链表
        """
        if head == None:
            return
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def Merge(self, pp, qq):
        """
        合并两个递增的链表，递归法
        """
        # 使用深拷贝隔绝对外界的影响
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)

        if p == None:
            return q
        if q == None:
            return p
        if p.val < q.val:
            p.next = self.Merge(p.next, q)
            return p
        else:
            q.next = self.Merge(p, q.next)
            return q

    def Merge2(self, pp, qq):
        """
        合并两个递增链表，迭代法
        """
        # 使用深拷贝隔绝对外界的影响
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)

        head = ListNode(0)
        tmp = head
        while p != None and q != None:
            if p.val < q.val:
                tmp.next = p
                p = p.next
            else:
                tmp.next = q
                q = q.next
            tmp = tmp.next
        if p == None:
            tmp.next = q
        if q == None:
            tmp.next = p
        return head.next


def main():
    p = ListNode(0)
    q = ListNode(0)
    s = Solution()

    # 初始化两个递增链表
    array1 = [1, 4, 7, 8, 9, 10]
    array2 = [2, 5, 6, 7, 8, 11, 13]
    s.init_ListNode(p, array1)
    s.init_ListNode(q, array2)
    s.print_ListNode(p)
    s.print_ListNode(q)

    # 合并
    m = s.Merge(p, q)
    s.print_ListNode(m)

    m = s.Merge2(p, q)
    s.print_ListNode(m)

    # 查看原始数据是否发生变化
    s.print_ListNode(p)
    s.print_ListNode(q)


if __name__ == "__main__":
    main()