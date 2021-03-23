#!/bin/bash python
"""
218. 天际线问题

思路：
堆
没啥思路，战略放弃
"""

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        由于原始数据已经按照x排序
        每一个建筑物都会提供两条竖线，每个竖线有两种类型：建筑物的左边界，或者右边界
        每条竖线有两个端点：上端点，以及下端点，所有的竖线共分三种情况：
        1. 完全暴露的：需要添加，左边界添加上端点，右边界添加下端点
        2. 完全覆盖的：不需要添加
        3. 部分覆盖的：需要添加，左边界添加上端点，右边界添加下端点（需要被截断）

        1) 什么时候竖线完全暴露？左侧没有未配对的左边界时
        2) 什么时候竖线完全覆盖？左右两端存在配对的更高的竖线
        3) 什么时候竖线部分覆盖？左右两端存在配对的更低的竖线

        暴力解法：将n个建筑物处理为2n个竖线，每个竖线向左右遍历，判断覆盖情况
        其它解法：从左到右遍历，依次扫描，保存[index, height]的最大堆
        """
        pass

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        参考链接：
        https://leetcode-cn.com/problems/the-skyline-problem/solution/sao-miao-xian-wei-hu-zui-da-dui-by-user5707f/
        """
        if buildings == []:
            return []
        
        # 左端点通过负数高度来标识，同时适用于标准库中的小顶堆转换为大顶堆
        # 将扫描线中的关键点按照points的前两个元素x, y来排序
        points = []
        for l, r, h in buildings:
            points.append((l, -h, r))
            points.append((r, h, 0))
        points.sort()

        # 初始值，[0初始高度， float('inf')对应无穷右边界]
        res, height_heap = [[0, 0]], [[0, float('inf')]]    
        for x, h, r in points:
            while x >= height_heap[0][1]:
                heapq.heappop(height_heap) # 关键点：清除扫过的高楼
            if h < 0:
                heapq.heappush(height_heap, [h, r]) # 左端点入堆
            if res[-1][1] != -height_heap[0][0]:
                res.append([x, -height_heap[0][0]]) # 当前最大高度变化，则是转折点
        return res[1:]