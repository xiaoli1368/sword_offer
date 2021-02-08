#!/bin/bash python
"""
47. 全排列 II

思路：
DFS，关键是如何去重，这里首先思考为什么会重复？
因此在选择索引为i的元素时，当前所选取的元素，之前已经使用过了
因此可以在循环选取之前，使用动态hash，判断当前元素之前是否已经使用过了
例如：[1, 1, 2, 2, 3, 3]
-----------> i
-----------> j -----> j
-----------> j k ---> j
当选择第i=2个元素时，待选元素遍历区间为[i:]，索引为j
当选定一个特定元素j=k时，可以发现k不能选取第二个2，因为之前出现过了
也就是 nums[j] not in nums[i:j]
"""

class Solution(object):
    def dfs(self, ret, nums, i):
        """
        DFS
        """
        if i >= len(nums):
            ret.append(nums[:])
            return
        for j in range(i, len(nums)):
            # 如果之前出现过相同的元素则跳过
            # 注意这里，nums[j]是否在nums[i:j]中出现过
            if nums[j] in nums[i:j]:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            self.dfs(ret, nums, i + 1)
            nums[i], nums[j] = nums[j], nums[i]
        return

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums != []:
            nums.sort()
            self.dfs(ret, nums, 0)
        return ret
