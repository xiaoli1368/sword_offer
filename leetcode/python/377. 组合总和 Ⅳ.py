#!/bin/bash python
"""
377. 组合总和 Ⅳ

思路：
DFS回溯爆搜，超时了
正解是动态规划，看作爬楼梯问题，dp[i] += dp[i - nums[j]]
参考链接：https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-pa-lou-ti-wen-ti-labuladongdong-g/
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(ret, nums, target):
            """
            注意到此时每个元素的使用次数是无限
            并且不同的顺序被视为不同的组合
            一种简单暴力的方式，就是使用set来去重
            for循环的方式可以保证对nums从前往后选取
            但是答案允许选取某个之前的元素，因此需要改变方式
            当target > 0 时进行dfs，每次选择nums中的一个
            """
            if target == 0:
                ret[0] += 1
            elif target > 0:
                for i in nums:
                    dfs(ret, nums, target - i)
            return
        # ===== 正式调用 =====
        ret = [0]
        if nums != [] and target > 0:
            dfs(ret, nums, target)
        return ret[0]