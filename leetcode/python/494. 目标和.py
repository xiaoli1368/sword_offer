#!/bin/bash python
"""
494. 目标和

思路：
1. 暴力方式DFS，超时
2. 正确思路，背包问题DP
3. 优化版本：进行DP的空间压缩
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        def dfs(nums, i, target, ssum):
            """
            回溯法
            """
            if i >= len(nums):
                if ssum == target:
                    self.cnt += 1
                return
            dfs(nums, i + 1, target, ssum + nums[i])
            dfs(nums, i + 1, target, ssum - nums[i])
            return
        dfs(nums, 0, S, 0)
        return self.cnt

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        最先想到的方法就是DFS回溯，但是超时了
        思考背包问题：每个元素只有两种：+，-，因此类似01背包，注意当前元素不能不选
        dp[i][j]表示前i个元素，和为j的方法数
        dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        注意由于存在负号，导致target的取值不止为S
        此时应该表示j表示可能取到的和，因此j的合法取值必然为[-sum(nums), +sum(nums)]
        并且由于j同时依赖左侧和右侧，因此无法覆盖进行一个方向上的迭代，因此不能空间压缩
        由于j存在负值，因此索引与表示的值存在转换关系：val = j - ssum
        dp[i-1][j-curr]中应该为：dp[i-1][j - ssum - curr + ssum] = dp[i-1][j-curr]
        [1, 1, 1] 2, row = 4, col = 7 
            -3  -2  -1  0  1  2  3
        ""   0   0   0  1  0  0  0
        1    0   0   1  0  1  0  0
        1    0   1   0  2  0  1  0
        1    1   0   3  0  3  0  1
        注意初始化第一行的中间位置为1，其实从图像上可以看出每次根据curr向作用两个方向累加
        注意不能同时限制：curr <= j < col - curr，因此j只有单侧情况时，也需要进行更新

        注意不考虑越界可能出现bug，例如：[1], 2
        但是如果abs(S)==nums，则不能直接返回1，例如：[1, 0], 1，答案为2，因为有+0和-0
        """
        n, ssum = len(nums), sum(nums)
        if abs(S) > ssum:
            return 0
        row, col = n + 1, ssum * 2 + 1
        dp = [[0] * col for _ in range(row)]
        dp[0][ssum] = 1
        for i in range(1, row):
            curr = abs(nums[i - 1])
            for j in range(col):
                if j >= curr:
                    dp[i][j] += dp[i - 1][j - curr]
                if j < col - curr:
                    dp[i][j] += dp[i - 1][j + curr]
        return dp[-1][S + ssum]