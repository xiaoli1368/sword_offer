#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def __init__(self):
        """
        初始化
        """
        self.head = None

    def Convert(self, root):
        """
        中序遍历，右中左
        """
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
    
    def print_2d_tree(self, root):
        """
        按链表顺序打印二叉树（先右子树方向，再按左子树方向返回）
        """
        if root == None:
            return
        
        while root:
            print("{}, ".format(root.val), end="")
            tail, root = root, root.right
        
        while tail:
            print("{}, ".format(tail.val), end="")
            tail = tail.left
        print()
    
    def test(self, vec):
        """
        测试函数
        """
        print("=====")
        root = TreeNode.TreeNode().creatFromFrontOrder(vec)

        start = time.time()
        result = self.Convert(root)
        end = time.time()

        print("times(us): {:>5.2f}, result: ".format((end - start)*10**6), end="")
        self.print_2d_tree(result)


def main():
    vec = [4, 2, 1, -1, -1, 3, -1, -1, 6, 5, -1, -1, 7, -1, -1]

    s = Solution()
    s.test(vec)


if __name__ == "__main__":
    main()