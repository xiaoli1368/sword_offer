#!/bin/bash python
"""
78. 子集

思路：
DFS
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        每个元素都有两种可能，添加或者不添加
        每种当前的遍历状态，只有遍历越界时才退出
        """
        # 特殊情况
        if nums == []:
            return []
        
        def dfs(nums, ret, path, i):
            """
            i表示当前正在遍历的索引
            """
            # 越界保存退出
            if i >= len(nums):
                ret.append(path[:])
                return
            # 跳过当前元素
            dfs(nums, ret, path, i + 1)
            # 选取当前元素
            path.append(nums[i])
            dfs(nums, ret, path, i + 1)
            path.pop()
            return
        
        # 正式调用
        ret, path = [], []
        dfs(nums, ret, path, 0)
        return ret
	
	# ===== 更加兼容排列的写法 =====
    def dfs(self, ret, path, nums, i):
        """
        先append的思路
        只要进入dfs的path就是有效path
        每一次都要从nums[i:]中选取下一个有效元素添加入Path，然后进入下一层
        """
        ret.append(path[:])
        if i >= len(nums):
            return
        for j in range(i, len(nums)):
            path.append(nums[j])
            self.dfs(ret, path, nums, j + 1) # 注意这里是j+1
            path.pop()
        return

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret, path = [], []
        if nums != []:
            self.dfs(ret, path, nums, 0)
        return ret