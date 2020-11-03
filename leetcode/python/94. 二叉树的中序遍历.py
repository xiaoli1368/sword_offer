#!/bin/bash python
"""
94. 二叉树的中序遍历

两种思路：
递归法，迭代法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def mid(root):
            if root == None:
                return 
            mid(root.left)
            ret.append(root.val)
            mid(root.right)
        mid(root)
        return ret
    
    def inorderTraversal2(self, root):
        """
        迭代法
        """
        ret = []
        stack = []
        curr = root
        while stack or curr:
            # 遍历左子树直到最左侧
            while curr:
                stack.append(curr)
                curr = curr.left
            # 保存中间节点
            curr = stack.pop()
            ret.append(curr.val)
            # 指向右子树
            curr = curr.right
        return ret