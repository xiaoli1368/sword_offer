#!/bin/bash python
"""
有多种思路：

思路一：
自行编写一个链表翻转函数reverse，对输入的两个listNode进行翻转
然后进行顺序的双链表相加，得到结果后进行reverse
时间复杂度较大，空间复杂度也较大

思路二：
将两个链表的值各自保存为list，之后从两个list的尾部进行相加以及进位
空间复杂度较大

思路三：
借助双栈完成逆序，与上一次思路大同小异，同样需要耗费空间

思路四：
其它高效解法，暂不讨论

其它：
可以使用头插法反向构造链表
"""

from ListNode import ListNode

class Solution():
	def addTwoNumbers1(self, p, q):
		"""
		双list法
        """
        if p == None:
            return q
        if q == None:
            return p
        
        tmp = p
        plist = []
        while tmp:
            plist.append(tmp.val)
            tmp = tmp.next
        
        tmp = q
        qlist = []
        while tmp:
            qlist.append(tmp.val)
            tmp = tmp.next
        
        # 从两个list的尾部开始相加
        s = 0
        lasthead = None
        p, q = len(plist) - 1, len(qlist) - 1
        while p >= 0 or q >= 0 or s:
            if p >= 0:
                s += plist[p]
                p -= 1
            if q >= 0:
                s += qlist[q]
                q -= 1
            newhead = ListNode(s % 10)
            newhead.next = lasthead
            lasthead = newhead
            s //= 10
        
        return newhead
	

	def addTwoNumbers2(self, p, q):
		"""
		双栈法，和双list法很像
		"""
		        """
        :type p: ListNode
        :type q: ListNode
        :rtype: ListNode
        """
        if p == None:
            return q
        if q == None:
            return p
		
		def listNodeToStack(head):
			# 转换链表为堆栈，好吧其实就是list
			stack = []
			while head:
				stack.append(head.val)
				head = head.next
			return stack
        
        pstack = listNodeToStack(p)
        qstack = listNodeToStack(q)
        
        # 从两个stack的顶部开始相加，s为进位
        s = 0
        lasthead = None
		while pstack or qstack or s:
            if pstack:
                s += pstack.pop()
            if qstack:
                s += qstack.pop()
            newhead = ListNode(s % 10)
            newhead.next = lasthead
            lasthead = newhead
            s //= 10
        
        return newhead