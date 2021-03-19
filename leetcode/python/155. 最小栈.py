#!/bin/bash python
"""
155. 最小栈

思路：
使用递减栈作为辅助结构
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        注意到由于基础的数据结构是栈，因此只能在一端进行push/pop
        当新添加的元素num，不对之前的最小值min产生影响时
        后续该元素num是否push/pop，则对之前的min都没有影响
        因此辅助数据结构为：单调递减栈，在栈顶获取min
        相同的元素在原始栈弹出时，单调栈也弹出
        """
        self.comSt = []
        self.minSt = []


    def push(self, x: int) -> None:
        """
        comSt正常push，而minSt确保递减，即栈顶为min
        """
        self.comSt.append(x)
        if self.minSt == [] or self.minSt[-1] >= x:
            self.minSt.append(x)


    def pop(self) -> None:
        """
        comSt正常pop，而minSt只有与comSt相同栈顶时才pop
        """
        if self.minSt[-1] == self.comSt[-1]:
            self.minSt.pop()
        self.comSt.pop()


    def top(self) -> int:
        """
        正常获取
        """
        return self.comSt[-1] if self.comSt else -1


    def getMin(self) -> int:
        """
        获取递减栈的栈顶
        """
        return self.minSt[-1] if self.minSt else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()