#!/bin/bash python3
#-*- coding:utf-8 -*-

import random
import time
import heapq
from MaxHeap import MaxHeap

class Solution():
    def GetLeastNumbers_Solution1(self, tinput, k):
        """
        利用stl进行排序，第一次的方式
        """
        if tinput == [] or k > len(tinput):
            return []

        tinput.sort()
        return tinput[0:k]

    def GetLeastNumbers_Solution2(self, tinput, k):
        """
        冒泡排序，找到前k个最小值
        """
        if tinput == [] or k > len(tinput):
            return []
        
        for i in range(0, k):
            for j in range(len(tinput) - 1, i, -1):
                if tinput[j - 1] > tinput[j]:
                    tinput[j - 1], tinput[j] = tinput[j], tinput[j - 1]
        
        return tinput[0:k]

    def GetLeastNumbers_Solution3(self, data, k):
        """
        基于快排partition的方式
        """
        if data == [] or k > len(data):
            return []
        
        start = 0
        end = len(data) - 1
        index = self.Partition(data, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
            else:
                start = index + 1
            index = self.Partition(data, start, end)
        
        return sorted(data[0:k])

    def GetLeastNumbers_Solution4(self, data, k):
        """
        利用空间换取时间的方法，在数据量巨大时低效
        """
        if data == [] or k > len(data):
            return []
        
        tmp = [0] * 200000
        for i in data:
            tmp[i] += 1
        
        cnt = 0
        result = []
        for i in range(0, len(tmp)):
            while tmp[i] > 0 and cnt < k:
                result.append(i)
                tmp[i] -= 1
                cnt += 1
            if cnt == k:
                break
        
        return result

    def GetLeastNumbers_Solution(self, data, k):
        """
        使用最大堆的思想，自行编写class
        注意这里不能使用stl的最小堆，heapq
        因为无法获取当前堆的最大值，也无法pop这个最大值
        """
        if data == [] or k <= 0 or k > len(data):
            return []

        heap = MaxHeap()
        for i in range(0, len(data)):
            if i < k: # 元素 [0, k - 1] 入堆
                heap.add(data[i])
            else:     # 元素 [k, -1] 判断是否入堆
                if data[i] < heap.getMax():
                    heap.pop()
                    heap.add(data[i])
        
        result = []
        for i in range(k):
            result.append(heap.pop())
        result.reverse()

        return result

    def Partition(self, data, start, end):
        """
        快排的关键函数，分区
        """
        if data == [] or start < 0 or end >= len(data):
            return -1
        
        index = (random.sample(range(start, end + 1), 1))[0]
        data[index], data[end] = data[end], data[index]

        small = start - 1
        for index in range(start, end):
            if data[index] < data[end]:
                small += 1
                data[index], data[small] = data[small], data[index]
        
        small += 1
        data[end], data[small] = data[small], data[end]
        return small

    def test(self, tinput, k):
        """
        测试函数
        """
        func_vec = [self.GetLeastNumbers_Solution1,
                    self.GetLeastNumbers_Solution2,
                    self.GetLeastNumbers_Solution3,
                    self.GetLeastNumbers_Solution4,
                    self.GetLeastNumbers_Solution]
        for func in func_vec:
            tmp_tinput = tinput[:]
            start = time.time()
            result = func(tmp_tinput, k)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    tinput2 = random.sample(range(1000), 1000)
    tinput3 = random.sample(range(100000), 100000)

    s = Solution()
    s.test(tinput, 4)
    print("=====")
    s.test(tinput2, 7)
    print("=====")
    s.test(tinput3, 10)


if __name__ == "__main__":
    main()