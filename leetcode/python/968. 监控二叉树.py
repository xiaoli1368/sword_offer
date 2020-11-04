#!/bin/bash python
"""
968. 监控二叉树

思路：

类似树形dp
每棵树返回三种状态
关键点：由底层倒推到顶层可以得到最优结果
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        每个节点返回一个状态值
        0表示已放置相机
        1表示未放置相机，但已覆盖
        2表示未放置相机，且未覆盖
        空节点返回1，本质是一个贪心，类似树形dp
        """
        self.ret = 0
        def back(root):
            if root == None:
                return 1
            left = back(root.left)
            right = back(root.right)
            # 当左右子树有一个未覆盖时，root需要放置相机了
            if left == 2 or right == 2:
                self.ret += 1
                return 0
            # 当左右子树至少有一个放置相机时，root已覆盖
            elif left == 0 or right == 0:
                return 1
            else:
                return 2
		# 注意对根节点的特殊处理
        if back(root) == 2:
            self.ret += 1
        return self.ret