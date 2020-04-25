#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root == None:
            return "#"
        
        return str(root.val) + "!" + self.Serialize(root.left) + self.Serialize(root.right)
    
    def my_Deserialize(self, s):
        # 传递列表更加方便
        if s[0] == "#":
            s.pop(0)
            return None
        
        # 获取当前值
        index = s.index("!")
        curr_val = int("".join(s[:index]))
        del s[:index + 1]
        #s = s[index + 1:] // 这是错误的方式
        
        currNode = TreeNode(curr_val)
        currNode.left = self.my_Deserialize(s)
        currNode.right = self.my_Deserialize(s)
        
        return currNode
        
    def Deserialize(self, s):
        # 注意字符串参数是传值的
        if s == "":
            return None
        
        tmp = list(s)
        return self.my_Deserialize(tmp)