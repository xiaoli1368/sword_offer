#!/bin/bash python
"""
377. 组合总和 Ⅳ

思路：
DFS回溯爆搜，超时了
正解是动态规划，看作爬楼梯问题，dp[i] += dp[i - nums[j]]
参考链接：https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-pa-lou-ti-wen-ti-labuladongdong-g/
参考代码：https://leetcode-cn.com/problems/combination-sum-iv/solution/377-zu-he-zong-he-ivdong-tai-gui-hua-xia-kbo0/
         https://mp.weixin.qq.com/s/PlowDsI4WMBOzf3q80AksQ
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

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        比494目标和要简单，因为不含负数
        但是问题在于不同顺序也会看作不同的组合
        由于每个元素可以无限选择，因此是一个完全背包DP
        dp[i][j]表示前i个元素，总和为j情况下的，组合个数
        dp[i][j] = dp[i - 1][j] + dp[i][j - nums[i]]
        空间压缩：dp[j] = dp[j] + dp[j - nums[i]]，注意正向遍历
        注意初始化：dp[0] = 1

        举例：[1, 2, 3], 4, 如果不考虑顺序，那就是如下
        注意到 dp[i][j] = dp[i - 1][j] + dp[i][j - nums[j]]，这种方式限定了nums[j]只能本层出现
        [1, 0, 0, 0, 0]
        [1, 1, 1, 1, 1]
        [1, 1, 2, 2, 3]
        [1, 1, 2, 3, 4]
		因此这种方法是错解，因为求的是组合，而非排列
        """
        dp = [1] + [0] * target 
        for i in range(1, 1 + len(nums)):
            curr = nums[i - 1]
            for j in range(curr, 1 + target):
                dp[j] += dp[j - curr]
        return dp[-1]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp[i][j] = dp[i - 1][j] + dp[i][j - nums[j]]
        求解排列的方法是改变遍历方式，外层遍历target，内层遍历nums，注意区别：
        [nums, target]: 求解对前nums[i]个元素构成target的组合数，由于nums[i]不可能出现在dp[i-1]中
                        因此只能是组合，不是排列
        [target, nums]: 求解对一个target，当前所有nums构成和的组合数，因此当前这一步考虑了所有nums
                        因此只能是排列，不是组合
        本题可以看作是对target的爬楼梯问题，每次可选的步长数组为nums，结果是排列数
        dp[j]表示对和为j的情况，在全部nums可选的情况下，排列数: dp[j] += dp[j - nums[i]]
        """
        dp = [1] + [0] * target 
        for j in range(1, target + 1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j - num]
        return dp[-1]