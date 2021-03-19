#!/bin/bash python
"""
901. 股票价格跨度

思路：
依旧是单调栈，区别在于单独调用，并且增加了全局的天数信息
"""

class StockSpanner:

    def __init__(self):
        """
        依旧是单调栈
        保存天数和值，(day, price)
        单调栈，寻找每个元素左侧最近的更大值
        返回两个元素的下标之差，如果没有找到则返回1
        单调递减栈，存储价格和下标（使用day代替）
        """
        self.day = 0
        self.st = []
        

    def next(self, price: int) -> int:
        self.day += 1
        while self.st and self.st[-1][1] <= price:
            self.st.pop()
        ret = self.day - (self.st[-1][0] if self.st else 0)
        self.st.append((self.day, price))
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)