#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import random

# 不等长最小栈

class Solution:
    def __init__(self):
        """
        初始化
        """
        self.stack = []
        self.minStack = []

    def push(self, node):
        """
        压入
        """
        self.stack.append(node)
        if self.minStack == [] or node <= self.min():
            self.minStack.append(node)

    def pop(self):
        """
        弹出
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        获取顶部元素
        """
        return self.stack[-1]

    def min(self):
        """
        获取最小元素
        """
        return self.minStack[-1]
    
    def test(self, lst):
        """
        测试函数
        push随机数据，中间获取最小值
        pop随机数据，中间获取最小值
        """
        ret = []
        print("=====")

        start = time.time()
        for i in lst:
            self.push(i)
            ret.append(self.min())
        for i in lst:
            ret.append(self.min())
            self.pop()
        end = time.time()
        print("time(us): {:>5.2f}, result: ".format((end - start)*10**6), end="")
        print(ret)


def main():
    lst = random.sample(range(20), 5)
    lst2 = random.sample(range(1000), 100)

    s = Solution()
    s.test(lst)
    s.test(lst2)


if __name__ == "__main__":
    main()