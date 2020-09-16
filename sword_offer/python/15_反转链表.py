#!bin/bash python3
#-*- coding:utf-8 -*-

import time
import ListNode

"""
class ListNode():
    def __init__(self, x=0):
        self.val = x
        self.next = None
"""

class Solution():
    def ReverseList1(self, head):
        """
        第一次的方式，迭代法
        """
        if head == None:
            return None

        p = head
        q = head.next
        head.next = None

        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        
        return p
    
    def ReverseList2(self, head):
        """
        迭代法优化版
        """
        if head == None or head.next == None:
            return head
        
        p = head.next
        head.next = None

        while p != None:
            q = p.next
            p.next = head
            head = p
            p = q
        
        return head
    
    def ReverseList3(self, head):
        """
        递归法
        """
        if head == None or head.next == None:
            return head
        
        curr = self.ReverseList3(head.next)
        head.next.next = head
        head.next = None

        return curr

    def test(self, head, ifPrint=True):
        """
        测试函数
        """
        func_vec = [self.ReverseList1,
                    self.ReverseList2,
                    self.ReverseList3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(head)
            end = time.time()

            print("time(us): {:>5.2f}, result: ".format((end - start)*10**6), end="")
            if ifPrint:
                result.listPrint(False, " ")
            else:
                print("too many numbers to display")
            
            head = func(result) # 注意恢复
            

def main():
    vec = [2, 3, 9, 5, 1, 7]
    head = ListNode.ListNode(0)
    head.creatFromList(vec)

    vec2 = [0] * 500
    head2= ListNode.ListNode(0)
    head2.creatFromList(vec2)

    s = Solution()
    s.test(head.next, True)
    s.test(head2.next, False)


if __name__ == "__main__":
    main()