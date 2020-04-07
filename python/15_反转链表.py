#!bin/bash python3
#-*- coding:utf-8 -*-

class ListNode():
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution():
    def init_use_list(self, head, array):
        """
        使用列表初始化空链表
        """
        if head == None:
            return

        for i in array:
            head.next = ListNode(i)
            head = head.next

    def print_ListNode(self, head):
        """
        打印整个链表
        """
        if head == None:
            return
        
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def ReverseList(self, head):
        """
        反转链表
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


def main():
    s = Solution()
    head = ListNode()
    array = [1, 3, 2, 9, 6, 2]

    s.init_use_list(head, array)
    s.print_ListNode(head)

    head = s.ReverseList(head)
    s.print_ListNode(head)


if __name__ == "__main__":
    main()