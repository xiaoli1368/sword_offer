#!/bin/bash python
"""
870. 优势洗牌

思路：
见注释
"""

class Solution(object):
    def binarySearch(self, vec, target):
        """
        在vec中寻找一个大于target的最小值的索引，如果不存在则返回最小值
        """
        l, h = 0, len(vec) - 1
        while l < h:
            m = (l + h) // 2
            if vec[m] > target:
                h = m
            else:
                l = m + 1
        return l if vec[l] > target else 0

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        这道题非常像是《田忌赛马》
        如果要求最大胜出个数，方法是：二者分别排序，然后依次贪心遍历找最小的胜出配对
        如果要求优势最大化的排列，那么B就不能改动
        思路是：先对A排序，然后对B的每个位置，贪心的寻找最小的更大值，可以每个都进行二分
        复杂度：O(nlogn)，注意对A数组存在pop，会耗费额外的复杂度
        """
        A.sort()
        ret = []
        for target in B:
            index = self.binarySearch(A, target)
            ret.append(A.pop(index))
        return ret