#!/bin/bash python
"""
1122. 数组的相对排序

多种思路：
1.计数排序（借助一个哈希，生成新的结果）
2.快排（借助一个哈希，自定义比较的逻辑）
3.归并（借助一个哈希，自定义比较的逻辑）
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        对arr1中的原理建立hash，然后类似计数排序
        """
        d = dict()
        for i in arr1:
            d[i] = 1 + d.get(i, 0)

        # 按照arr2的顺序，构建结果数组
        ret = []
        for i in arr2:
            ret += [i] * d[i]
            del d[i]
        
        # 得到arr1中尚未在arr2中出现的剩下的元素（可能有重复）
        others = []
        for i in d:
            others += [i] * d[i]

        # 返回结果
        return ret + sorted(others)

	# ===== 快排 =====

    def partition(self, vec, d, l, h):
        """
        快排分区函数
        """
        start = l - 1
        for i in range(l, h):
            s1 = vec[i] in d and vec[h] in d and d[vec[i]] < d[vec[h]]
            s2 = vec[i] in d and vec[h] not in d
            s3 = vec[i] not in d and vec[h] not in d and vec[i] < vec[h]
            if s1 or s2 or s3:
                start += 1
                vec[i], vec[start] = vec[start], vec[i]
        start += 1
        vec[h], vec[start] = vec[start], vec[h]
        return start
    
    def quickSort(self, vec, d, l, h):
        """
        快排内部递归函数
        """
        if l >= h:
            return
        m = self.partition(vec, d, l, h)
        self.quickSort(vec, d, l, m - 1)
        self.quickSort(vec, d, m + 1, h)
        return

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == []:
            return []
        
        # 建立字典，key是arr2的元素，value是对应元素的索引
        d = dict()
        for index, value in enumerate(arr2):
            d[value] = index
        
        # 进行快排，输出结果
        self.quickSort(arr1, d, 0, len(arr1) - 1)
        return arr1

    # ===== 归并 =====

    def merge(self, vec, d, l, m, h):
        """
        归并合并函数
        """
        tmp = vec[l:h+1]
        p, q = l, m + 1
        for i in range(l, h + 1):
            if p <= m and q <= h:
                vp, vq = tmp[p - l], tmp[q - l]
                s1 = vp in d and vq in d and d[vp] <= d[vq]
                s2 = vp in d and vq not in d
                s3 = vp not in d and vq not in d and vp <= vq
            if p <= m and (q > h or s1 or s2 or s3):
                vec[i] = tmp[p - l]
                p += 1
            else:
                vec[i] = tmp[q - l]
                q += 1
        return

    def mergeSort(self, vec, d, l, h):
        """
        归并递归函数
        """
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(vec, d, l, m)
        self.mergeSort(vec, d, m + 1, h)
        self.merge(vec, d, l, m, h)
        return

    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        对arr1中的原理建立hash，然后类似计数排序
        """
        # 建立哈希
        d = dict()
        for index, value in enumerate(arr2):
            d[value] = index
        
        # 进行归并排序并返回结果
        self.mergeSort(arr1, d, 0, len(arr1) - 1)
        return arr1