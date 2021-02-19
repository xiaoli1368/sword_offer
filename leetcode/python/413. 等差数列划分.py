#!/bin/bash python
"""
413. 等差数列划分

思路：
动态规划
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        划重点：
        求等差子数组的个数
        1. 等差的要求，差可以为0，长度至少为3
        2. 子数组的要求，子数组内部元素必须相邻，也就是说限定[begin, end]后该子数组就确定了
        3. 当前位置要想加入子数组，则要保证差值与之前相同
        状态递推方程：
        1. 定义dp[i]表示以索引i为结尾的等差子数组的个数
        2. dp[i] = dp[i - 1] + 1 if 等差
                 = 0 if 不等差
        3. ret = sum(dp[i])
        """
        ret = 0
        dp = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] + A[i - 2] == 2 * A[i - 1]:
                dp[i] = dp[i - 1] + 1
            ret += dp[i]
        return ret