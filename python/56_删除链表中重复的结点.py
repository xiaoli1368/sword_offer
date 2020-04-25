#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def checkSame(self, head):
        """
        输入一个结点，输出后边有多个个重复的，以及不重复的那个结点
        """
        cnt = 0
        while head != None and head.next != None:
            if head.val != head.next.val:
                return cnt, head.next
            else:
                cnt += 1
                head = head.next
        
        return cnt, None
        
    def deleteDuplication(self, head):
        if head == None:
            return None
        
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head
        
        while curr != None:
            cnt, tmp = self.checkSame(curr.next)
            if cnt == 0:
                curr = curr.next
            else:
                curr.next = tmp
                
        return new_head.next