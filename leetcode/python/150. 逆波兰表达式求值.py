#!/bin/bash python
"""
150. 逆波兰表达式求值

思路：
栈
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        应该就是直接栈操作了
        """
        stack = []
        d = {"+": lambda x, y : x + y,
             "-": lambda x, y : x - y,
             "*": lambda x, y : x * y,
             "/": lambda x, y : int(x / y)}
        for char in tokens:
            if char in d:
                y = stack.pop()
                x = stack.pop()
                stack.append(d[char](x, y))
            else:
                stack.append(int(char))
        return stack[-1]