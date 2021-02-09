#!/bin/bash python
"""
40. 组合总和 II

思路：
正常DFS
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(ret, path, nums, target, i):
            """
            每个元素只有选或者不选两种情况，其实就是遍历所有子集，然后保证求和
            """
            if target == 0:
                ret.append(path[:])
            elif target > 0 and i < len(nums):
                for j in range(i, len(nums)):
                    if nums[j] in nums[i:j]:
                        continue
                    path.append(nums[j])
                    dfs(ret, path, nums, target - nums[j], j + 1)
                    path.pop()
            return
        # ===== 正式调用 =====
        ret, path = [], []
        if candidates != []:
            candidates.sort()
            dfs(ret, path, candidates, target, 0)
        return ret