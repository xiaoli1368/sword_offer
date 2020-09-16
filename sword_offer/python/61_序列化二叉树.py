#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def Serialize(self, root):
        """
        序列化
        """
        if root == None:
            return "#,"
        else:
            return str(root.val) + "," + self.Serialize(root.left) + self.Serialize(root.right)
    
    def Deserialize(self, s):
        """
        反序列化
        """
        def Des(lst):
            if lst == []:
                return None
            val = lst.pop(0)
            if val == "#":
                return None
            else:
                root = TreeNode.TreeNode(int(val))
                root.left = Des(lst)
                root.right = Des(lst)
                return root
        
        lst = s.split(",") # 利用,分割str为list
        return Des(lst)
    
    def test(self, vec):
        """
        测试函数
        """
        head = TreeNode.TreeNode()
        ori = head.creatFromFrontOrder(vec)
        print("=====")
        start = time.time()
        s = self.Serialize(ori)
        rec = self.Deserialize(s)
        end = time.time()
        
        print("time(us): {:>5.2f}, str: {}".format((end - start)*10**6, s))
        print("ori-front-order: ", end="")
        head.printFrontOrder(ori);
        print("\nrec-front-order: ", end="")
        head.printFrontOrder(rec)
        print()


def main():
    vec = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

    s = Solution()
    s.test(vec)


if __name__ == "__main__":
    main()