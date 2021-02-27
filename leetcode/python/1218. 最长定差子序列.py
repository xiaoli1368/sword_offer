#!/bin/bash python
"""
1218. 最长定差子序列

思路：
动态规划 + hash优化
"""

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        暴力方法：二重循环，找到以每个arr[i]为首，差为diff的最长序列长度，复杂度：O(n^2)
        动态规划：dp[i]表示以arr[i]为结尾的且差为diff的等差子序列的最大长度，递推方程：
                 dp[i] = 1 + dp[arr[i]-diff], if arr[i]-diff存在于arr[0:i]，否则为1
                 为了判断是否存在，需要内部循环，整体复杂度：O(n^2) + O(n)
        优化方法：注意到arr不是有序的，在无序数组中快速找到arr[i]-diff，方法就是hash
                 同时dp状态压缩至迭代，直接一次遍历，hash解决，复杂度：O(n) + O(n)
        """
        ret, d = 0, dict()
        for num in arr:
            last = num - difference
            d[num] = 1 + (0 if last not in d else d[last])
            ret = max(ret, d[num])
        return  ret