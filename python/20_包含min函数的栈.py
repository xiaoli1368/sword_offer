#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution:
    """
    注意最小数必须由一个栈来维护，不能是一个数
    否则经过pop之后就无法保持最小数是正确的了
    也就是说需要保持两个栈的对应性
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or self.min() > node:
            self.minStack.append(node)
        else:
            tmp = self.min()
            self.minStack.append(tmp)

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        if self.stack == [] or self.minStack == []:
            return None
        return self.minStack[-1]


def main():
    s = Solution()

    s.push(1)
    s.push(6)
    s.push(5)
    s.pop()
    s.push(8)
    s.push(0)
    s.push(3)

    print(s.top())
    print(s.min())


if __name__ == "__main__":
    main()