#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def GetNumberOfK(self, data, k):
        """
        常规思路，简单二分查找，双边延拓
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

    def GetNumberOfK2(self, data, k):
        """
        高效思路, [k, k+1]
        """
        first = self.binarySearch(data, k)
        last = self.binarySearch(data, k + 1)
        if first == len(data) or data[first] != k:
            return 0
        else:
            return last - first

    def binarySearch(self, data, k):
        """
        变形的二分查找，找出第一个大于等于k的值的索引
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


def main():
    s = Solution()
    data = [1, 2, 3, 3, 3, 3, 4, 5, 6]

    print(s.GetNumberOfK(data, 3))
    print(s.GetNumberOfK2(data, 3))


if __name__ == "__main__":
    main()