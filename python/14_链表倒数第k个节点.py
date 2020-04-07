#!/bin/bash python3
#-*- coding:utf-8 -*-

class ListNode():
    """
    定义链表节点
    """
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def init_use_list(self, xlist):
        """
        使用列表进行初始化
        """
        tmp = self
        for i in xlist:
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = ListNode(i)

    def print_listNode(self):
        """
        打印当前链表
        """
        tmp = self
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
        print()


class Solution():
    def FindKthToTail(self, head, k):
        """
        使用列表存储所有节点
        """
        if head == None or k == 0:
            return None
        
        tmp = [head]
        while head.next:
            head = head.next
            tmp.append(head)
        
        if k <= len(tmp):
            return tmp[-k]
        else:
            return None

    def FindKthToTail2(self, head, k):
        """
        使用双指针的方式
        """
        p = head
        q = head
        count = 0

        while p != None:
            count += 1
            p = p.next
            if count > k:
                q = q.next

        if k < 0 or k > count:
            q = None
        return q


def main():
    s = Solution()
    myNode = ListNode()
    array = [1, 5, 9, 6, 7, 3]

    myNode.init_use_list(array)
    myNode.print_listNode()
    print(s.FindKthToTail(myNode, 3).val)
    print(s.FindKthToTail2(myNode, 3).val)


if __name__ == "__main__":
    main()