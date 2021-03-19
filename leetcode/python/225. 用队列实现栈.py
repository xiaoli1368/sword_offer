#!/bin/bash python
"""
225. 用队列实现栈

思路：
使用两个队列，其中一个保持空，每次pop时，将非空的那个正常pop/push到非空
直到剩下最后一个
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        使用两个list队列来模拟栈
        一个队列q2保持空，另一个q1用来push值
        当进行pop的时候，将q1依次顺序pop并push到q2，并把q1的最后一个弹出
        然后q1/q2交换
        """
        self.q1 = []
        self.q2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        ret = self.pop()
        self.q1.append(ret)
        return ret


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1 == [] and self.q2 == []



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()