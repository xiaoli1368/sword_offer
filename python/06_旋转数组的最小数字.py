#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def minNumberInRotateArray1(self, array):
        """
        暴力枚举
        """
        if array == []:
            return 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return array[i + 1]
        return array[0]

    def minNumberInRotateArray2(self, array):
        """
        二分查找，[l, m]区间待优化版
        """
        if array == []:
            return 0

        l = 0
        h = len(array) - 1
        while l < h:
            m = h - (h - l) // 2
            if array[l] == array[m] and array[m] == array[h]:
                return self.minNumber(array, l, h)
            elif array[l] <= array[m]:
                l = m
            else:
                # 需要特殊处理
                if l + 1 == m:
                    l += 1
                h = m
        return array[l]

    def minNumberInRotateArray(self, array):
        """
        二分查找，高效思路，优先使用[m, h]区间
        """
        length = len(array)
        if length == 0:
            return 0
        
        l = 0
        h = length - 1
        while l <= h:
            m = (l + h) // 2
            if array[l] == array[m] and array[m] == array[h]:
                return self.minNumber(array, l, h)
            elif array[m] <= array[h]:
                h = m
            else:
                l = m + 1
        return array[l]

    def minNumber(self, array, l, h):
        """
        输入一个数组，返回最小值
        """
        tmp = array[l]
        while l <= h:
            if tmp > array[l]:
                tmp = array[l]
            l += 1
        return tmp

    # ===== 以下用来测试二分查找的区间划分 =====

    def minNumberInRotateArray3(self, array):
        """
        借助二分查找，先找到最大值的索引
        返回最大值右侧的值即为最小值
        """
        if array == []:
            return 0
        
        length = len(array)
        maxIndex = self.maxIndexInRotateArray(array)

        # 需要修正
        while maxIndex < length - 1 and array[maxIndex] == array[maxIndex + 1]:
            maxIndex += 1
        
        # 输出
        return array[(maxIndex + 1) % length]

    def maxNumberInRotateArray(self, array):
        """
        二分查找，查找旋转数组中的最大值
        """
        if array == []:
            return 0
        
        l = 0
        h = len(array) - 1
        while l <= h:
            m = h - (h - l) // 2
            if array[l] == array[m] and array[m] == array[h]:
                return self.maxNumber(array, l, h)
            elif array[l] <= array[m]:
                l = m
            else:
                h = m - 1
        return array[l]

    def maxIndexInRotateArray(self, array):
        """
        二分查找，返回最大值的索引
        """
        if array == []:
            return 0
        
        l = 0
        h = len(array) - 1
        while l <= h:
            m = h - (h - l) // 2
            if array[l] == array[m] and array[m] == array[h]:
                return self.maxIndex(array, l, h)
            elif array[l] <= array[m]:
                l = m
            else:
                h = m - 1
        return l

    def maxNumber(self, array, l, h):
        """
        获取数组中的最大值，这里没有直接使用max函数
        """
        tmp = array[l]
        for i in range(l, h + 1):
            if tmp < array[i]:
                tmp = array[i]
        return tmp

    def maxIndex(slef, array, l, h):
        """
        获取数组中最大值的索引
        """
        tmp = l
        for i in range(l, h + 1):
            if tmp < array[i]:
                tmp = i
        return tmp

    def test(self, array):
        """
        测试函数
        """
        func_vec = [self.minNumberInRotateArray1,
                    self.minNumberInRotateArray2,
                    self.minNumberInRotateArray3,
                    self.minNumberInRotateArray,
                    self.maxNumberInRotateArray]
        for func in func_vec:
            # 这里可以使用引用
            print(func(array))


def main():
    array = [3, 4, 5, 1, 2]
    array2 = [1, 1, 1, 0, 1]

    s = Solution()
    s.test(array)
    print("==========")
    s.test(array2)


if __name__ == "__main__":
    main()