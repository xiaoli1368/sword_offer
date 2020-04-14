#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def __init__(self):
        self.cnt = 0

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


def main():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 0]
    print(s.InversePairs(nums))


if __name__ == "__main__":
    main()