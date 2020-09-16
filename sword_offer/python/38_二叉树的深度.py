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

class Solution():
    def TreeDepth1(self, root):
        """
        递归法
        """
        if root == None:
            return 0

        left = self.TreeDepth1(root.left)
        right = self.TreeDepth1(root.right)
        return 1 + max(left, right)
    
    def TreeDepth2(self, root):
        """
        迭代法，bfs，寻找最深的层次
        """
        if root == None:
            return 0
        
        ret = 0
        last = [root]

        while last:
            curr = []
            for node in last:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            last = curr
            ret += 1
        
        return ret
    
    def test(self, root):
        """
        测试函数
        """
        func_vec = [self.TreeDepth1, self.TreeDepth2]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(root)
            end = time.time()
            print("result: {:d}, times(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    vec = [3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1]
    root = TreeNode.TreeNode().creatFromFrontOrder(vec)

    s = Solution()
    s.test(root)


if __name__ == "__main__":
    main()