#!/bin/bash python
"""
牛客. 判断一个链表是否为回文结构

思路：
1：顺序访问链表，保存到list，然后判断list回文，O(2n)+O(n)
2：找到中间节点，翻转前半部分链表，然后从中间判断回文，O(1.5*n)+O(1)
   缺点是会改变原有的链表结构，且代码量多

注意：
- python有可能超时了，cpp没有超时
"""

# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head):
        # write code here
        if head == None or head.next == None:
            return True
        vec = []
        while head:
            vec.append(head.val)
            head = head.next
        l, h = 0, len(vec) - 1
        while l < h:
            if vec[l] != vec[h]:
                return False
            l += 1
            h -= 1
        return True

    def isPail(self , head):
        # write code here
        if head == None or head.next == None:
            return True
        
        # 找到偏右的中间节点，并且前半部分翻转
        last = None
        slow = fast = head
        while fast and fast.next: # 注意这里的条件
            fast = fast.next.next # 注意要先移动快指针
            next = slow.next
            slow.next = last
            last = slow
            slow = next
        
        # 进行判断
        # 对于 1->2->2->1 的情况，p q分别指向了2 2
        # 对于 1->2->1 的情况，p q分别指向了 1 1
        p = last
        q = slow if fast == None else slow.next # 注意这里
        while p and q and p.val == q.val:
            p = p.next
            q = q.next
        return p == q == None