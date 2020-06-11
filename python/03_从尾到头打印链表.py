#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import ListNode

"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution():
    def __init__(self):
        """
        初始化结果list
        """
        self.vec_ = []

    def printListFromTailToHead1(self, head):
        """
        1. 递归法
        递归时间复杂度O(n)，空间复杂度O(1)
        """
        if head == None:
            return
        else:
            self.printListFromTailToHead1(head.next)
            self.vec_.append(head.val)
    
    def printListFromTailToHead2(self, head):
        """
        2. 使用堆栈
        时间复杂度O(2n)，空间复杂度O(n)
        """
        if head == None:
            return
        
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        
        while stack != []:
            self.vec_.append(stack[-1])
            stack.pop(-1)
    
    def printListFromTailToHead3(self, head):
        """
        3. 头插法形成新的反向链表，然后顺序输出
        时间复杂度O(2n)，空间复杂度O(n)
        """
        if head == None:
            return
        
        newhead = ListNode.ListNode(0)
        while head != None:
            newhead.insertHead(head.val)
            head = head.next
        
        while newhead.next != None:
            self.vec_.append(newhead.next.val)
            newhead = newhead.next
    
    def printListFromTailToHead4(self, head):
        """
        4. 两次遍历，vec尾部添加
        """
        if head == None:
            return
        
        length = 0
        currhead = head
        while currhead != None:
            length += 1
            currhead = currhead.next
        
        index = 1
        self.vec_ = [0] * length
        while head != None:
            self.vec_[length - index] = head.val
            head = head.next
            index += 1
    
    def printListFromTailToHead5(self, head):
        """
        5. 一次遍历，vec头部添加
        时间复杂度O(n)，空间复杂度O(1)
        """
        if head == None:
            return
        
        while head != None:
            self.vec_.insert(0, head.val)
            head = head.next
    
    def printListFromTailToHead6(self, head):
        """
        6. 原链表基础上直接翻转，然后顺序输出
        其实就是翻转链表了，注意会破坏原有链表
        时间复杂度O(2n)，空间复杂度O(1)
        """
        if head == None:
            return
        
        p = head
        q = head.next
        head.next = None
        while q != None:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        
        while p != None:
            self.vec_.append(p.val)
            p = p. next

    def test(self, datas):
        """
        测试函数
        datas为二维list，每个list对应一个链表
        """
        func_vec = [self.printListFromTailToHead1,
                    self.printListFromTailToHead2,
                    self.printListFromTailToHead3,
                    self.printListFromTailToHead4,
                    self.printListFromTailToHead5,
                    self.printListFromTailToHead6]

        for data in datas:
            print("=====")
            for func in func_vec:
                # 生成链表
                head = ListNode.ListNode(0)
                head.creatFromList(data)
                head = head.next

                # 从尾到头打印
                start = time.time()
                func(head);
                end = time.time()

                # 输出结果
                print("time(us): {:5.2f}, result: ".format((end - start)*10**6), end="")
                if len(self.vec_) > 20:
                    print("too many numbers to display")
                else:
                    print(self.vec_)
                self.vec_.clear()
            

def main():
    data = [[1, 8, 6, 4],
            [4, 5, 0, 9, 4, 2, 6, 9, 1, 7, 5, 2, 2, 4],
            [0] * 500]

    s = Solution()
    s.test(data)


if __name__ == "__main__":
    main()