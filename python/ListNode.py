#!/bin/bash python3

"""
定义单链表
"""

class ListNode():
    def __init__(self, x):
        """
        初始化
        """
        self.val = x
        self.next = None
    
    def insertTail(self, x):
        """
        尾部插入
        """
        if self == None:
            return
        
        while self.next != None:
            self = self.next
        
        self.next = ListNode(x)
    
    def insertHead(self, x):
        """
        头部插入
        """
        if self == None:
            return
        
        newNode = ListNode(x)
        newNode.next = self.next
        self.next = newNode
    
    def deleteTail(self):
        """
        尾部删除
        """
        if self == None or self.next == None:
            return
        
        while self.next.next != None:
            self = self.next
        
        del self.next
        self.next = None
    
    def creatFromList(self, lst):
        """
        从list中创建，头节点默认为0
        """
        del self.next

        if lst == []:
            return
        
        for i in lst:
            self.next = ListNode(i)
            self = self.next
    
    def saveToList(self):
        """
        顺序保存到list
        去除了固定头节点
        """
        if self == None:
            return []
        
        ret = []
        while self != None:
            ret.append(self.val)
            self = self.next
        return ret[1:]

    def listPrint(self):
        """
        顺序打印，不包括固定的头指针
        """
        tmp = self.next
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next