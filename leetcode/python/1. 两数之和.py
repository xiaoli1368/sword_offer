#!/bin/bash python
"""
1. 两数之和

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        需要确保找到的两个元素的下标不能相等
        需要使用dict，记录val是否存在，以及所有相同val的下标
        举例:[3, 2, 4] 6
             [3, 3, 2, 4] 6
        """
        n, d = len(nums), dict()
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        for i in range(n):
            a, b = nums[i], target - nums[i]
            if b in d:
                if a != b:
                    return (d[a][0], d[b][0])
                elif len(d[a]) >= 2:
                    return (d[a][0], d[a][1])
        return None

    # ===== 优化版 =====
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        优化版，在添加当前元素的时候，先进行前向的寻找target-curr
        """
        d = dict()
        for i, val in enumerate(nums):
            if target - val in d:
                return [d[target - val], i]
            d[val] = i
        return []