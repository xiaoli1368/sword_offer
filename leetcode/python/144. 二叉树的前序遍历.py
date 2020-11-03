#!/bin/bash python
"""
144. 二叉树的前序遍历

两种思路：递归法，迭代法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def front(root):
            if root == None:
                return
            ret.append(root.val)
            front(root.left)
            front(root.right)
        front(root)
        return ret
    
    def preorderTraversal2(self, root):
        """
        堆栈的方式
        """
        ret = []
        stack = [root] if root else []

        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return ret