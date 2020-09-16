#！/bin/bash python3

class directQueue():
    """
    直接实现一个队列
    简易版本，后续待优化
    """
    def __init__(self, value=0):
        self.val = value
        self.size = 0
        self.next = None

    def push(self, value):
        newQueue = directQueue(value)
        newQueue.next = self.next
        self.next = newQueue
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        
        tmpNode = self
        tmpVal = 0

        # 寻找倒数第二个节点
        while tmpNode.next.next != None:
            tmpNode = tmpNode.next
        
        tmpVal = tmpNode.next.val
        tmpNode.next = None
        self.size -= 1
        return tmpVal