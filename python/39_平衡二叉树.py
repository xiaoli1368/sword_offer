#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def __init__(self):
        """
        类内变量，用于保持结果
        """
        self.isBalanced = True

    def getTreeHeight(self, root):
        """
        获取二叉树的高度，同时修改标志
        """
        if root == None:
            return 0

        l = self.getTreeHeight(root.left)
        r = self.getTreeHeight(root.right)

        # 保证l为更大的值
        l, r = max(l, r), min(l, r)

        # 修改符号
        if l - r > 1:
            self.isBalanced = False

        return 1 + l

    def isBalanced_Solution(self, root):
        """
        参考解法
        """
        if root == None:
            return True

        self.getTreeHeight(root)
        return self.isBalanced

    def isBalanced_Solution2(self, root):
        """
        个人解法
        """
        if root == None:
            return True

        l = self.getTreeHeight(root.left)
        r = self.getTreeHeight(root.right)

        l, r = max(l, r), min(l, r)

        return l - r <= 1 and self.isBalanced_Solution2(root.left) and self.isBalanced_Solution2(root.right)


def main():
    # 需要补充测试用例
    pass


if __name__ == "__main__":
    main()