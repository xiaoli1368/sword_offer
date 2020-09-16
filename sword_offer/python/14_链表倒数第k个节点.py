#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import ListNode
import random

"""
class ListNode():
    def __init__(self, x=0):
        self.val = x
        self.next = None
"""

class Solution():
    def FindKthToTail1(self, head, k):
        """
        1. 列表存储所有节点
        时间复杂度O(n)，空间复杂度O(n)
        """
        if head == None or k <= 0:
            return None
        
        ptr = []
        while head:
            ptr.append(head)
            head = head.next
        
        if k <= len(ptr):
            return ptr[-k]
        else:
            return None
    
    def FindKthToTail2(self, head, k):
        """
        2. 两重遍历的方式
        时间复杂度O(2n - k)，空间复杂度O(1)
        """
        if head == None or k <= 0:
            return None
        
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        if k > length:
            return None
        
        for i in range(length - k):
            head = head.next
        
        return head

    def FindKthToTail3(self, head, k):
        """
        3. 双指针的方式
        时间复杂度O(n)，空间复杂度O(1)
        """
        if head == None or k <= 0:
            return None
        
        p, q, count = head, head, 0
        while p != None:
            count += 1
            p = p.next
            if count > k:
                q = q.next

        return q if k <= count else None
    
    def test(self, head, k):
        """
        测试函数
        """
        func_vec = [self.FindKthToTail1,
                    self.FindKthToTail2,
                    self.FindKthToTail3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(head, k)
            end = time.time()
            print("time(us): {:>5.2f}, result: ".format((end - start)*10**6), end="")
            if result != None:
                print(result.val)
            else:
                print("None")


def main():
    array = [1, 2, 5, 6, 7, 9]
    head1 = ListNode.ListNode(0)
    head1.creatFromList(array)

    array2 = list(random.sample(range(10000), 10000))
    head2 = ListNode.ListNode(0)
    head2.creatFromList(array2)

    s = Solution()
    s.test(head1, 2)
    s.test(head1, 10)
    s.test(head2, 100)
    s.test(head2, 300)


if __name__ == "__main__":
    main()