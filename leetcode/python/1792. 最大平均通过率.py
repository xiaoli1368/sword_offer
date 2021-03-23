#!/bin/bash python
"""
1792. 最大平均通过率

思路：
堆
"""

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        如何保证平均通过率最大？由于班级个数是确定的，因此只要通过率总和增大就可以
        也就是说对n个班级来分配m个好学生，保证最终的通过率总和最大，如何分配？
        可以考虑一个一个来进行分配，每次分配学生时，考虑分配到哪个版本可以获取最大的
        当前一次的通过率提升
        从整体来看是一个大顶堆，对[a, b]班级，当前的通过率提升为(a+1)/(b+1) - (a/b)
        整理后可得，[a, b] -> (b - a) / (b^2 + b) 大顶堆
                   [a, b] -> (a - b) / (b^2 + b) 小顶堆
        """
        # 初始化
        ret, q = 0, []
        func = lambda a, b : (a - b) / (b**2 + b)

        # 建立小顶堆，内部元素为：[func, a, b]
        for a, b in classes:
            ret += a / b
            q.append((func(a, b), a, b))
        heapq.heapify(q)

        # 每次选取最大提升来分配学生
        for _ in range(extraStudents):
            improve, a, b = heapq.heappop(q)
            ret += -improve
            heapq.heappush(q, (func(a + 1, b + 1), a + 1, b + 1))
        return ret / len(classes)