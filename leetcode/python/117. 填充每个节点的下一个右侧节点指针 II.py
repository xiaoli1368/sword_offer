#!/bin/bash
"""
117. 填充每个节点的下一个右侧节点指针 II

两种方式：
一是层次遍历，next直接指向右侧节点即可
二是编写一个函数，获取当前节点的同层右侧节点
注意这个右侧节点不一定就是右子树节点
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        层次遍历方法，两个list迭代
        """
        if root == None:
            return None
        
        curr_list = [root]

        while curr_list:
            next_list = []
            for i in range(len(curr_list)):
                node = curr_list[i]
                if i + 1 < len(curr_list):
                    node.next = curr_list[i + 1]
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            curr_list = next_list
        
        return root


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        层序遍历，单个queue
        """
        if root == None:
            return None
        
        queue = [root]

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i < size - 1 and queue != []:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root


class Solution:
    def getNextNode(self, root):
        """
        获取root的右侧节点的下一层的最左侧节点
        """
        nextNode = None
        while root and root.next and nextNode == None:
            root = root.next
            if root.left:
                nextNode = root.left
            elif root.right:
                nextNode = root.right
        return nextNode

    def connect(self, root: 'Node') -> 'Node':
        """
        使用dfs递归，利用next指针
        注意遍历顺序，必须是先right后left
        """         
        def dfs(root, nextNode):
            if root == None:
                return
            root.next = nextNode # 处理根节点
            if root.left == None and root.right == None: # 左右子树都不存在
                return
            nextNode = self.getNextNode(root) # 否则寻找下一个同层右节点 
            if root.right: # 如果存在右子树
                dfs(root.right, nextNode)
                dfs(root.left, root.right)
            elif root.left: # 不存在右子树且左子树不为空
                dfs(root.left, nextNode)
        
        dfs(root, None)
        return root