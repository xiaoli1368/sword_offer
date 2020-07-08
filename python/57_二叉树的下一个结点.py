#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class TreeLinkNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    
    def creatFromFrontOrder(self, vec):
        """
        从先序序列中构建二叉树
        空为-1
        """
        begin = 0

        def creatFunc(vec, father):
            """
            递归调用的函数，传递上一层的父节点
            """
            nonlocal begin
            if vec == [] or begin >= len(vec) or vec[begin] == -1:
                begin += 1
                return None
            root = TreeLinkNode(vec[begin])
            root.next = father
            begin += 1
            root.left = creatFunc(vec, root)
            root.right = creatFunc(vec, root)
            return root
        
        return creatFunc(vec, None)
    
    def getAllNode(self, root):
        """
        层次遍历，获取所有节点
        """
        if root == None:
            return []
        
        ret, curr_list = [], [root]

        while curr_list:
            next_list = []
            for node in curr_list:
                ret.append(node)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            curr_list = next_list
        
        return ret
    

class Solution:
    def GetNext(self, p):
        """
        获取当前节点的中序遍历的下一个节点
        """
        if p == None:
            return None
        
        if p.right != None: # 右子树非空时，找到右子树的最深左子树即可
            p = p.right
            while p.left != None:
                p = p.left
            return p
        else:
            # 右子树为空时，下一个节点一定在上层的某个双亲节点处
            # 当前节点来自上一层的左子树，直接返回双亲节点
            # 当前节点来自上一层的右子树，继续迭代
            while p.next != None:
                if p == p.next.left:
                    return p.next
                else:
                    p = p.next
            
        return None
    
    def test(self, vec):
        """
        测试函数
        输入先序序列，建立二叉树
        获取层次遍历的全部节点
        输出每个节点的下一个中序遍历节点
        """
        head = TreeLinkNode()
        root = head.creatFromFrontOrder(vec)
        all_node = head.getAllNode(root)

        print("=====")
        for node in all_node:
            start = time.time()
            result = self.GetNext(node)
            end = time.time()
            
            next_node = (-1 if result == None else result.val)
            father_node = (-1 if node.next == None else node.next.val)
            print("curr-node: {:2d}, father-node: {:2d}, next-node: {:2d}, time(us): {:>5.2f}".format(node.val, father_node, next_node, (end - start)*10**6))


def main():
    vec = [1, 2, 4, 8, -1, -1, 9, -1, -1, 5, 10, -1, -1, 11, -1, -1, 3, 6, -1, -1, 7, -1, -1]

    s = Solution()
    s.test(vec)


if __name__ == "__main__":
    main()