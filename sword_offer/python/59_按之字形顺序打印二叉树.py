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
        1. 两次list迭代，顺序遍历，直接翻转
        """
        if root == None:
            return []
        
        sign, ret, curr_list = 0, [], [root]
        
        while curr_list:
            curr_vec = []
            next_list = []
            
            for node in curr_list:
                curr_vec.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            
            if sign == 1:
                curr_vec.reverse()
            sign = 1 - sign
            ret.append(curr_vec)
            curr_list = next_list
        
        return ret
 
    def PrintLevelOrder2(self, root):
        """
        2. 两次list迭代，倒序遍历，借助sign翻转
        """
        if root == None:
            return []
        
        sign, ret, curr_list = 0, [], [root]
        
        while curr_list:
            curr_vec = []
            next_list = []
            
            for i in curr_list[::-1]:
                curr_vec.append(i.val)
                if sign == 0:
                    if i.left:
                        next_list.append(i.left)
                    if i.right:
                        next_list.append(i.right)
                else:
                    if i.right:
                        next_list.append(i.right)
                    if i.left:
                        next_list.append(i.left)
            
            sign = 1 - sign
            ret.append(curr_vec)
            curr_list = next_list
        
        return ret
    
    def PrintLevelOrder3(self, root):
        """
        3. 使用list模拟双端队列，选择不同的插入位置
        """
        if root == None:
            return None
        
        ret, queue = [], [root]

        while queue:
            curr_vec = []
            last_num = len(queue)

            for _ in range(last_num):
                node = queue.pop(0)
                insertIndex = 0 if len(ret) % 2 == 1 else len(ret)
                curr_vec.insert(insertIndex, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ret.append(curr_vec)
            
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