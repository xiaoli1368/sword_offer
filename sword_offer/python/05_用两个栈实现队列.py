#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import random
import StackNode

"""
class stackNode():
    def __init__(self, value=0):
        self.val = value
        self.next = None
"""

class Solution():
    """
    使用两个堆栈实现一个队列
    """
    def __init__(self):
        """
        初始化
        """
        # 使用list封装
        self.s1 = []
        self.s2 = []
        # 使用自定义的栈
        self.stack1 = StackNode.StackNode()
        self.stack2 = StackNode.StackNode()
        
    # ===== 使用list封装 ===== 
    def push(self, val):
        """
        压入
        """
        self.s1.append(val)
    
    def pop(self):
        """
        弹出
        """
        if self.s1 == [] and self.s2 == []:
            return 0
        
        if self.s2 != []:
            return self.s2.pop(-1)
        
        while self.s1:
            self.s2.append(self.s1.pop(-1))
        
        return self.pop()
    
    # ===== 使用自定义的栈 =====
    def push2(self, val):
        """
        压入
        """
        self.stack1.push(val)

    def pop2(self):
        """
        弹出
        """
        if self.stack1.empty() and self.stack2.empty():
            return 0
        
        if not self.stack2.empty():
            tmp = self.stack2.top()
            self.stack2.pop()
            return tmp
        
        while not self.stack1.empty():
            tmp = self.stack1.top()
            self.stack1.pop()
            self.stack2.push(tmp)
        
        return self.pop2()

    def test(self, lst):
        """
        测试函数
        输入lst，全部push，然后全部pop
        """
        print("=====")
        start = time.time()
        for i in lst:
            self.push(i)
        for i in lst:
            print("{:d}, ".format(self.pop()), end="")
        end = time.time()
        print("times(us): {:>5.2f}".format((end - start)*10**6))

        start = time.time()
        for i in lst:
            self.push2(i)
        for i in lst:
            print("{:d}, ".format(self.pop2()), end="")
        end = time.time()
        print("times(us): {:>5.2f}".format((end - start)*10**6))


def main():
    lst = [1, 2, 3, 5, 7]
    lst2 = list(random.sample(range(20), 20))
    lst3 = list(range(100))

    s = Solution()
    s.test(lst)
    s.test(lst2)
    s.test(lst3)


if __name__ == "__main__":
    main()