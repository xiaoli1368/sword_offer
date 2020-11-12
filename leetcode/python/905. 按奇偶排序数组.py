#!/bin/bash python
"""
905. 按奇偶排序数组

常规思路：双指针
"""

class Solution(object):
    def sortArrayByParity(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if a == []:
            return []
        
        even, odd = 0, len(a) - 1
        while even < odd:
            # 找到不满足条件的even
            while even < odd and a[even] % 2 == 0:
                even += 1
            # 找到不满足条件的odd
            while odd > even and a[odd] % 2 == 1:
                odd -= 1
            # 如果二者有效则交换
            if even < odd:
                a[even], a[odd] = a[odd], a[even]
        
        return a