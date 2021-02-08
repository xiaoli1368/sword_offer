#!/bin/bash python
"""
90. 子集 II

思路：
DFS，关键是去重，这里需要知道path数组中上一个有效数组的索引
"""

class Solution:
    def dfs(self, ret, path, nums, last, i):
        """
        dfs
        last表示path中最后一个元素的索引
        """
        if i >= len(nums):
            ret.append(path[:])
            return
        self.dfs(ret, path, nums, last, i + 1)
        # 只要不重复时才添加
        if nums[i] not in nums[last+1:i]:
            path.append(nums[i])
            self.dfs(ret, path, nums, i, i + 1)
            path.pop()
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        """
        ret, path = [], []
        if nums != []:
            nums.sort()
            self.dfs(ret, path, nums, -1, 0)
        return ret
	
	# ===== 与排列兼容的方式 =====
    def dfs(self, ret, path, nums, i):
        """
        dfs
        """
        ret.append(path[:])
        if i >= len(nums):
            return
        for j in range(i, len(nums)):
            # 这里与排序使用同样的方法去重
            if nums[j] in nums[i:j]:
                continue
            path.append(nums[j])
            self.dfs(ret, path, nums, j + 1)
            path.pop()
        return

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret, path = [], []
        if nums != []:
            nums.sort()
            self.dfs(ret, path, nums, 0)
        return ret