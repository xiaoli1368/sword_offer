#!/bin/bash python
"""
1145. 二叉树着色游戏
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        我方第一手抢占的节点只有三个，分别是对方的左右子树或父节点
        因此需要遍历得到x.left/right的节点个数，就可以知道三种情况的节点个数
        判断我方能获取最多节点的时候，能否赢下游戏
        """
        def front(root, x):
            """
            先序遍历找到值为x的节点
            """
            if root == None or root.val == x:
                return root
            left = front(root.left, x)
            if left:
                return left
            right = front(root.right, x)
            if right:
                return right
            return None

        def nodeNum(root):
            """
            返回节点个数
            """
            if root == None:
                return 0
            return 1 + nodeNum(root.left) + nodeNum(root.right)
        
        if root == None:
            return True
        curr = front(root, x)
        left = nodeNum(curr.left)
        right = nodeNum(curr.right)
        num = max(left, right, n - left - right - 1)
        return num > n - num