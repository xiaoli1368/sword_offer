#!/bin/bash python3
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
    def FindPath(self, root, target):
        """
        递归法
        """
        path = [] # 记录临时的一条路径
        ret = []  # 记录最终的结果

        def backTracking(root, target):
            if root == None:
                return
            
            path.append(root.val)
            target -= root.val

            if target == 0 and root.left == root.right == None:
                ret.append(path[:]) # 拷贝添加
            else:
                backTracking(root.left, target)
                backTracking(root.right, target)
            
            path.pop()

        backTracking(root, target)
        return ret
    
    def test(self, vec, target):
        """
        测试函数
        """
        root = TreeNode.TreeNode().creatFromFrontOrder(vec)

        print("=====")
        start = time.time()
        result = self.FindPath(root, target)
        end = time.time()
        print("times(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    vec = [10, 7, 4, -1, -1, 5, -1, -1, 12, -1, -1]
    vec2 = [5, 4, 11, 7, -1, -1, 2, -1, -1, -1, 8, 13, -1, -1, 4, 5, -1, -1, 1, -1, -1]

    s = Solution()
    s.test(vec, 22)
    s.test(vec2, 22)


if __name__ == "__main__":
    main()