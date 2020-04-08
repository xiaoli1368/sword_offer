#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x=0):
        """
        建立二叉树的数据结构
        """
        self.val = x
        self.left = None
        self.right = None

    def init_with_list(self, array):
        """
        使用列表进行初始化
        默认先序列遍历，-1表示此处无值
        以头结点的左子树为真正的树
        """
        def func(a):
            if a == []:
                return None
            elif a[0] == -1:
                a.pop(0)
                return None
            else:
                tmp = TreeNode(a[0])
                a.pop(0)
                tmp.left = func(a)
                tmp.right = func(a)
                return tmp

        a = array.copy()
        self.left = func(a)
        
    def print_TreeNode(self):
        """
        先序列打印二叉树
        """
        def func(head):
            if head == None:
                return
            else:
                print(head.val, end=" ")
                func(head.left)
                func(head.right)

        func(self.left)
        print()


class Solution:
    def __init__(self):
        self.path = []
        self.ret = []

    def FindPath(self, root, target):
        if root == None:
            return self.ret

        self.path.append(root.val)
        target -= root.val

        if target == 0 and root.left == None and root.right == None:
            tmp = self.path[:]
            self.ret.append(tmp)
        else:
            self.FindPath(root.left, target)
            self.FindPath(root.right, target)
        
        self.path.pop(-1)
        return self.ret

def main():
    t = TreeNode()
    t.init_with_list([10, 7, 4, -1, -1, 5, -1, -1, 12, -1, -1])
    t.print_TreeNode()

    # 寻找路径
    s = Solution()
    result = s.FindPath(t.left, 22)
    print(result)


if __name__ == "__main__":
    main()