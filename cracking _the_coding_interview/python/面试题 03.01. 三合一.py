class TripleInOne(object):

    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        self.llen = [0] * 3
        self.vec = [0] * (stackSize * 3)
        self.size = stackSize


    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        if self.llen[stackNum] >= self.size:
            return
        self.vec[stackNum * self.size + self.llen[stackNum]] = value
        self.llen[stackNum] += 1


    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        if self.llen[stackNum] <= 0:
            return -1
        ret = self.vec[stackNum * self.size + self.llen[stackNum] - 1]
        self.llen[stackNum] -= 1
        return ret


    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        if self.llen[stackNum] <= 0:
            return -1
        return self.vec[stackNum * self.size + self.llen[stackNum] - 1]


    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        return self.llen[stackNum] == 0


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)