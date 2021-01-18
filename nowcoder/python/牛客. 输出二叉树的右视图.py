#!/bin/bash python
"""
牛客. 输出二叉树的右视图

思路：
1. 首先思考能否在两个数组上寻找右视图，结果发现不是很好实现
2. 那么最直接的方式就是自行重建二叉树，然后层序遍历，重建的时候存在优化空间，传递index更好，但容易出错
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 求二叉树的右视图
# @param xianxu int整型一维数组 先序遍历
# @param zhongxu int整型一维数组 中序遍历
# @return int整型一维数组
#

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, left, mid):
        """
        已知先序和中序序列，重建二叉树
        """
        if left == [] or mid == [] or len(left) != len(mid):
            return None
        val = left[0]
        i = mid.index(val)
        root = TreeNode(val)
        root.left = self.recoverTree(left[1:1+i], mid[:i])
        root.right = self.recoverTree(left[1+i:], mid[i+1:])
        return root
    
    def solve(self, left, mid):
        # write code here
        root = self.recoverTree(left, mid)
        if root == None:
            return []
        
        ret, queue = [], [root]
        while queue:
            curr = 0
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                curr = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(curr)
        return ret