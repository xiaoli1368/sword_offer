#!/bin/bash python
"""
337. 打家劫舍 III

思路：

树形dp
每棵子树返回两个状态值，当前节点被偷/不偷后向下得到的最大值
当前根节点更加左右子树的不同状态，返回root被偷/不偷后的最大值
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        树形dp
        截止到当前root节点，能偷到的最大钱与两个子树的钱有关
        每个子树都应该返回，当前被偷或者不偷，能得到的最大钱
        """
        def back(root):
            """
            后续遍历
            """
            if root == None:
                return 0, 0
            leftOn, leftOff = back(root.left)
            rightOn, rightOff = back(root.right)
            rootOn = root.val + leftOff + rightOff
            rootOff = max(leftOn, leftOff) + max(rightOn, rightOff)
            return rootOn, rootOff
        return max(back(root))