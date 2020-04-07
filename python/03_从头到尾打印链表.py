#!/bin/bash python3
#-*- coding:utf-8 -*-


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def insertHead(self, x):
        tmp = ListNode(x)
        tmp.next = self.next
        self.next = tmp

    def listPrint(self):
        tmp = self.next
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next


class Solution():
    def printListFromTailToHead(self, listNode):
        vec = []
        if listNode is not None:
            vec += self.printListFromTailToHead(listNode.next)
            vec.append(listNode.val)
        return vec
        """
        以下形式会报错：'NoneType' object is not iterable
        else:
            return vec
        """

    def printListFromTailToHead2(self, listNode):
        """
        参考答案，不断在列表头部插入新元素
        """
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result


def main():
    listNode = ListNode(0)
    listNode.insertHead(5)
    listNode.insertHead(8)
    listNode.insertHead(10)
    listNode.listPrint()

    s = Solution()
    vec = s.printListFromTailToHead(listNode)
    print(vec[:-1])

    print(s.printListFromTailToHead2(listNode))


if __name__ == "__main__":
    main()