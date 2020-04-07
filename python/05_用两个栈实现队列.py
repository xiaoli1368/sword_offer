#!/bin/bash python3
#-*- coding:utf-8 -*-

"""
[1] 实现一个堆栈
[2] 使用两个堆栈实现一个队列
[3] 直接实现一个队列
"""

class stackNode():
    def __init__(self, value=0):
        self.size = 0
        self.val = value
        self.next = None
    
    def pop(self):
        if self.size > 0:
            tmp = self.next.val
            self.next = self.next.next
            """
            注意这里不能采用 self = self.next 的方式
            """
            self.size -= 1
            return tmp

    def push(self, newVal):
        """
        从顶部往下push，顶部保持不变
        """
        newStack = stackNode(newVal)
        newStack.next = self.next
        self.next = newStack
        self.size += 1

    def top(self):
        if self.size > 0:
            return self.next.val


class queueNode():
    """
    使用两个堆栈实现一个队列
    """
    def __init__(self):
        self.stack1 = stackNode(0)
        self.stack2 = stackNode(0)
        self.size = 0

    def push(self, value):
        self.stack1.push(value)
        self.size += 1

    def pop(self):
        if self.stack2.size > 0:
            self.size -= 1
            return self.stack2.pop()
        
        length = self.stack1.size
        if length > 0:
            for i in range(length):
                tmp = self.stack1.top()
                self.stack1.pop()
                self.stack2.push(tmp)
            return self.pop()


class directQueue():
    """
    直接实现一个队列
    """
    def __init__(self, value=0):
        self.val = value
        self.size = 0
        self.next = None

    def push(self, value):
        newQueue = directQueue(value)
        newQueue.next = self.next
        self.next = newQueue
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        
        tmpNode = self
        tmpVal = 0

        # 寻找倒数第二个节点
        while tmpNode.next.next != None:
            tmpNode = tmpNode.next
        
        tmpVal = tmpNode.next.val
        tmpNode.next = None
        self.size -= 1
        return tmpVal


class Solution:
    """
    用两个栈实现一个队列的高效率版
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if len(self.stack2) != 0:
            return self.stack2.pop()
        
        length = len(self.stack1)
        if length != 0:
            for i in range(length):
                self.stack2.append(self.stack1.pop())

        return self.pop()


def main():
    array = [1, 2, 3, 5, 7]
    my_stack = stackNode(0)
    my_queue = queueNode()
    my_directqueue = directQueue()
    s = Solution()

    print("===== stack / queue / direct-queue test =====")
    print("begin push: -----")
    for i in array:
        print(i, end=" ")
        my_stack.push(i)
        my_queue.push(i)
        my_directqueue.push(i)
        s.push(i)
    print("\nstack size: {}".format(my_stack.size))
    print("queue size: {}".format(my_queue.size))
    print("direct-queue size: {}".format(my_directqueue.size))

    print("begin pop: -----")
    for i in array:
        print("stack: {}, queue: {}, direct-queue: {}, s: {}".format(my_stack.pop(), 
                                                                     my_queue.pop(), 
                                                                     my_directqueue.pop(),
                                                                     s.pop()))
    print("stack size: {}".format(my_stack.size))
    print("queue size: {}".format(my_queue.size))
    print("direct-queue size: {}".format(my_directqueue.size))
    

if __name__ == "__main__":
    main()