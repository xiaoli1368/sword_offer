#!/bin/bash python
"""
530. 二叉搜索树的最小绝对差

思路：
中序遍历，按照有序数组直接的差值来更新
"""

def Solution(obejct):
    def getMinimumDifference(self, root):
        self.ret = float("+inf")
        self.lastVal = float("-inf")
        def mid(root):
            if root == None:
                return
            mid(root.left)
            self.ret = min(self.ret, root.val - self.lastVal)
            self.lastVal = root.val
            mid(root.right)
            return
        mid(root)
        return self.ret