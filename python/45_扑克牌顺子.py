#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def IsContinuous1(self, numbers):
        """
        第一次解法，一次遍历，利用保存的信息判断
        这个版本有误，不能处理含有重复的情况
        修改版见下
        """
        if len(numbers) != 5:
            return False
        
        nmin = 14
        nmax = 0
        zero_cnt = numbers.count(0)

        for i in numbers:
            if i == 0:
                continue
            if i < nmin:
                nmin = i
            if i > nmax:
                nmax = i
        
        if nmin < 0 or nmax > 13:
            return False

        if zero_cnt == 4 or (nmax - nmin <= 4 and nmax != nmin):
            return True
        else:
            return False

    def IsContinuous2(self, numbers):
        """
        个人解法修改版，pythonic
        """
        if len(numbers) != 5:
            return False

        # 去除非0重复
        for i in numbers:
            if i != 0 and numbers.count(i) > 1:
                return False 
        
        tmp_no_zero = [i for i in numbers if i != 0]
        return max(numbers) - min(tmp_no_zero) <= 4

    def IsContinuous(self, numbers):
        """
        参考答案，癞子补全法
        """
        if len(numbers) != 5:
            return False
        
        numbers.sort()
        cnt = numbers.count(0)

        for i in range(cnt, len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                return False
            cnt -= numbers[i + 1] - numbers[i] - 1
        
        return cnt >= 0

    def test(self, numbers):
        """
        测试函数
        """
        func_vec = [self.IsContinuous1,
                    self.IsContinuous2,
                    self.IsContinuous]
        print("=====")
        for func in func_vec:
            tmp_numbers = numbers[:]
            start = time.time()
            result = func(tmp_numbers)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    numbers = [[1, 2, 3, 4, 5],
               [1, 1, 1, 1, 1],
               [1, 3, 0, 5, 0],
               [1, 1, 0, 0, 5],
               [3, 5, 2, 0, 0],
               [0, 0, 0, 0, 9],
               [3, 9, 1, 0, 0],
               [9, 4, 2, 5, 6]]
    
    s = Solution()
    for nums in numbers:
        s.test(nums)


if __name__ == "__main__":
    main()