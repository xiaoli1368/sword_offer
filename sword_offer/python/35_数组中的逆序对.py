#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import random

class Solution():
    def __init__(self):
        self.cnt = 0
    
    def InversePairs1(self, nums):
        """
        暴力枚举
        """
        if nums == []:
            return 0
        
        count = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
        
        return count

    def InversePairs(self, nums):
        """
        注意，这种方式没有对外界的nums进行保护
        """
        if nums == []:
            return 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt % 1000000007
        
    def mergeSort(self, nums, l, h):
        if l >= h:
            return
        m = l + (h - l) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, h)
        self.merge(nums, l, m, h)

    def merge(self, nums, l, m, h):
        i = l
        j = m + 1
        k = l
        tmp = []
        while i <= m or j <= h:
            if i > m: # 前数组已经遍历完
                tmp.append(nums[j])
                j += 1
            elif j > h or nums[i] <= nums[j]: # 后数组已经遍历完，或则　前 < 后
                tmp.append(nums[i])
                i += 1
            else: # 前 > 后，符合逆序对的定义
                tmp.append(nums[j])
                j += 1
                self.cnt += m - i + 1
            k += 1

        # 拷贝数组
        nums[l:h+1] = tmp[:]
    
    def merge2(self, nums, l, m, h):
        """
        [NOTE](lzc/2020/10/07):改进版归并合并函数
        """
        tmp = nums[l:h+1]
        p, q = l, m + 1
        for i in range(l, h + 1):
            if p <= m and q <= h and tmp[p - l] > tmp[q - l]:
                self.cnt += m - q + 1
            if p <= m and (q > h or tmp[p - l] <= tmp[q - l]):
                nums[i] = tmp[p - l]
                p += 1
            else:
                nums[i] = tmp[q - l]
                q += 1
        return

    def test(self, nums):
        """
        测试函数
        """
        func_vec = [self.InversePairs1, self.InversePairs]
        for func in func_vec:
            # 必要的处理，防止后续调用影响
            tmp_nums = nums[:]
            self.cnt = 0

            # 正式调用
            start = time.time()
            result = func(tmp_nums)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 0]
    nums2 = random.sample(range(100), 100) # 这种方式生成0-100的乱序

    s = Solution()
    s.test(nums)
    print("=====")
    s.test(nums2)


if __name__ == "__main__":
    main()