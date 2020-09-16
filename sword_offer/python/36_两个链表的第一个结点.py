#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import ListNode
import random

"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution():
    def FindFirstCommonNode(self, h1, h2):
        """
        1. 字典方法
        时间复杂度O(n + m)，空间复杂度O(n)
        """
        if h1 == None or h2 == None:
            return None

        listMap = []
        while h1:
            listMap.append(id(h1))
            h1 = h1.next

        while h2:
            if listMap.count(id(h2)) == 1:
                return h2
            h2 = h2.next

        return None

    def FindFirstCommonNode2(self, h1, h2):
        """
        2. 循环法，高效的迭代解法
        时间复杂度O(n + m)，空间复杂度O(1)
        """
        t1, t2 = h1, h2
        while t1 != t2:
            t1 = t1.next if t1 != None else h2
            t2 = t2.next if t2 != None else h1
        return t1
    
    def test(self, data1, data2):
        """
        测试函数
        输入两个list，分别构建链表，将vec2链接到vec1的中点位置
        """
        func_vec = [self.FindFirstCommonNode,
                    self.FindFirstCommonNode2]
        
        head1 = ListNode.ListNode(0)
        head2 = ListNode.ListNode(0)
        head1.creatFromList(data1)
        head2.creatFromList(data2)
        tail2 = head2.getLastNode()
        tail2.next = head1.getMiddleNode()

        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(head1, head2)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result.val, (end - start)*10**6))
        

def main():
    """
    需要补充测试用例
    """
    data1 = [1, 2, 4, 8, 2, 9, 6]
    data2 = [4, 6, 9]

    data3 = list(random.sample(range(1000), 1000))
    data4 = list(range(1, 100))

    s = Solution()
    s.test(data1, data2)
    s.test(data3, data4)


if __name__ == "__main__":
    main()