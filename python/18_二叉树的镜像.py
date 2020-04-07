#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def creat_TreeNode(self, array):
        """
        先序填充一个二叉树, 以-1表示空
        """
        if array == []:
            return None
        if array[0] == -1:
            del array[0]
            return None
        currHead = TreeNode(array[0])
        del array[0]
        currHead.left = self.creat_TreeNode(array)
        currHead.right = self.creat_TreeNode(array)
        return currHead

    def print_TreeNode(self, head):
        """
        先序打印二叉树
        """
        if head == None:
            print(-1, end=" ")
            return

        print(head.val, end=" ")
        self.print_TreeNode(head.left)
        self.print_TreeNode(head.right)

    def Mirror(self, root):
        """
        返回当前二叉树的镜像
        """
        if root == None:
            return root
        
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


def main():
    array = [8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1]

    s = Solution()
    head = s.creat_TreeNode(array)

    s.print_TreeNode(head)
    print()

    head = s.Mirror(head)
    s.print_TreeNode(head)
    print()


if __name__ == "__main__":
    main()