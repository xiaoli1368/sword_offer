#!/bin/bash python
"""
216. 组合总和 III

思路：
常规DFS
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(ret, path, n, k, i):
            """
            n表示剩余的求和点，i表示剩下的取值范围[i, 9]
            从前向后取，最终每个成立的结果都是有序的
            由于每种结合不含重复的数字，因此k最大为9
            [1, 2, 3, 4, 5, 6, 7, 8, 9]，每个元素不取或者取一个
            """
            if n == 0 and len(path) == k:
                ret.append(path[:])
            elif n > 0 and i <= 9:
                for j in range(i, 10):
                    path.append(j)
                    dfs(ret, path, n - j, k, j + 1)
                    path.pop()
            return
        # ===== 正式调用 =====
        ret, path = [], []
        if k > 0 and 1 <= n <= 9 * k:
            dfs(ret, path, n, k, 1)
        return ret