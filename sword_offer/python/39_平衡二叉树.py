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
    def isBalanced_Solution1(self, root):
        """
        1. 个人解法，先序遍历，自顶向下递归调用，存在优化空间
        """
        if root == None:
            return True
        else:
            return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced_Solution1(root.left) and self.isBalanced_Solution1(root.right)
    
    def depth(self, root):
        """
        获取树的深度
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.depth(root.left), self.depth(root.right))
    
    def isBalanced_Solution2(self, root):
        """
        2. 后序遍历，提前剪枝
        """
        return self.depthAndJudge(root) != -1

    def depthAndJudge(self, root):
        """
        返回当前树的高度，如果是-1，表明是非平衡二叉树
        """
        if root == None:
            return 0
        
        left = self.depthAndJudge(root.left)
        if left == -1:
            return -1
        
        right = self.depthAndJudge(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
    
    def test(self, vec):
        """
        测试函数
        """
        func_vec = [self.isBalanced_Solution1,
                    self.isBalanced_Solution2]
        root = TreeNode.TreeNode().creatFromFrontOrder(vec)
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(root)
            end = time.time()
            print("result: {}, times(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    vec = [3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1]
    vec2 = [1, 2, 3, 4, -1, -1, 4, -1, -1, 3, -1, -1, 2, -1, -1]

    s = Solution()
    s.test(vec)
    s.test(vec2)


if __name__ == "__main__":
    main()