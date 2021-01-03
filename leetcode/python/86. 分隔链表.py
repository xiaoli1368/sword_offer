#!/bin/bash python
"""
86. 分隔链表

思路：
1. 明确问题，首先明确这是一个类似排序分区的问题，其次需要向面试官交流，这里的顺序能否只交换值，还是交换节点？
2. 对于可以交换值的问题，则就是快排分区函数，注意分区后的内部顺序无法保证
3. 对于必须交换节点的情况，本题就是插入排序的框架，跟快排分区也很像，定义start表示两个分区的分隔节点（前一个分区的末尾），定义curr为当前遍历的节点，依次把应该位于前一个分区的节点插入到start末尾
4. 优化：上一种思路实现颇为繁琐，实际实现时，可以先遍历，使得start先定位到前一个分区的最后节点，然后再开始之后的遍历
5. 对于上述方法在一个链表中操作较为繁琐，可以用两个新头节点分别存储前后两个分区，最终前后连接即可。（注意在链表中法4高效，但是在数组中法4并不好）

举一反三：
1. 对于可以直接交换值的情况？
2. 对于前后两个分区各自保持原来顺序的情况？或者不需要保持呢？
3. 对于数据结构为数组的情况？（需要考虑元素只能取几个值，或者无穷多值）
4. 对于多个分区的情况，例如输入[x, y]要求链表分区为[-inf, x], [x, y], [y, inf]？（这个问题类似荷兰国旗问题，但是链表就要方便很多，例如该问题可以新建3个头节点，依次形成三个链表，然后首尾相连即可，但是如果数据结构为数组，并且元素取值有无穷多个，那么就难办了）
"""

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        因为要把curr插入到start后方，所以需要保存last_curr
        这个方法有些繁琐
        """
        if head == None:
            return 

        # start表示前一个分区的末尾
        start = newHead = ListNode(0, head)
        last_curr = start
        curr = head

        while curr:
            if curr.val >= x: # 移动last，不动start
                last_curr = curr
                curr = curr.next
            elif curr.val < x and start.next == curr: # 移动last和start
                last_curr = curr
                curr = curr.next
                start = start.next
            elif curr.val < x and start.next != curr: # 不动last动start
                # 断开节点
                last_curr.next = curr.next
                # 插入节点
                next_start = start.next
                start.next = curr
                curr.next = next_start
                # 更新指针
                curr = last_curr.next
                start = start.next

        return newHead.next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return
        
        # 考虑有可能在头部插入，新建额外的头节点
        Head = ListNode(float("-inf"))
        Head.next = head
        
        # 一次遍历，第一个指针定位到开头小于x的最后一个节点
        p = Head
        while p.next and p.next.val < x:
            p = p.next
        
        # 第二个指针开始遍历，大于x的直接跳过，小于的先删除，后插入
        q = p
        while q.next:
            if q.next.val >= x:
                q = q.next
            else:
                deleteNode = q.next
                q.next = q.next.next
                InsertNode = p.next
                p.next = deleteNode
                deleteNode.next = InsertNode
                p = p.next
        
        return Head.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        更好的方法
        一次遍历，得到low和high链表，然后合并
        """
        if head == None:
            return head

        lowHead = lh = ListNode(0)
        highHead = hh = ListNode(0)

        while head:
            next = head.next
            if head.val < x:
                lh.next = head
                lh = lh.next
            else:
                hh.next = head
                hh = hh.next
            head = next
        
        lh.next = highHead.next
        hh.next = None
        return lowHead.next
