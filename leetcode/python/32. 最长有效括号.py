#!/bin/bash python
"""
32. 最长有效括号

每道题需要想清楚几个问题：
1. 我是如何想到的？
2. 我是如何进行优化的？
3. 后续有哪些follow up？

思路一：
使用堆栈一次处理，然后再次遍历

思路二：
直接堆栈一次遍历，小技巧是先保存上一次没有消去的末尾

思路三：
动态规划
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        n = len(s)
        stack = []
        tmp = [0] * n
        for i in range(n):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                tmp[i] = 1
                tmp[stack[-1]] = 1
                stack.pop()
            else:
                stack.append(i)
        print(tmp)

        mmax = 0
        ssum = 0
        for i in range(n):
            if tmp[i] == 0:
                ssum = 0
            else:
                ssum += tmp[i]
            mmax = max(mmax, ssum)
        return mmax

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        只要相消就意味着出现了合法字符串，就要进行更新
        """
        ret = 0
        stack = [-1] # 存储下标，这里相当于保存了上一次未消去的末尾下标

        for i in range(len(s)):
            if len(stack) > 1 and s[i] == ")" and s[stack[-1]] == "(":
                stack.pop()
                ret = max(ret, i - stack[-1])
            else:
                stack.append(i)
        
        return ret