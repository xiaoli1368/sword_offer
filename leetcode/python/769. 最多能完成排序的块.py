#!/bin/bash python
"""
769. 最多能完成排序的块

思路:
贪心寻找最大的覆盖索引
"""

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        每个元素i，最终排序后的位置索引为i
        也就是说当前元素i，必须和索引为i的元素，在同一个块内
        因此思路类似跳跃游戏，一次遍历，更新当前块内的所需的索引的范围
        如果范围已经满足，则进行分块
        """
        cnt = maxIndex = 0
        for i in range(len(arr)):
            if maxIndex < arr[i]:
                maxIndex = arr[i]
            if maxIndex == i:
                cnt += 1
        return cnt

    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        贪心找到最右端覆盖索引后，进行分块
        """
        cnt = maxIndex = 0
        for i in range(len(arr)):
            maxIndex = max(maxIndex, arr[i])
            cnt += 1 if maxIndex == i else 0
        return cnt