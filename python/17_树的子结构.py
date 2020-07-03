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
    def HasSubtree(self, a, b):
        """
        1. 内部定义递归函数
        注意需要传递flag记录之前是否已经对齐
        """
        def isSubTree(a, b, flag):
            if b == None:
                return True
            if a == None:
                return False
            if flag and a.val != b.val: # 如果之前对齐，本次不等
                return False
            if a.val == b.val and isSubTree(a.left, b.left, True) and isSubTree(a.right, b.right, True):
                return True
            else:
                return isSubTree(a.left, b, False) or isSubTree(a.right, b, False)
  
        # 调用子函数
        if a == None or b == None:
            return False
        return isSubTree(a, b, False) 

    def HasSubtree2(self, a, b):
        """
        2. 更加高效的方式
        """
        def isSubTree(a, b):
            if b == None:
                return True
            if a == None or a.val != b.val:
                return False
            return isSubTree(a.left, b.left) and isSubTree(a.right, b.right)
        
        return (a != None and b != None) and (isSubTree(a, b) or self.HasSubtree2(a.left, b) or self.HasSubtree2(a.right, b))
    
    def test(self, A, B):
        """
        测试函数
        """
        func_vec = [self.HasSubtree, self.HasSubtree2]
        head = TreeNode.TreeNode(0)
        a = head.creatFromFrontOrder(A)
        b = head.creatFromFrontOrder(B)

        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(a, b)
            end = time.time()
            print("result: {}, times(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    A = [8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1]
    B = [8, 9, -1, -1, 2, -1, -1]
    A2 = [1, 0, -4, -1, -1, -3, -1, -1, 1, -1, -1]
    B2 = [1, -4, -1, -1, -1]

    s = Solution()
    s.test(A, B)
    s.test(A2, B2)


if __name__ == "__main__":
    main()