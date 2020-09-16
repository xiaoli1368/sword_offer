#!/bin/bash python3

"""
定义栈

注意Node的数据结构和函数是分开的
这样方便去写链栈，而顺序栈可以直接使用list封装接口完成

也可以将Node的数据结构和函数合并，这样需要额外的头节点
例如通过头插法实现push，但这种方式每个Node都会有额外的空间来保存函数

class stackNode():
    def __init__(self, value=0):
        # 初始化
        self.size = 0
        self.val = value
        self.next = None
    
    def pop(self):
        if self.size > 0:
            tmp = self.next.val
            self.next = self.next.next
            # 注意这里不能采用 self = self.next 的方式
            self.size -= 1
            return tmp

    def push(self, newVal):
        # 从顶部往下push，顶部保持不变
        newStack = stackNode(newVal)
        newStack.next = self.next
        self.next = newStack
        self.size += 1

    def top(self):
        if self.size > 0:
            return self.next.val
"""

class oneStackNode():
    def __init__(self, x):
        """
        单个栈节点的定义
        """
        self.val = x
        self.next = None

class StackNode():
    def __init__(self):
        """
        初始化
        """
        self.head = None
        self.size = 0
    
    def push(self, val):
        """
        插入
        """
        newHead = oneStackNode(val)
        newHead.next = self.head
        self.head = newHead
        self.size += 1
    
    def pop(self):
        """
        弹出
        """
        if self.head == None:
            return
        else:
            self.head = self.head.next
            self.size -= 1
    
    def top(self):
        """
        返回顶部的值
        """
        if self.head == None:
            return 0
        else:
            return self.head.val
    
    def size(self):
        """
        获取长度
        """
        return self.size
    
    def empty(self):
        """
        是否为空
        """
        return self.head == None
    
    def getValue(self, k):
        """
        获取第k个值
        """
        if self.head == None or k <= 0 or k > self.size:
            return 0
        else:
            cnt = 0
            curr = self.head
            while curr:
                cnt += 1
                if cnt == k:
                    return curr.val
            return 0

    def setValue(self, k, val):
        """
        修改第k个值
        """
        if self.head == None or k <= 0 or k > self.size:
            return
        else:
            cnt = 0
            curr = self.head
            while curr:
                cnt += 1
                if cnt == k:
                    curr.val = val
                    break
            return
    
    def creatFromList(self, lst):
        """
        从list中创建
        """
        if lst == []:
            return None
        
        head = oneStackNode(lst[0]);
        curr = head
        for i in range(1, len(lst)):
            curr.next = oneStackNode(lst[i])
            curr = curr.next
        
        return head
    
    def saveToList(self):
        """
        保存到list
        """
        if self.head == None:
            return
        
        lst = []
        curr = self.head

        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        return ret
    
    def listPrint(self):
        """
        顺序打印
        """
        if self.head == None:
            return
        
        curr = head
        while curr:
            print("{:d} ".format(curr.val))
            curr = curr.next
        
        return