#!/bin/bash python3
#-*- coding::utf-8 -*-

class RandomListNode:
    def __init__(slef, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, head):
        """
        next指针关联
        """
        if head == None:
            return None
        
        # 遍历节点并拷贝到后面
        currNode = head
        while currNode != None:
            nextNode = currNode.next
            newNode = RandomListNode(currNode.label)
            currNode.next = newNode
            newNode.next = nextNode
            currNode = nextNode
            
        # 拷贝随机的链接关系
        currNode = head
        while currNode != None:
            currNode.next.random = currNode.random.next if currNode.random else None
            currNode = currNode.next.next
            
        # 从旧链表中分离出新链表
        currNode = head
        headClone = head.next
        while currNode != None:
            tmp = currNode.next
            currNode.next  = tmp.next
            tmp.next = tmp.next.next if tmp.next else None
            currNode = currNode.next
            
        return headClone

    def Clone2(self, head):
        """
        map映射方法
        """
        if head == None:
            return None
        
        head1 = head
        head2 = RandomListNode(head1.label)
        newhead = head2
        Map = {head1 : head2}
        
        # 完全复制并且建立映射
        while head1 != None:
            if head1.next != None:
                head2.next = RandomListNode(head1.next.label)
                
            head1 = head1.next
            head2 = head2.next
            Map[head1] = head2
            
        # 复制随机的链接
        head1 = head
        head2 = newhead
        while head1 != None:
            head2.random = Map[head1.random]
            head1 = head1.next
            head2 = head2.next
            
        return newhead
    
    def Clone3(self, head):
        """
        递归方法（这种方式，新链表挂载在了旧链表上）
        """
        if head == None:
            return None
        
        newhead = RandomListNode(head.label)
        newhead.random = head.random
        newhead.next = self.Clone(head.next)
        
        return newhead


def main():
    """
    这个code不是很好测试
    后续补充
    """
    pass


if __name__ == "__main__":
    main()