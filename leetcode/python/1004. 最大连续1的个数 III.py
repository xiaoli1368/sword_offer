#!/bin/bash python
"""
1004. 最大连续1的个数 III

思路：
滑窗法
"""

class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        """
        滑窗法
        """
        if A == []:
            return 0
        
        n = len(A)
        l = h = ret = 0

        while h < n:
            # 移动右指针
            while h < n and (A[h] == 1 or k > 0):
                if A[h] == 0:
                    k -= 1
                h += 1
            # 更新结果
            ret = max(ret, h - l)
            # 移动左右指针
            if A[l] == 0 and l != h:
                k += 1
            l += 1
            h = max(l, h)
        return ret

    # ===== 其它方式的滑窗法 =====
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        滑窗法
        """
        # 滑动区间为(l, h]
        ret, l = 0, -1
        for h in range(len(A)):
            if A[h] == 1 or K > 0:
                # 当前区间满足要求的条件
                ret = max(ret, h - l)
                if A[h] == 0:
                    K -= 1
            elif A[h] == 0 and K == 0:
                # 移动左指针，直到遇到第一个0，与当前h处0抵消
                while l < h:
                    l += 1
                    if A[l] == 0:
                        break
        return ret