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