#!/bin/bash python
"""
1769. 移动所有球到每个盒子所需的最小操作数

思路：
前缀和，同时也有dp的思想了
"""

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        小球只能移动到相邻的盒子中，因此要将所有的小球移动到box[i]处
        则分两个步骤：将左侧所有移动到box[i-1], 将右侧所有移动到box[i+1], 然后再移动到box[i]
        整体上看是一个前缀和的题目，从左到右遍历依次，从右往左遍历一次，然后对应位置累加
        dp[i]表示[:i]上的小球汇总到i处的操作数，ssum表示[:i-1]的小球总和
        dp[i] = dp[i - 1] + ssum，同理右侧
            0  0  1  0  1  1
        左  0  0  0  1  2  4
        右  11 8  5  3  1  0 
        和  11 8  5  4  3  4
        """
        n = len(boxes)
        ssum, left = 0, [0] * n
        for i in range(n):
            if i >= 1:
                left[i] = left[i - 1] + ssum
            ssum += int(boxes[i])
        ssum, right, ret = 0, [0] * n, [0] * n
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                right[i] = right[i + 1] + ssum
            ssum += int(boxes[i])
            ret[i] = left[i] + right[i]
        return ret

    # ===== 优化版 =====
    def minOperations(self, boxes: str) -> List[int]:
        """
        由于dp只有相邻的左侧或者右侧有关，因此可以空间压缩: O(2n) + O(n)
        """
        n = len(boxes)
        dp = [0] * n
        left_sum = left_opt = right_sum = right_opt = 0
        for i in range(n):
            # 统计左侧
            left_opt += left_sum
            left_sum += int(boxes[i])
            dp[i] += left_opt
            # 统计右侧
            j = n - 1 - i
            right_opt += right_sum
            right_sum += int(boxes[j])
            dp[j] += right_opt
        return dp