#!/bin/bash python
"""
145. 二叉树的后序遍历

三种思路：

递归法

标记法（标记每个节点，是否应该存储值）
其实其它顺序的遍历也可以状态标记，缺点就是耗费空间
python方便的地方在于list不要求元素的类型统一

迭代法

转自网友：二叉树前中后序的递归版本属于easy题，而迭代版本通常是medium甚至是hard。在做迭代版本之前，我建议大家先问问各类“遍历”算法的本质是什么？是最后输出的那一串有序的数字吗？数字的顺序是对的，遍历算法就是对的吗？个人认为，以上问题的答案都应该是：否。“遍历”的本质是对内存的有序访问，失去了访问顺序，即便你用各种数据结构恢复了这个次序，遍历本身也显得毫无意义。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        def back(root):
            if root == None:
                return
            back(root.left)
            back(root.right)
            self.ret.append(root.val)
            return
        back(root)
        return self.ret

    def postorderTraversal2(self, root):
        """
        直接混合存储节点node和int
        """
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, int):
                ret.append(node)
            elif node != None:
                stack += [node.val, node.right, node.left]
        return ret

    def postorderTraversal3(self, root):
        """
        状态标记法
        0表示节点，1表示值
        """
        ret = []
        stack = [(root, 0)] if root else []
        while stack:
            node, flag = stack.pop()
            if flag == 1:
                ret.append(node.val)
                continue
            stack.append((node, 1))
            if node.right:
                stack.append((node.right, 0))
            if node.left:
                stack.append((node.left, 0))
        return ret

    def postorderTraversal4(self, root):
        """
        更加高效的迭代法
        """
        ret, stack, curr, prev = [], [], root, None
        while stack or curr:
            # 遍历左子树
            while curr:
                stack.append(curr)
                curr = curr.left
            # 获取根节点
            curr = stack.pop()
            if curr.right and curr.right != prev:
                # 遍历右子树
                stack.append(curr)
                curr = curr.right
            else:
                # 遍历根节点
                ret.append(curr.val)
                prev = curr
                curr = None
        return ret