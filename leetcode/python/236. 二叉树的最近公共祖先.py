#!/bin/bash python
"""
236. 二叉树的最近公共祖先
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        类似树形dp
        每个节点返回一个状态值
        只有两种可能，空或者非空（某个节点，有可能是公共祖先）
        空表示，该子树没有找到两个节点
        非空表示，该子树是一个或者两个节点的祖先

		这里其实是一个先序遍历
		如果根找到了p/q中的一个，直接返回root
		否则遍历left/right，根据左右子树的状态，确定返回值
        """
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right