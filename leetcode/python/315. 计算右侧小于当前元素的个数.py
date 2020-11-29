#!/bin/bash python
"""
315. 计算右侧小于当前元素的个数

思路：
1. 归并排序，在两个有序数组中找到右侧小于当前元素的个数
2. 建立辅助数组，indexs用来记录每个元素最初始的索引，注意indexs是随排序变化的，（如果不存在重复元素，则直接hash就行了）
3. 注意从大到小排序，同时注意归并的时候对于相等的特殊情况的处理
"""

class Solution(object):
    def merge(self, vec, counts, indexs, l, m, h):
        """
        归并合并函数
        按照从大到小的顺序
        """
        tmp_vec = vec[l:h+1]
        tmp_ind = indexs[l:h+1]
        p, q = l, m + 1
        for i in range(l, h + 1):
            if p <= m and q <= h and tmp_vec[p - l] > tmp_vec[q - l]: # 这里统计右侧小于当前元素的个数
                counts[tmp_ind[p - l]] += h - q + 1
            if p <= m and (q > h or tmp_vec[p - l] > tmp_vec[q - l]): # 注意从大到小排序，注意没有等号
                vec[i] = tmp_vec[p - l]
                indexs[i] = tmp_ind[p - l]
                p += 1
            else:
                vec[i] = tmp_vec[q - l]
                indexs[i] = tmp_ind[q - l]
                q += 1
        return
    
    def mergeSort(self, vec, counts, indexs, l, h):
        """
        归并递归函数
        """
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(vec, counts, indexs, l, m)
        self.mergeSort(vec, counts, indexs, m + 1, h)
        self.merge(vec, counts, indexs, l, m, h)
        return

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        # 新建辅助数组
        n = len(nums)
        counts = [0] * n               # 每个元素右侧更小元素的个数
        indexs = [x for x in range(n)] # 每个元素在counts中的索引
        self.mergeSort(nums, counts, indexs, 0, n - 1)
        return counts