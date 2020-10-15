#!/bin/bash python
"""
116. 填充每个节点的下一个右侧节点指针

思路一：
bfs层次优先遍历

思路二：
dfs
"""

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        层次优先法，队列
        """
        if root == None:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                node.next = queue[0] if queue and i != size - 1 else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    
    def connect2(self, root):
        """
        利用next指针的先序遍历
        """
        def dfs(root, nextNode):
            """
            当前root的下一个节点为nextNode
            遍历当前树，并且构建每个节点的nextNode
            """
            if root == None:
                return
            root.next = nextNode
            dfs(root.left, root.right)
            dfs(root.right, None if root.next == None else root.next.left)
            return
        dfs(root, None)
        return root