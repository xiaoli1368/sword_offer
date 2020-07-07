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

class Solution():
    def PrintLevelOrder1(self, root):
        """
        1. 两个向量交替存储
        """
        if root == None:
            return []
        
        ret, curr_list = [], [root]

        while curr_list:
            curr_vec = []
            next_list = []
            for i in curr_list:
                curr_vec.append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            ret.append(curr_vec)
            curr_list = next_list
            
        return ret
    
    def PrintLevelOrder2(self, root):
        """
        2. 队列法，bfs
        """
        if root == None:
            return
        
        ret, queue = [], [root]

        while queue:
            curr_vec = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                curr_vec.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(curr_vec)
        
        return ret
    
    def PrintLevelOrder3(self, root):
        """
        3. 递归法，dfs
        """
        def dfs(root, ret, level):
            if root == None:
                return
            if level >= len(ret):
                ret.append([])
            ret[level].append(root.val)
            dfs(root.left, ret, level + 1)
            dfs(root.right, ret, level + 1)
            return
        
        ret = []
        dfs(root, ret, 0)
        return ret
    
    def test(self, vec):
        """
        测试函数
        """
        func_vec = [self.PrintLevelOrder1,
                    self.PrintLevelOrder2,
                    self.PrintLevelOrder3]
        root = TreeNode.TreeNode().creatFromFrontOrder(vec)
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(root)
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