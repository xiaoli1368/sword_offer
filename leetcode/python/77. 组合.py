#!/bin/bash python
"""
77. 组合

思路：
还是DFS，区别是遍历下一层的j需要额外添加一个条件，保证整体长度可以达到k
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(ret, path, n, k, i):
            """
            ret最终结果，path当前路径，i表示当前待选元素为：[i, n]
            """
            size = len(path)
            if size == k:
                ret.append(path[:])
                return
            for j in range(i, n + 2 + size - k): # j的取值应保证剩余元素总长度大于等于k
                path.append(j)
                dfs(ret, path, n, k, j + 1)
                path.pop()
            return
        
        # ===== 调用 =====
        # 特殊情况
        if n < 1 or k > n:
            return []
        ret, path = [], []
        dfs(ret, path, n, k, 1)
        return ret