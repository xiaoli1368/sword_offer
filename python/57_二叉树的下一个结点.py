#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, p):
        if p == None:
            return None
        
        if p.right != None:
            p = p.right
            while p.left != None:
                p = p.left
            return p
        else:
            while p.next != None:
                if p == p.next.left:
                    return p.next
                else:
                    p = p.next
            
        return None