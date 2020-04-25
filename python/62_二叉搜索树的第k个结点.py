#!/bin/bash/ python3
#-*- coding:utf-8 -*-

#python排序法：
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.tmp = []
        
    def sortInsert(self, root):
        # 排序后遍历保存
        if root == None:
            return
        self.sortInsert(root.left)
        self.tmp.append(root)
        self.sortInsert(root.right)
        return
    
    def KthNode(self, root, k):
        # 返回对应节点TreeNode
        if root == None or k <= 0:
            return None
        
        self.sortInsert(root)
        if k > len(self.tmp):
            return None
        else:
            return self.tmp[k - 1]

#中序遍历法：
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.index = 0
    
    def KthNode(self, root, k):
        # 返回对应节点TreeNode
        if root == None or k <= 0:
            return None
        
        tmp = self.KthNode(root.left, k)
        if tmp:
            return tmp
        
        self.index += 1
        if self.index == k:
            return root
        
        tmp = self.KthNode(root.right, k)
        if tmp:
            return tmp
        
        return None