#!/bin/bash python
"""
446. 等差数列划分 II - 子序列

思路：
动态规划+内部hash
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        注意条件：数组不是有序的，等差数列长度至少为3，差diff可以为任意值
        暴力解法：DFS回溯出所有的等差路径，然后统计个数（对于n=1000，复杂度过大）
        高效解决：思考回溯中可以剪枝的优化空间

        动态规划：
        1. 感觉是二维DP，如果每个dp[i]只表示以A[i]结尾的等差子序列个数，由于缺少diff无法递推
        2. dp[i][diff]表示以A[i]结尾，且差为diff的等差数列个数，A[i] - last = diff
           其中diff没有明确的遍历序列，因此只有从A[i]-A[j]生成，时间复杂度O(n^2)
        3. dp[i]表示以A[i]结尾的等差序列信息，由于存在不同的diff，因此内部使用一个dict存储
           dict的[key,val]对应[diff,cnt]，表示以A[i]结尾的不同差的等差序列个数
           状态跳转方程： dp[i][diff] = d[j][diff], diff = A[i] - A[j]
           注意到存在bug，当初始化dp[i][diff] = 0时，后续所有结果都是0
        4. 引入长度为2的弱等差序列个数，从所有的弱等差序列中统计得到强等差序列个数
           dp[i][diff] 先更新当前这一对弱等差序列个数：dp[i][diff] += 1
           然后同步判断dp[j]是否存在diff键，如果存在，则必然再增加dp[j][diff]个弱/强等差序列
        """
        ret, n = 0, len(A)
        dp = [dict() for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = 1 + dp[i].get(diff, 0) # 统计统计len=2的弱等差序列对
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff] # 统计len>=3的弱等差序列对
                    ret += dp[j][diff] # 统计len>=3的强等差序列对
        return ret