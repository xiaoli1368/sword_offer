#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        # write code here
        ret = []
        if root == None:
            return ret
        
        curr_list = [root]
        
        while curr_list:
            tmp = []
            next_list = []
            for i in curr_list:
                tmp.append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            ret.append(tmp)
            curr_list = next_list
            
        return ret