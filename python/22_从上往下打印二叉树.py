#!/bin/bash python3
#-*- coding:utf-8 -*-

class TreeNode():
    def __init__(self, x=0):
        """
        建立二叉树的数据结构
        """
        self.val = x
        self.left = None
        self.right = None

    def init_with_list(self, array):
        """
        使用列表进行初始化
        默认先序列遍历，-1表示此处无值
        以头结点的左子树为真正的树
        """
        def func(a):
            if a == []:
                return None
            elif a[0] == -1:
                a.pop(0)
                return None
            else:
                tmp = TreeNode(a[0])
                a.pop(0)
                tmp.left = func(a)
                tmp.right = func(a)
                return tmp

        a = array.copy()
        self.left = func(a)
        
    def print_TreeNode(self):
        """
        先序列打印二叉树
        """
        def func(head):
            if head == None:
                return
            else:
                print(head.val, end=" ")
                func(head.left)
                func(head.right)

        func(self.left)
        print()


class Solution:
    def PrintFromTopToBottom(self, root):
        """
        从上往下打印二叉树，使用列表存储的方式
        两层列表互相迭代
        """
        if root == None:
            return []

        result = []
        curr_list = [root]
        while curr_list:
            next_list = []
            for node in curr_list:
                result.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
            curr_list = next_list
            # 到最后，curr_list会变为[]
        
        return result

    def PrintFromTopToBottom2(self, root):
        """
        使用队列的方式
        """
        if root == None:
            return []

        result = []
        queue = []

        # 每次按照层次先后，入列出列即可
        queue.append(root)
        while len(queue) > 0:
            currRoot = queue.pop(0)
            result.append(currRoot.val)
            if currRoot.left:
                queue.append(currRoot.left)
            if currRoot.right:
                queue.append(currRoot.right)

        return result

    def print_type_zhi(self, root):
        """
        拓展，之字型打印，左右，右左，左右，由此递推
        此时不符号队列的形式了，队列是先进先出
        每一层有时间是先进先出，有时候是先进后出
        需要额外的控制变量，实现对于数据结构的反向
        还是两层向量，交替迭代
        """
        if root == None:
            return []

        index = 1
        result = []
        curr_list = [root]

        while curr_list:
            curr_result = []
            next_list = []

            for node in curr_list:
                curr_result.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)

            if index % 2 == 1:
                curr_result.reverse()
            
            index += 1
            result += curr_result
            curr_list = next_list

        return result


def main():
    t = TreeNode()
    t.print_TreeNode()
    t.init_with_list([1, 2, 4, -1, -1, 5, -1, -1, 3, 6, -1, -1, 7, -1, -1])
    t.print_TreeNode()

    # 从上往下打印
    s = Solution()
    print(s.PrintFromTopToBottom(t.left))
    print(s.PrintFromTopToBottom2(t.left))

    # 之字型打印
    print(s.print_type_zhi(t.left))


if __name__ == "__main__":
    main()