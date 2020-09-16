#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time
import ListNode

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplication(self, head):
        """
        第一次的方式，利用辅助函数，检测当前节点后续的重复次数
        """
        if head == None:
            return None
        
        new_head = ListNode.ListNode(0)
        new_head.next = head
        curr = new_head
        
        while curr != None:
            cnt, tmp = self.checkSame(curr.next)
            if cnt == 0:
                curr = curr.next
            else:
                curr.next = tmp
                
        return new_head.next

    def checkSame(self, head):
        """
        输入一个结点，输出后边有多个个重复的，以及不重复的那个结点
        """
        cnt = 0
        while head != None and head.next != None:
            if head.val != head.next.val:
                return cnt, head.next
            else:
                cnt += 1
                head = head.next
        
        return cnt, None
    
    def test(self, array):
        """
        测试函数
        """
        head = ListNode.ListNode(0)
        head.creatFromList(array)
        
        print("=====")
        start = time.time()
        result = self.deleteDuplication(head.next)
        end = time.time()
        print("time(us): {:>5.2f}, result: ".format((end - start)*10**6))
        result.listPrint(False)
        

def main():
    array = [1, 1, 2, 3, 3, 5, 7, 7, 9]
    array2 = [1] * 100 + [2] * 200 + [3] + [4] * 400 + [5]

    s = Solution()
    s.test(array)
    s.test(array2)


if __name__ == "__main__":
    main()