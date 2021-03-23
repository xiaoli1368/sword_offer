#!/bin/bash python
"""
341. 扁平化嵌套列表迭代器

思路：
1. 递归DFS
2. 堆栈
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        递归，提前存储所有的元素
        """
        self.i = 0
        self.nums = []
        self.dfs(nestedList)
    
    def dfs(self, nestedList):
        """
        递归存储
        """
        if nestedList == []:
            return
        for NestedInteger in nestedList:
            if NestedInteger.isInteger():
                self.nums.append(NestedInteger.getInteger())
            else:
                self.dfs(NestedInteger.getList())
        

    def next(self):
        """
        :rtype: int
        """
        ret = self.nums[self.i]
        self.i += 1
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.nums)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# ===== 堆栈 =====
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        使用堆栈
        反向初始化
        正向弹出解包
        """
        self.st = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.st.append(nestedList[i])
        
    
    def next(self) -> int:
        """
        由于hasNext已经确认存在目标了
        """
        return self.st.pop().getInteger()
        
    
    def hasNext(self) -> bool:
        """
        判断是否存在
        特别的，如果存在list，则需要解包，保证栈顶元素为int
        """
        while self.st and not self.st[-1].isInteger():
            lastList = self.st.pop().getList()
            for i in range(len(lastList) - 1, -1, -1):
                self.st.append(lastList[i])
        return self.st != []