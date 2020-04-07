#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def reConstructBinaryTree(self, pre, vin):
        newTree = TreeNode(pre[0])
        if len(pre) == 1 and len(vin) == 1:
            return newTree

        index = 0
        for i in vin:
            if i != pre[0]:
                index += 1
            else:
                break

        newLeftPre = newLeftVin = newRightPre = newRightVin = []
        newLeftPre = pre[1 : 1 + index]
        newRightPre = pre[1 + index : ]
        newLeftVin = vin[: index]
        newRightVin = vin[1 + index :]

        if newLeftPre:
            newTree.left = self.reConstructBinaryTree(newLeftPre, newLeftVin)
        if newRightPre:
            newTree.right = self.reConstructBinaryTree(newRightPre, newRightVin)

        return newTree

    def print_front_order(self, tree):
        """
        先序列打印二叉树
        """
        if tree == None:
            return
        print(tree.val, end=" ")
        self.print_front_order(tree.left)
        self.print_front_order(tree.right)

    def print_middle_order(self, tree):
        """
        中序打印二叉树
        """
        if tree == None:
            return
        self.print_middle_order(tree.left)
        print(tree.val, end=" ")
        self.print_middle_order(tree.right)

    def print_end_order(self, tree):
        """
        后序打印二叉树
        """
        if tree == None:
            return
        self.print_end_order(tree.left)
        self.print_end_order(tree.right)
        print(tree.val, end=" ")

    def print_three_order(self, tree):
        """
        三种顺序打印二叉树
        """
        print("===== three order =====")
        self.print_front_order(tree)
        print()
        self.print_middle_order(tree)
        print()
        self.print_end_order(tree)
        print()


def main():
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    vin = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    tree = s.reConstructBinaryTree(pre, vin)

    # 打印输出
    s.print_three_order(tree)



if __name__ == "__main__":
    main()