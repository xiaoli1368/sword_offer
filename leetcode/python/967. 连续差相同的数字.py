#!/bin/bash python
"""
967. 连续差相同的数字

思路：
标准的DFS
"""

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        思路：
        1. 暴力方法：顺序遍历0到最大的n位数，然后依次拆分判断绝对差是否为k
        2. 其它方式：回溯法，依次选择满足条件的元素
        """
        # 特殊情况
        if n < 2 or k < 0:
            return []
        
        def dfs(ret, n, k, num, last, i):
            """
            回溯法
            ret, n, k, num, last, i: 最终结果，总长度，要求的差，当前的数字，上一位数字，当前长度
            """
            if i > n: # 满足长度后返回
                ret.append(num)
            elif i == 1: # 第一位数字随便选取
                for j in range(1, 10):
                    dfs(ret, n, k, j, j, i + 1)
            else: # 非第一位，只有两种可能+k/-k
                if last + k < 10:
                    j = last + k
                    dfs(ret, n, k, num * 10 + j, j, i + 1)
                if last - k >= 0 and k != 0: # 防止+k/-k重复
                    j = last - k
                    dfs(ret, n, k, num * 10 + j, j, i + 1)
            return
        
        # 正式调用
        ret = []
        dfs(ret, n, k, 0, 0, 1)
        return ret

    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        思路：
        1. 暴力方法：顺序遍历0到最大的n位数，然后依次拆分判断绝对差是否为k
        2. 其它方式：回溯法，依次选择满足条件的元素
        """
        # 特殊情况
        if n < 2 or k < 0:
            return []
        
        def dfs(ret, n, k, num, last, i):
            """
            回溯法
            从第二位开始
            ret, n, k, num, last, i: 最终结果，总长度，要求的差，当前的数字，上一位数字，当前长度
            """
            # 满足长度后直接返回
            if i > n:
                ret.append(num)
                return
            # 否则生成下一层所有可访问元素，依次DFS
            # 非第一位，只有两种可能+k/-k，使用set防止重复
            nextNum = range(1, 10) if i == 1 else set([last + k, last - k])
            for j in nextNum:
                if 0 <= j <= 9:
                    dfs(ret, n, k, num * 10 + j, j, i + 1)
            return
        
        # 正式调用
        ret = []
        dfs(ret, n, k, 0, 0, 1)
        return ret