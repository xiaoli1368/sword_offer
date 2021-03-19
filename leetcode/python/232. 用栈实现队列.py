#!/bin/bash python
"""
232. 用栈实现队列

思路：
需要一个额外的栈来完成翻转
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
    

    def pushOneToTwo(self):
        """
        如果s2为空，则将s1中所有的元素pop/push到s2
        """
        if self.s2 == []:
            while self.s1:
                self.s2.append(self.s1.pop())
        return


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.pushOneToTwo()
        return self.s2.pop() if self.s2 else -1


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.pushOneToTwo()
        return self.s2[-1] if self.s2 else -1


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()