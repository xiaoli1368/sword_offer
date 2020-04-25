#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, root):
        if root == None:
            return []
        
        ret = []
        curr_list = [root]
        sign = 0
        
        while curr_list:
            tmp = []
            next_list = []
            curr_list.reverse()
            
            for i in curr_list:
                tmp.append(i.val)
                if sign == 0:
                    if i.left:
                        next_list.append(i.left)
                    if i.right:
                        next_list.append(i.right)
                else:
                    if i.right:
                        next_list.append(i.right)
                    if i.left:
                        next_list.append(i.left)
            
            ret.append(tmp)
            curr_list = next_list
            sign = 1 - sign
        
        return ret