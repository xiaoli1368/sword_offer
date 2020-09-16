#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def maxInWindows1(self, num, size):
        """
        第一次的解法，使用stl求最大值
        """
        length = len(num)
        ret = []
        
        if size > length or size <= 0:
            return ret
        
        for i in range(0, length - size + 1):
            ret.append(max(num[i: i + size]))
        
        return ret
    
    def maxInWindows2(self, num, size):
        """
        优化版
        """
        if size <= 0 or size > len(num):
            return []
        
        ret = [max(num[i:i+size]) for i in range(len(num) - size + 1)]
        return ret

    def maxInWindows3(self, num, size):
        """
        stl优化版，使用了临时变量
        """
        if size <= 0 or size > len(num):
            return []
        
        lastMax = num[0]
        popValue = num[0]
        ret = []

        for i in range(len(num) - size + 1):
            if lastMax == popValue:
                lastMax = max(num[i:i+size])
            elif lastMax < num[i + size - 1]:
                lastMax = num[i + size - 1]
            ret.append(lastMax)
            popValue = num[i]
        
        return ret
    
    def maxInWindows4(self, num, size):
        """
        使用双端队列
        """
        if size <= 0 or size > len(num):
            return []
        
        ret, deq = [], []

        for i in range(len(num)):
            while deq != [] and num[i] > num[deq[-1]]:
                deq.pop(-1)
            
            if deq != [] and deq[0] < i - size + 1:
                deq.pop(0)
            
            deq.append(i)

            if i >= size - 1:
                ret.append(num[deq[0]])
        
        return ret

    def test(self, num, size):
        """
        测试函数
        """
        func_vec = [self.maxInWindows1,
                    self.maxInWindows2,
                    self.maxInWindows3,
                    self.maxInWindows4]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(num, size)
            end = time.time()
            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))
    

def main():
    num = [2, 3, 4, 2, 6, 2, 5, 1]
    num2 = [16, 14, 12, 10, 8, 6, 4]

    s = Solution()
    s.test(num, 3)
    s.test(num2, 5)


if __name__ == "__main__":
    main()