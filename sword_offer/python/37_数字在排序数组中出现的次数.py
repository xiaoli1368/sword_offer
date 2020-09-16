#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def GetNumberOfK1(self, data, k):
        """
        暴力枚举
        """
        if data == []:
            return 0
        
        count = 0
        for i in data:
            if i == k:
                count += 1
        
        return count

    def GetNumberOfK2(self, data, k):
        """
        pythonic方式
        """
        return data.count(k)

    def GetNumberOfK3(self, data, k):
        """
        常规思路，简单二分查找，双边延拓
        第一次的方式，存在优化空间
        """
        if data == []:
            return 0

        # 二分查找是否存在
        l = 0
        h = len(data) - 1
        index = -1
        while l <= h:
            m = l + (h - l) // 2
            if data[m] > k:
                h = m - 1
            elif data[m] < k:
                l = m + 1
            elif data[m] == k:
                index = m
                break

        # 如果不存在k
        if index == -1:
            return 0

        l = index
        h = index
        while data[l] == k or data[h] == k:
            if data[l] == k:
                l -= 1
            if data[h] == k:
                h += 1
        
        return h - l - 1

    def GetNumberOfK4(self, data, k):
        """
        一次二分查找，然后双边延拓，封装优化版
        """
        if data == []:
            return 0
        
        index = self.binarySearch_one(data, k)
        if index == -1:
            return 0
        
        first = index
        last = index
        while data[first] == k:
            first -= 1
        while data[last] == k:
            last += 1
        
        return last - first - 1

    def GetNumberOfK(self, data, k):
        """
        高效思路, [k, k+1]
        """
        first = self.binarySearch(data, k)
        last = self.binarySearch(data, k + 1)
        return last - first

    def binarySearch(self, data, k):
        """
        变形的二分查找，找出第一个大于等于k的值的索引
        注意k大于全部数组时，返回的是len(data)
        """
        l = 0
        h = len(data)
        while l < h:
            m = l + (h - l) // 2
            if data[m] >= k:
                h = m
            else:
                l = m + 1
        return l

    def binarySearch_one(self, data, k):
        """
        普通二分查找，寻找单一元素索引，不存在则返回-1
        """
        l = 0
        h = len(data) - 1
        while l < h:
            m = l + (h - l) // 2
            if data[m] == k:
                return m
            elif data[m] < k:
                l = m + 1
            else:
                h = m - 1
        
        if data[l] != k:
            return -1
        
        return l

    def test(self, data, k):
        """
        测试函数
        """
        func_vec = [self.GetNumberOfK1,
                    self.GetNumberOfK2,
                    self.GetNumberOfK3,
                    self.GetNumberOfK4,
                    self.GetNumberOfK]
        for func in func_vec:
            start = time.time()
            result = func(data, k)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    data = [1, 2, 3, 3, 3, 3, 4, 5, 6]
    data2 = list(range(0, 1000))

    s = Solution()
    s.test(data, 3)
    print("=====")
    s.test(data2, 36)

if __name__ == "__main__":
    main()