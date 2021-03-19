#!/bin/bash python
"""
735. 行星碰撞

思路：
正常的栈题目，关键点是while-else的方法
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for curr in asteroids:
            flag = True
            if curr <= 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < -curr:
                        stack.pop()
                    elif stack[-1] > -curr:
                        flag = False
                        break
                    else:
                        stack.pop()
                        flag = False
                        break
            if flag:
                stack.append(curr)
        return stack

    # ===== 改进版 =====
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        注意已经说了value非0
        难点是while-else的用法
        """
        stack = []
        for curr in asteroids:
            while stack and stack[-1] > 0 and curr < 0:
                if stack[-1] == -curr:
                    stack.pop()
                    break
                elif stack[-1] < -curr:
                    stack.pop()
                elif stack[-1] > -curr:
                    break
            else:
                stack.append(curr)
        return stack