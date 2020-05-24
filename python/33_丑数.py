#!/bin/bash python3 
#-*- coding:utf-8 -*-

import time
import heapq

class Solution():
    def GetUglyNumber_Solution1(self, index):
        """
        暴力解法，复杂度较大
        """
        cnt = 0
        result = 0

        while cnt < index:
            result += 1
            num = result

            while num % 5 == 0:
                num //= 5
            while num % 3 == 0:
                num //= 3
            while num % 2 == 0:
                num //= 2
            
            if num == 1:
                cnt += 1

        return result

    def GetUglyNumber_Solution2(self, index):
        """
        优先级队列模拟法
        """
        if index <= 0:
            return 1
        
        result = 1
        s = set()
        mask = (2, 3, 5)
        q = []

        for i in range(1, index):
            for m in mask:
                tmp = result * m
                if tmp not in s:
                    s.add(tmp)
                    heapq.heappush(q, tmp)
            result = heapq.heappop(q)
            s.remove(result)

        return result

    def GetUglyNumber_Solution3(self, index): 
        """
        高效解法：三指针
        """
        result = index * [1]
        t2 = t3 = t5 = 0

        for i in range(1, index):
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5)
            if result[i] == 2 * result[t2]:
                t2 += 1
            if result[i] == 3 * result[t3]:
                t3 += 1
            if result[i] == 5 * result[t5]:
                t5 += 1
        
        return result[-1]

    def test(self, index):
        """
        测试函数
        """
        func_vec = [self.GetUglyNumber_Solution1,
                    self.GetUglyNumber_Solution2,
                    self.GetUglyNumber_Solution3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(index)
            end = time.time()
            print("number: {:d}, result: {:d}, time(us): {:>5.2f}".format(index, result, (end - start)*10**6))


def main():
    s = Solution()
    for i in range(1, 801, 100):
        s.test(i)


if __name__ == "__main__":
    main()