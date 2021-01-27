#!/bin/bash python
"""
763. 划分字母区间

思路：
记录每个字母最后出现的索引即可
然后顺序依次遍历，使用[start, end]来表示当前的区间
每次都有更新end，表示当前区间的最大右边界
而一旦达到了最大右边界，则表示完成了一个分区，需要更新状态
"""

class Solution(object):
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        其实也是一个滑窗法
        需要hash统计每个字母出现的位置，只需要最大的索引即可
        """
        if s == "":
            return []
        
        n = len(s)
        d = dict()
        for i in range(n):
            d[s[i]] = i
        
        ret = []
        l = h = 0
        while h < n:
            # 移动右指针，只要没有达到最大右边界则移动
            right = d[s[l]]
            while h < n and h < right:
                right = max(right, d[s[h]])
                h += 1
            # 跳出结果，h达到了最大右边界
            ret.append(h - l + 1)
            # 更新指针
            h += 1
            l = h
        return ret

    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
		这种写法比较简练
		直接使用i遍历，但是[start, end]记录状态
        """
        ret = []
        d = dict()

        for i in range(len(s)):
            d[s[i]] = i
        
        start = end = 0
        for i in range(len(s)):
            end = max(end, d[s[i]])
            if i == end:
                ret.append(end - start + 1)
                start = i + 1

        return ret