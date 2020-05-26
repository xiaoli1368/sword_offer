#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time
import heapq


class Solution():
    def __init__(self):
        self.data = []
        self.maxQueue = [] # 大顶堆，保存较小的一半
        self.minQueue = [] # 小顶堆，保存较大的一半
    
    def GetMedian1(self):
        """
        获取中位数
        """
        if self.data == []:
            return 0
        
        length = len(self.data)
        if length % 2 == 1:
            return self.data[length // 2]
        else:
            return (self.data[length // 2] + self.data[length // 2 - 1]) / 2

    def Insert1_sort(self, num):
        """
        方法一：stl排序
        """
        self.data.append(num)
        self.data.sort()
    
    def Insert1_find(self, num):
        """
        方法二：遍历寻找插入位置，保证插入有序
        """
        if self.data == []:
            self.data.append(num)
            return
        
        i = 0
        while i < len(self.data) and num > self.data[i]:
            i += 1
        
        self.data.insert(i, num)
    
    def Insert1_binSearch(self, num):
        """
        方法三：利用二分查找，插入有序
        """
        index = self.binarySearch(num)
        self.data.insert(index, num)
    
    # ===== 堆方法 =====

    def Insert2(self, num):
        """
        注意大顶堆是在小顶堆操作的基础上，push/pop取反得到的
        """
        if len(self.minQueue) != len(self.maxQueue):
            heapq.heappush(self.maxQueue, -heapq.heappushpop(self.minQueue, num))
        else:
            heapq.heappush(self.minQueue, -heapq.heappushpop(self.maxQueue, -num))
    
    def GetMedian2(self):
        """
        注意取反，+ 变为 -
        """
        if len(self.minQueue) != len(self.maxQueue):
            return self.minQueue[0]
        else:
            return (self.minQueue[0] - self.maxQueue[0]) / 2

    # ===== 工具函数 =====

    def binarySearch(self, num):
        """
        二分查找左边界
        """
        if self.data == []:
            return 0
        
        l = 0
        h = len(self.data) - 1

        while l <= h:
            m = l + (h - l) // 2
            if num >= self.data[m]:
                l = m + 1
            elif num < self.data[m]:
                h = m - 1
        
        return l
    
    def clear_data(self):
        """
        清空数据结构
        """
        self.data.clear()
        self.maxQueue.clear()
        self.minQueue.clear()
    
    def test(self, array):
        """
        测试函数
        """
        func_vec = [(self.Insert1_sort, self.GetMedian1),
                    (self.Insert1_find, self.GetMedian1),
                    (self.Insert1_binSearch, self.GetMedian1),
                    (self.Insert2, self.GetMedian2)]
        for func_pair in func_vec:
            result = []
            self.clear_data()

            start = time.time()
            for i in array:
                func_pair[0](i)
                result.append(float(func_pair[1]()))
            end = time.time()

            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))
        

def main():
    array = [1, 2, 4, 9, 6, 7, 1, 3, 3, 5, 10, 8, 3, 2, 4, 5]
    s = Solution()
    s.test(array)


if __name__ == "__main__":
    main()