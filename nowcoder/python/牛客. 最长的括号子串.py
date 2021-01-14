#!/bin/bash python
"""
牛客. 最长的括号子串

思路：
这道题在leetcode上做过，但是第二次做还是没想到最优解
两种思路：1. 暴力标记法。2. 栈操作。3. 动态规划。
"""

#
# 
# @param s string字符串 
# @return int整型
#
class Solution:
    def longestValidParentheses(self , s):
        # write code here
        if s == "":
            return 0
        
        # 暴力法，使用堆栈将每个可以配对的括号位置设置为1，然后统计最长连1长度 
        n = len(s)
        vec = [0] * n
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")" and stack != [] and s[stack[-1]] == "(":
                vec[i] = 1
                vec[stack.pop()] = 1
        # 统计长度
        ret = 0
        l = h = 0 # [l, h)
        while h < n:
            # 移动左指针直到找到第一个1
            l = h
            while l < n and vec[l] == 0:
                l += 1
            h = l
            # 移动右指针，直到不是1
            while h < n and vec[h] == 1:
                h += 1
            # 更新结果
            ret = max(ret, h - l)
        return ret

    def longestValidParentheses(self , s):
        # write code here
        # 堆栈法
        # 需要解决的一个问题就是，如何保证当前串和之前串是相连的
        # 改变当前子串计算长度的方式，当前子串为：[l, h]
        # 以前的计算方式为：h - l + 1, 改为：h - last
        # last表示上一个"("的位置，因为"("必然不是一个子串的开头
        if s == []:
            return 0
        
        # 堆栈记录所有的不能匹配的位置下标，注意到"(",")"都有可能无法完成匹配
        # 预先存储-1
        ret = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == ")" and stack != [] and stack[-1] >= 0 and s[stack[-1]] == "(":
                stack.pop()
                ret = max(ret, i - stack[-1])
            else:
                stack.append(i)
        return ret