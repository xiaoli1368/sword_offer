#!/bin/bash python
"""
5691. 通过最少操作次数使数组的和相等

思路：
贪心 + 哈希
"""

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        1. 是否有解？需要明确两个数组的取值区间是否有交集
        2. 在有解的情况下，获取两数组各自的sum以及差diff，并且交换顺序保证 sum1 < sum2
        3. 此时使用贪心的策略，优先改变可以提供较大curr_diff的元素
        4. 因此先需要生成[key:value] = [curr_diff:cnt]的哈希表，然后贪心来减少diff
           注意nums1与num2的key键获取方式不同，前者增大curr_diff，后者减少curr_diff
        """
        # 特殊情况
        len1, len2 = len(nums1), len(nums2)
        if max(len1, len2) > 6 * min(len1, len2):
            return -1
        
        # 获取sum和diff，并且交换顺序，保证sum1<sum2
        sum1, sum2 = sum(nums1), sum(nums2)
        diff = abs(sum1 - sum2)
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
        
        # 获取dict，[key:value] = [curr_diff:cnt]
        d = dict.fromkeys(range(1, 6), 0)
        for val in nums1:
            if val <= 5:
                curr_diff = 6 - val
                d[curr_diff] += 1
        for val in nums2:
            if val >= 2:
                curr_diff = val - 1
                d[curr_diff] += 1
        
        # 贪心获取最少次数
        cnt, curr_diff = 0, 5
        while diff > 0:
            if d[curr_diff] > 0:
                cnt += 1
                diff -= curr_diff
                d[curr_diff] -= 1
            else:
                curr_diff -= 1
        return cnt