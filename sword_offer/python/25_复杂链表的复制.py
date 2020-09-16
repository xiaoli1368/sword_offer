#!/bin/bash python3
#-*- coding::utf-8 -*-

import time
import random
import copy

class RandomListNode:
    def __init__(self, x=0):
        self.label = x
        self.next = None
        self.random = None
    
    def generate(self, num, maxVal):
        """
        生成题目要求的random链表
        """
        if num <= 0 and maxVal <= 0:
            return None
        
        # 生成基本的链表
        head = RandomListNode(0)
        curr = head
        vec = []

        for i in range(num):
            curr.next = RandomListNode(random.randint(0, maxVal))
            curr = curr.next
            vec.append(curr)
        
        # 建立随机关系
        curr = head.next
        while curr:
            curr.random = vec[random.randint(0, num - 1)]
            curr = curr.next
        
        return head.next
    
    def isSame(self, h1, h2):
        """
        判断两个random链表是否相同
        """
        while h1 and h2:
            if h1.label != h2.label:
                break
            if h1.random == None and h2.random != None:
                break
            if h1.random != None and h2.random == None:
                break
            if h1.random and h2.random and h1.random.label != h2.random.label:
                break
            h1 = h1.next
            h2 = h2.next
        
        return h1 == None and h2 == None
    
    def print_1d_RandomListNode(self, head):
        """
        打印一维链表
        """
        cnt = 0
        while head:
            print("{}, ".format(head.label), end="")
            head = head.next
            cnt += 1
            if cnt >= 20:
                print("..., ", end="")
                break


class Solution:
    def Clone1(self, head):
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
    
    def Clone2(self, h1):
        """
        dict优化版
        """
        if h1 == None:
            return None
        
        h2 = RandomListNode()
        curr1, curr2 = h1, h2
        dic = {None: None}

        # 完全建立线性节点以及映射
        while curr1:
            curr2.next = RandomListNode(curr1.label)
            curr2 = curr2.next
            dic[curr1] = curr2
            curr1 = curr1.next
        
        # 建立随机节点
        while h1:
            dic[h1].random = dic[h1.random]
            h1 = h1.next
        
        return h2.next


    def Clone3(self, head):
        """
        dfs图遍历
        """
        def dfs(head):
            if head == None:
                return None
            if head in dic:
                return dic[head]
            # 创建新节点
            copy = RandomListNode(head.label)
            dic[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        
        dic = dict()
        return dfs(head)
    
    def Clone4(self, head):
        """
        bfs图遍历
        """
        def bfs(head):
            if head == None:
                return None
            clone = RandomListNode(head.label)
            queue = [head]
            dic = {head : clone, None : None}

            while queue:
                tmp = queue.pop(0)
                if tmp.next != None and tmp.next not in dic:
                    dic[tmp.next] = RandomListNode(tmp.next.label)
                    queue.append(tmp.next)
                if tmp.random!= None and tmp.random not in dic:
                    dic[tmp.random] = RandomListNode(tmp.random.label)
                    queue.append(tmp.random)
                dic[tmp].next = dic[tmp.next]
                dic[tmp].random = dic[tmp.random]
            return clone
        
        return bfs(head)
                
    def Clone5(self, head):
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

    def Clone6(self, head):
        """
        深拷贝
        """
        if head == None:
            return None
        return copy.deepcopy(head)
    
    def Clone7(self, head):
        """
        递归法，新链表挂载在旧链表上
        其实就是浅拷贝
        """
        if head == None:
            return None
        
        newhead = RandomListNode(head.label)
        newhead.random = head.random
        newhead.next = self.Clone7(head.next)
        
        return newhead
    
    def test(self, head):
        """
        测试函数
        """
        func_vec = [self.Clone1, 
                    self.Clone2,
                    self.Clone3,
                    self.Clone4,
                    self.Clone5,
                    self.Clone6,
                    self.Clone7]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(head)
            end = time.time()
            print("result: {}, ".format(result.isSame(head, result)), end="")
            result.print_1d_RandomListNode(result)
            print("time(us): {:>5.2f}".format((end - start)*10**6))

def main():
    """
    这个code不是很好测试
    后续补充
    """
    head = RandomListNode().generate(100, 100)

    s = Solution()
    s.test(head)


if __name__ == "__main__":
    main()