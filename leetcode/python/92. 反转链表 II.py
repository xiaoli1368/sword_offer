#!/bin/bash python
"""
92. 反转链表 II

思路：
1. 整体上看，有递归和迭代两种思路，但是迭代更加直观并且高效
2. 迭代法可以按部就班操作，也可以一次性操作
3. 按部就班：
	1) 获取前M-1个节点，截断后方。
	2) 获取第[M, N]个节点，截断后方，当前链表翻转。
	3) 三条链表首尾相连。
4. 新建链表头插法
	1) 大体上还是上述的步骤
	2) 区别在于中间遍历的时候直接翻转，可以先翻转完毕后修改连接，也可以直接头插法
	3) 注意完全是新建了一个链表
5. 需要注意的点：
	1) 链表为空，M/N不合理
	2) 链表长度小于M
	3) 遍历长度小于N
6. 待补充：
	1) 递归法
	2) 更加优秀的解法

举一反三：
1. 翻转全部链表
2. 翻转前N个链表
3. 翻转后N个链表
4. 翻转第[M, N]个链表
5. 如果把链表改为数组/字符串呢？那就简单很多，因为可以随机读取了
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write your code here
        """
        1. 链表为空或则mn没有意义
        2. 链表长度小于m
        3. 链表长度小于n
        4. 其它
        
        newHead mprev mnode nnode nnext
        """
        if head == None or m <= 0 or n <= 0 or m > n:
            return head
        
        # 考虑到头节点也可能翻转，因此设置额外头节点
        newHead = ListNode(0, head)
        
        # 找到第m-1个节点
        cnt = 0
        mprev = newHead
        while mprev and cnt < m - 1:
            cnt += 1
            mprev = mprev.next
        
        # 如果后续没有节点
        if mprev == None or mprev.next == None:
            return head
        
        # 翻转[m, n]的节点
        nnode = None
        mnode = curr = mprev.next
        while curr and cnt < n:
            next = curr.next
            curr.next = nnode
            nnode = curr
            curr = next
            cnt += 1
        nnext = curr
        
        # 拼接并返回
        mprev.next = nnode
        mnode.next = nnext
        return newHead.next

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        使用额外存储空间，新建一个链表
		curr对原始的head进行遍历
		对[0, m-1][m+1, n]则新建节点添加
        对[m, n]之间使用头插法
		相当于重新建立链表
        """
        if head == None or m > n:
            return head
        
        Head = ListNode(0)
        curr = tail = Head
        cnt = 0

        while head:
            cnt += 1
            if cnt < m or cnt > n:
                tail.next = ListNode(head.val)
                curr = curr.next
            else:
                tmp = curr.next
                curr.next = ListNode(head.val)
                curr.next.next = tmp
            if tail.next:
                tail = tail.next 
            head = head.next
        
        return Head.next