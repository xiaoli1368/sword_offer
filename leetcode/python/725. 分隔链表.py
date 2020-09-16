# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if head == None:
            return [None] * k
        
        # 获取链表长度
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        # 获取长度列表
        lst = [length // k] * k
        for i in range(0, length - length // k * k):
            lst[i] += 1
        
        # 分隔
        ret = []
        for currLen in lst:
            if currLen == 0:
                ret.append(None)
            else:
                cnt, p = 1, head
                while cnt < currLen:
                    cnt += 1
                    p = p.next
                ret.append(head)
                head = p.next
                p.next = None
        
        return ret