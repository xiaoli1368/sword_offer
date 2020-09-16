#!/bin/bash python3
#-*- coding:utf-8 -*-

import copy
import pdb
import time
import ListNode

"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution():
    def Merge1(self, pp, qq):
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
            p.next = self.Merge1(p.next, q)
            return p
        else:
            q.next = self.Merge1(p, q.next)
            return q

    def Merge2(self, pp, qq):
        """
        合并两个递增链表，迭代法
        """
        # 使用深拷贝隔绝对外界的影响
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)

        head = ListNode.ListNode(0)
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

    def Merge3(self, pp, qq):
        """
        合并两个递增链表，迭代法，优化版
        """
        # 使用深拷贝隔绝对外界的影响
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)

        head = curr = ListNode.ListNode(0)
        while p and q:
            if p.val < q.val:
                curr.next, p = p, p.next
            else:
                curr.next, q = q, q.next
            curr = curr.next
        curr.next = p if p else q

        return head.next

    def test(self, array1, array2):
        """
        测试函数
        输入两个有序list，各自构造成链表，然后合并
        """
        func_vec = [self.Merge1, self.Merge2, self.Merge3]
        p, q = ListNode.ListNode(0), ListNode.ListNode(0)
        p.creatFromList(array1)
        q.creatFromList(array2)

        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(p.next, q.next)
            end = time.time()

            print("times(us): {:>5.2f}, result: ".format((end - start)*10**6), end="")
            result.listPrint(False)


def main():
    array1 = [1, 4, 7, 8, 9, 10]
    array2 = [2, 5, 6, 7, 8, 11, 13]

    s = Solution()
    s.test(array1, array2)


if __name__ == "__main__":
    main()