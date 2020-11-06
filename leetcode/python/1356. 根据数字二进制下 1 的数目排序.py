#!/bin/bash python
"""
1356. 根据数字二进制下 1 的数目排序

两种思路：
一是直接借助sort()直接给定自拟的排序接口
二是自行编写自定义的快排
"""

class Solution(object):
    def getOnes(self, n):
        """
        获取数字n中二进制位为1的数目
        """
        ret = 0
        while n > 0:
            ret += 1
            n &= n - 1
        return ret

    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if arr == []:
            return []
        
        ret = sorted(arr, key=lambda x : (self.getOnes(x), x))
        return ret
	
	# ===== 第二种方法 =====
    def partition(self, vec, ones, l, h):
        """
        快排分区函数
        """
        start = l - 1
        for i in range(l, h):
            if ones[i] < ones[h] or (ones[i] == ones[h] and vec[i] < vec[h]):
                start += 1
                ones[i], ones[start] = ones[start], ones[i]
                vec[i], vec[start] = vec[start], vec[i]
        start += 1
        ones[h], ones[start] = ones[start], ones[h]
        vec[h], vec[start] = vec[start], vec[h]
        return start

    def _quickSort(self, vec, ones, l, h):
        """
        快排内部递归函数
        """
        if l >= h:
            return
        m = self.partition(vec, ones, l, h)
        self._quickSort(vec, ones, l, m - 1)
        self._quickSort(vec, ones, m + 1, h)
        return

    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if arr == []:
            return []
			
        # 生成对应的1的个数矩阵
        ones = []
        for num in arr:
            cnt = 0
            while num:
                cnt += 1
                num &= num - 1
            ones.append(cnt)

        # 调用快排
        self._quickSort(arr, ones, 0, len(arr) - 1)
        return arr