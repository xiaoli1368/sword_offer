#!/bin/bash python
"""
451. 根据字符出现频率排序

思路:
1. 快排
2. 桶排序
"""

class Solution(object):
    def partition(self, vec, l, h):
        """
        快排分区函数
        """
        start = l
        for i in range(l, h):
            if vec[i][0] > vec[h][0]:
                vec[i], vec[start] = vec[start], vec[i]
                start += 1
        vec[h], vec[start] = vec[start], vec[h]
        return start

    def quickSort(self, vec, l, h):
        """
        快排，从大到小
        vec内元素的个数为：[cnt, char]
        """
        if l < h:
            m = self.partition(vec, l, h)
            self.quickSort(vec, l, m - 1)
            self.quickSort(vec, m + 1, h)

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        先使用快排方法吧
        """
        # 特殊情况
        if s == "":
            return s

        # 统计hash并生成数组, [cnt, char]
        d = dict()
        for char in s:
            d[char] = 1 + d.get(char, 0)
        vec = [(cnt, char) for char, cnt in d.items()]

        # 进行快排
        self.quickSort(vec, 0, len(vec) - 1)

        # 返回结果
        ret = ""
        for cnt, char in vec:
            ret += char * cnt
        return ret

    # ===== 桶排序 =====
    def frequencySort(self, s: str) -> str:
        """
        因为是字符，所以就对128个ASCII进行桶排序即可
        """
        # 特殊情况
        if s == "":
            return s
        
        # 统计hash并且得到最大频次
        max_cnt, d = 0, dict()
        for char in s:
            d[char] = 1 + d.get(char, 0)
            max_cnt = max(max_cnt, d[char])
        
        # 进行桶排序，下标是出现频次，元素是当前字符，可能有多个字符，所以内部还是list
        buckets = [[] for _ in range(max_cnt + 1)]
        for char, cnt in d.items():
            buckets[cnt].append(char)
        
        # 从后往前合成返回结果
        ret = ""
        for cnt in range(max_cnt, -1, -1):
            for char in buckets[cnt]:
                ret += cnt * char
        return ret