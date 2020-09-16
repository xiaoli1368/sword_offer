#!/bin/bash python3

"""
定义二叉树节点
同时封装函数到节点
"""

class TreeNode():
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

    def creatFromFrontOrder(self, vec):
        """
        从先序序列中构建二叉树
        空为-1
        """
        begin = 0

        def creatFunc(vec):
            """
            递归调用的函数
            """
            nonlocal begin # 实现函数内修改函数外的变量
            if vec == [] or begin >= len(vec) or vec[begin] == -1:
                begin += 1
                return None
            root = TreeNode(vec[begin])
            begin += 1
            root.left = creatFunc(vec)
            root.right = creatFunc(vec)
            return root
        
        return creatFunc(vec)
    
    def printFrontOrder(self, root):
        """
        先序遍历输出
        """
        if root == None:
            return
        
        print("{:d}, ".format(root.val), end="")
        self.printFrontOrder(root.left)
        self.printFrontOrder(root.right)
        return

    def printMiddleOrder(self, root):
        """
        中序遍历输出
        """
        if root == None:
            return
        
        self.printMiddleOrder(root.left)
        print("{:d}, ".format(root.val), end="")
        self.printMiddleOrder(root.right)
        return

    def printBackOrder(self, root):
        """
        后序遍历输出
        """
        if root == None:
            return
        
        self.printBackOrder(root.left)
        self.printBackOrder(root.right)
        print("{:d}, ".format(root.val), end="")
        return
    
    def printThreeOrder(self, root):
        """
        输出三种遍历顺序
        """
        if root == None:
            return
        
        print("===== three order =====")
        self.printFrontOrder(root)
        print()
        self.printMiddleOrder(root)
        print()
        self.printBackOrder(root)
        print()