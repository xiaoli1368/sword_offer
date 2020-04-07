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

    def HasSubtree(self, a, b):
        """
        判断b是否为a的子结构
        """
        # 定义用于递归的子函数
        def isSubTree(a, b):
            if b == None:
                return True
            if a == None:
                return False
            if a.val == b.val:
                return isSubTree(a.left, b.left) and isSubTree(a.right, b.right) or isSubTree(a.left, b) or isSubTree(a.right, b)
            else:
                return isSubTree(a.left, b) or isSubTree(a.right, b)
  
        # 调用子函数
        if a == None or b == None:
            return False
        return isSubTree(a, b) 

    def HasSubtree2(self, a, b):
        """
        不定义子函数的方式
        """
        if a == None or b == None:
            return False

        tmp = False
        if a.val == b.val:
            if b.left == b.right == None:
                return True
            elif b.left == None and b.right != None:
                tmp = self.HasSubtree2(a.right, b.right)
            elif b.left != None and b.right == None:
                tmp = self.HasSubtree2(a.left, b.left)
            else:
                tmp = self.HasSubtree2(a.left, b.left) and self.HasSubtree2(a.right, b.right)

        if tmp:
            return tmp
        else:
            return self.HasSubtree2(a.left, b) or self.HasSubtree2(a.right, b)


def main():
    array = [8, 8, 9, -1, -1, 2, 4, -1, -1, 7, -1, -1, 7, -1, -1]
    array2 = [8, 9, -1, -1, 2, -1, -1]

    s = Solution()

    head = s.creat_TreeNode(array)
    head2 = s.creat_TreeNode(array2)

    s.print_TreeNode(head)
    print()
    s.print_TreeNode(head2)
    print()

    print(s.HasSubtree(head, head))
    print(s.HasSubtree2(head, head2))


if __name__ == "__main__":
    main()