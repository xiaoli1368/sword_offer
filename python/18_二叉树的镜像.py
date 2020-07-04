#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def Mirror1(self, root):
        """
        1. 递归法，自顶向下，在原树上操作
        """
        if root == None:
            return root
        
        root.left, root.right = root.right, root.left
        self.Mirror1(root.left)
        self.Mirror1(root.right)
        return root
    
    def Mirror2(self, root):
        """
        2. 辅助栈，自顶向下，在原树上操作
        """
        if root == None:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root
    
    def Mirror3(self, root):
        """
        3. 递归法，自底向上，新建一颗树
        """
        if root == None:
            return None
        
        head = TreeNode.TreeNode(root.val)
        head.left = self.Mirror3(root.right)
        head.right = self.Mirror3(root.left)
        return head
    
    def test(self, vec):
        """
        测试函数
        """
        func_vec = [self.Mirror1, self.Mirror2, self.Mirror3]
        tmpNode = TreeNode.TreeNode()

        print("=====")
        for func in func_vec:
            root = tmpNode.creatFromFrontOrder(vec)
            start = time.time()
            result = func(root)
            end = time.time()
            print("result: ", end="")
            tmpNode.printFrontOrder(result)
            print("times(us): {:>5.2f}".format((end - start)*10**6))


def main():
    vec = [8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1]

    s = Solution()
    s.test(vec)


if __name__ == "__main__":
    main()