#!/bin/bash python
"""
922. 按奇偶排序数组 II

理一下思路：

奇偶排序，全部奇数在前，全部偶数在后，内部保持顺序
思路1：二重循环冒泡法，时间O(n^2)，空间O(1)
思路2：新数组+两次遍历，时间O(n)，空间O(n)

奇偶排序，全部奇数在前，全部偶数在后，内部顺序任意（注意这里）
思路1：二重循环冒泡法，时间O(n^2)，空间O(1)
思路2：新数组+两次遍历，时间O(n)，空间O(n)
思路3：双指针左右遍历，时间O(n)，空间O(1)，这种方式会导致内部乱序（不稳定）

奇偶排序，偶数和奇数交替排布，保证测试数据有效，内部顺序任意（注意这里，就是本题）
思路1：二重循环，时间O(n^2)，空间O(1)
思路2：新数组+两次遍历，时间O(n)，空间O(n)
思路3：双指针同时从左到右遍历，时间O(n)，空间O(1)，无法保持有序，如246135

拓展排序，要求数组内元素a[i]与i具有相同的mod3值，内部顺序任意
思路1：新数组+3次遍历，时间O(n)，空间O(n)
思路2：三指针同时从左向右遍历，[m0, m1, m2]，交换的时候存在多种情况
"""

class Solution(object):
    def sortArrayByParityII(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if a == [] or len(a) % 2 != 0:
            return a
        # 二重循环
        for i in range(len(a)):
            if a[i] % 2 == i % 2: # 满足奇偶性质
                continue
            for j in range(i + 1, len(a)): # 找到下一个同i特性的值并交换
                if a[j] % 2 == i % 2:
                    a[i], a[j] = a[j], a[i]
                    break
        return a
    
    def sortArrayByParityII(self, a):
        """
        使用额外数组
        """
        if a == [] or len(a) % 2 != 0:
            return []
        ret = [0] * len(a)
        even, odd = 1, len(a) - 1
        for i in a:
            if i % 2 == 0:
                ret[even] = i
                even += 2
            else:
                ret[odd] = i
                odd += 2
        return ret

    def sortArrayByParityII(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if a == [] or len(a) % 2 != 0:
            return a
        n = len(a)
        even, odd = 0, 1
        while even < n and odd < n:
            # 偶指针找到当前位置为奇数的情况
            while even < n and a[even] % 2 == 0:
                even += 2
            # 奇指针找到当前位置为偶数的情况
            while odd < n and a[odd] % 2 == 1:
                odd += 2
            # 如果都没有越界则交换
            if even < n and odd < n:
                a[even], a[odd] = a[odd], a[even]
        return a