#!/bin/bash/ python3
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

class Solution():
    def isSymmetrical(self, root):
        """
        递归法
        """
        def isSame(a, b):
            if a == None and b == None:
                return True
            if a == None or b == None:
                return False
            return a.val == b.val and isSame(a.left, b.right) and isSame(a.right, b.left)

        if root == None:
            return False
        else:
            return isSame(root.left, root.right)
    
    def test(self, vec):
        """
        测试函数
        """
        head = TreeNode.TreeNode()
        print("=====")
        root = head.creatFromFrontOrder(vec)
        start = time.time()
        result = self.isSymmetrical(root)
        end = time.time()
        print("result: {}, times(us): {:>5.2f}, front-order: ".format(result, (end - start)*10**6), end="")
        head.printFrontOrder(root)
        print()


def main():
    vec = [1, 2, 3, -1, -1, 4, -1, -1, 2, 4, -1, -1, 3, -1, -1]
    vec2 = [1, 2, -1, 3, -1, -1, 2, -1, 3, -1, -1]

    s = Solution()
    s.test(vec)
    s.test(vec2)


if __name__ == "__main__":
    main()