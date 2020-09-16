#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import TreeNode

"""
class TreeNode():
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def PrintFromTopToBottom1(self, root):
        """
        1. 两层列表互相迭代
        """
        if root == None:
            return []

        result, curr_list = [], [root]
        while curr_list:
            next_list = []
            for node in curr_list:
                result.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            curr_list = next_list
        
        return result

    def PrintFromTopToBottom2(self, root):
        """
        2. 使用list模拟队列的方式
        """
        if root == None:
            return []

        result, queue = [], [root]
        while queue:
            currRoot = queue.pop(0)
            result.append(currRoot.val)
            if currRoot.left:
                queue.append(currRoot.left)
            if currRoot.right:
                queue.append(currRoot.right)

        return result

    def test(self, vec):
        """
        测试函数
        """
        func_vec = [self.PrintFromTopToBottom1,
                    self.PrintFromTopToBottom2]
        head = TreeNode.TreeNode().creatFromFrontOrder(vec)
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(head)
            end = time.time()
            print("times(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    vec = [1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1]
    vec2 = [3, 9, -1, -1, 20, 15, -1, -1, 7, -1, -1]

    s = Solution()
    s.test(vec)
    s.test(vec2)


if __name__ == "__main__":
    main()