#!/bin/bash python
"""
11. 盛最多水的容器

思路：
见注释
当前区间盛水量的多少，只跟区间左右两端点的最小值有关
跟区间内部的最大值和最小值是无关的
因此可以双指针（双指针事实上是不能保证遍历所有可能的区间的，只有O(n^2)才能遍历所有）
（之所以双指针能够凑效，是因为双指针可以保证一些区间不用遍历，因为他一定不满足要求）
（这个不满足要求的条件判断，也就是双指针更新移动的关键点）
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        思路一：
        暴力方法，二重循环确定每个区间[l:r]
        直接min求最小值得高度，然后高度乘以宽度等于水量
        注意高度只和两个端点

        思路二：
        遍历每个元素，假定当前元素i为高度
        然后向两边遍历，当两边元素小于i高度则到边界，统计宽度

        思路三：
        双指针
        区间盛水量和区间宽度以及两端的较小值有关
        l,r分别从左右开始遍历
        每次移动指针则宽度必然变小，要想有机会获取更大的ret
        则必然去移动那个更小的端点，希望更小的端点高度变大
        """
        ret = 0

        """
        for l in range(len(height)):
            for r in range(l, len(height)):
                curr = (r - l) * min(height[l], height[r])
                ret = max(ret, curr)
        """

        """
        for i in range(len(height)):
            l = r = i
            while l - 1 >= 0 and height[l - 1] >= height[l]:
                l -= 1
            while r + 1 < len(height) and height[r + 1] >= height[r]:
                r += 1
            curr = (r - l) * height[i]
            ret = max(ret, curr)
        return ret
        """

        ret = 0
        l, r = 0, len(height) - 1
        while l < r:
            ret = max(ret, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ret