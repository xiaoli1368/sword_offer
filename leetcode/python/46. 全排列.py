#!/bin/bash python
"""
46. 全排列

思路：
DFS
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        因为没有重复，所以不需要进行排序
        """
        # 特殊情况
        if nums == []:
            return []
        
        def dfs(nums, ret, i):
            """
            i表示正在进行第i索引
            """
            if i >= len(nums):
                ret.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(nums, ret, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
            return

        # 正式调用
        ret = []
        dfs(nums, ret, 0)
        return ret