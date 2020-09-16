#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time
import ListNode

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def EntryNodeOfLoop1(self, head):
        """
        1. 哈希表解法
        时间复杂度O(n)，空间复杂度O(n)
        """
        if head == None:
            return None
        
        dic = dict()
        while head != None:
            if head in dic:
                return head
            else:
                dic[head] = True
                head = head.next
        
        return None
    
    def EntryNodeOfLoop2(self, head):
        """
        2. 哈希表解法，使用list
        时间复杂度O(n)，空间复杂度O(1)
        """
        if head == None:
            return None
        
        tmp = []
        while head:
            if head in tmp:
                return head
            else:
                tmp.append(head)
                head = head.next
        
        return None
    
    def EntryNodeOfLoop3(self, head):
        """
        3. 快慢指针法
        时间复杂度 > O(n)，空间复杂度O(1)
        """
        if head == None:
            return None
        
        p = q = head
        while p and q and q.next:
            p, q = p.next, q.next.next
            if p == q:
                break
        if p != q:
            return None
        
        p = head
        while p != q:
            p, q = p.next, q.next
        return p
    
    def EntryNodeOfLoop4(self, head):
        """
        4. 标记法，利用链表存储标记
        时间复杂度O(n)，空间复杂度O(1)
        缺点是破化了原有数据
        """
        if head == None:
            return None
        
        while head:
            if head.val == 666:
                return head
            else:
                head.val = 666
                head = head.next
        
        return None

    def test(self, array, pos):
        """
        测试函数
        """
        head = ListNode.ListNode(0)
        head.creatFromList(array)
        tail = head.getLastNode()
        circle = head.getIndexNode(pos)
        tail.next = circle
        
        func_vec = [self.EntryNodeOfLoop1,
                    self.EntryNodeOfLoop2,
                    self.EntryNodeOfLoop3,
                    self.EntryNodeOfLoop4]
        print("=====")

        for func in func_vec:
            start = time.time()
            result = func(head)
            end = time.time()

            print("result: {:d}, pointer: {}, time(us): {:>5.2f}".format(result.val, result, (end - start)*10**6))

def main():
    array = [3, 2, 0, -4, 1, 5]
    array2 = list(range(10000))

    s = Solution()
    s.test(array, 2)
    s.test(array2, 100)


if __name__ == "__main__":
    main()