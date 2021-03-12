#!/bin/bash python
"""
331. 验证二叉树的前序序列化

思路：
递归或者堆栈
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        模仿树的重建，最终应该满足的条件为
        vec[i:]可以形成二叉树，并且i最终达到len(vec)
        """
        i, vec = 0, preorder.split(",")
        # ====================================
        def dfs(vec):
            """
            vec[i:]能否按照先序恢复一颗二叉树
            """
            nonlocal i
            if i >= len(vec): # 越界了
                return False
            elif vec[i] == "#": # 没有越界，当前为空节点
                i += 1
                return True
            else: # 当前为非空节点，遍历左右子树
                i += 1
                return dfs(vec) and dfs(vec)
        # ====================================
        return dfs(vec) and i >= len(vec)

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        利用堆栈
        当出现9##的时候，将其转换为#，判断最终能否剩余一个#即可
        相当于把左子树整体用一个空节点替换了
        """
        stack, vec = [], preorder.split(",")
        for node in vec:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                stack.pop(), stack.pop(), stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"