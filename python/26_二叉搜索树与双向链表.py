#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None
    def Convert(self, root):
        # write code here
        if root == None:
            return None
        
        # 右
        self.Convert(root.right)
        
        # 中
        root.right = self.head
        if self.head != None:
            self.head.left = root
        self.head = root
        
        # 左
        self.Convert(root.left)
        
        return self.head


def main():
    pass


if __name__ == "__main__":
    main()