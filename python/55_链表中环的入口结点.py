#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, head):
        # write code here
        tmp = []
        while head != None:
            if tmp.count(head) == 0:
                tmp.append(head)
                head = head.next
            else:
                return head
        
        return None