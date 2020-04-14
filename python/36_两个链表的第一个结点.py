#!/bin/bash python3
#-*- coding:utf-8 -*-

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def FindFirstCommonNode(self, h1, h2):
        """
        字典方法
        """
        if h1 == None or h2 == None:
            return None

        listMap = []
        
        tmp = h1
        while tmp:
            listMap.append(id(tmp))
            tmp = tmp.next

        tmp = h2
        while tmp:
            if listMap.count(id(tmp)) == 1:
                return tmp
            tmp = tmp.next

        return None

    def FindFirstCommonNode2(self, h1, h2):
        """
        高效的迭代解法
        """
        t1 = h2
        t2 = h2
        while t1 != t2:
            t1 = t1.next if t1 != None else h2
            t2 = t2.next if t2 != None else h1
        return t1
        

def main():
    """
    需要补充测试用例
    """
    pass


if __name__ == "__main__":
    main()