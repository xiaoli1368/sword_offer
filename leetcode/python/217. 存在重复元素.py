#!/bin/bash python
"""
217. 存在重复元素
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False