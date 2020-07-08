#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode():
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def __init__(self):
        """
        初始化，全局计数变量
        """
        self.cnt = 0

    def KthNode1(self, root, k):
        """
        1. 整体中序遍历，直接索引
        """
        def getMiddleVec(root, vec):
            if root == None:
                return
            else:
                getMiddleVec(root.left, vec)
                vec.append(root)
                getMiddleVec(root.right, vec)
        
        if root == None or k <= 0:
            return None
        
        vec = []
        getMiddleVec(root, vec)
        if k > len(vec):
            return None
        return vec[k - 1]

    def KthNode2(self, root, k):
        """
        中序列遍历法，利用全局变量计数
        """
        if root == None or k <= 0:
            return None
        
        ret = self.KthNode2(root.left, k)
        if ret:
            return ret
        
        self.cnt += 1
        if self.cnt == k:
            return root
        
        ret = self.KthNode2(root.right, k)
        if ret:
            return ret
        
        return None
    
    def test(self, vec, k):
        """
        测试函数
        """
        func_vec = [self.KthNode1, self.KthNode2]
        root = TreeNode.TreeNode().creatFromFrontOrder(vec)
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(root, k)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result.val, (end - start)*10**6))

def main():
    vec = [5, 3, 2, 1, -1, -1, -1, 4, -1, -1, 6, -1, -1]

    s = Solution()
    s.test(vec, 3)


if __name__ == "__main__":
    main()