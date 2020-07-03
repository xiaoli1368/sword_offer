#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution():
    def reConstructBinaryTree1(self, pre, vin):
        """
        第一次的方式
        存在较大的优化空间
        """
        newTree = TreeNode.TreeNode(pre[0])
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
            newTree.left = self.reConstructBinaryTree1(newLeftPre, newLeftVin)
        if newRightPre:
            newTree.right = self.reConstructBinaryTree1(newRightPre, newRightVin)

        return newTree
    
    def reConstructBinaryTree2(self, pre, vin):
        """
        递归优化版
        但是中间重新生成了list，所以低效
        更加高效的方式是传递list引用，以及索引
        """
        if pre == [] or vin == []:
            return None
        
        mid = vin.index(pre[0])
        root = TreeNode.TreeNode(pre[0])
        root.left = self.reConstructBinaryTree2(pre[1:mid+1], vin[:mid])
        root.right = self.reConstructBinaryTree2(pre[mid+1:], vin[mid+1:])

        return root
    
    def test(self, pre, vin):
        """
        测试函数
        """
        func_vec = [self.reConstructBinaryTree1,
                    self.reConstructBinaryTree2]
        print("=====")
        for func in func_vec:
            start = time.time()
            root = func(pre, vin)
            end = time.time()
            print("times(us): {:>5.2f}, result: ".format((end - start)*10**6))
            root.printThreeOrder(root)


def main():
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    vin = [4, 7, 2, 1, 5, 3, 8, 6]

    s = Solution()
    s.test(pre, vin)


if __name__ == "__main__":
    main()