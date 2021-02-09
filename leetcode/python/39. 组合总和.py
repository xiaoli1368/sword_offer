#!/bin/bash python
"""
39. 组合总和

思路：
DFS，但是注意不需要for循环选取下一个元素，只是判断当前元素的选取情况，可以不选，或者选多个
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(ret, path, nums, target, i):
            """
            因为所有元素都是正整数，所以找到之后可以停止
            但是如果存在0或负数，找到之后还需继续寻找
            每个元素都有几种情况：不选，选一个，选多个
            注意这里不再使用for循环来选取后续，只看当前是否选取
            """
            if target == 0:
                ret.append(path[:])
            elif target > 0 and i < len(nums):
                dfs(ret, path, nums, target, i + 1) # 当前不选
                path.append(nums[i]) # 选取当前，但是下一层还从i开始
                dfs(ret, path, nums, target - nums[i], i)
                path.pop()
            return
        # ===== 正式调用 =====
        ret, path = [], []
        if candidates != []:
            dfs(ret, path, candidates, target, 0)
        return ret