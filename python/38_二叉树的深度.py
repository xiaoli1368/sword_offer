#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def TreeDepth(self, root):
        if root == None:
            return 0

        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)

        return 1 + (left if left > right else right)
        # return 1 + max(left, right)


def main():
    # 需要补充测试用例
    pass


if __name__ == "__main__":
    main()