#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def FindGreatestSumOfSubArray1(self, array):
        """
        暴力枚举，双层循环，借助stl排序
        """
        if array == []:
            return 0
        
        ret = []
        for i in range(0, len(array)):
            tmp = array[i]
            ret.append(tmp)
            for j in range(i + 1, len(array)):
                tmp += array[j]
                ret.append(tmp)
        
        ret.sort()
        return ret[-1]

    def FindGreatestSumOfSubArray2(self, array):
        """
        暴力枚举，双层循环
        """
        if array == []:
            return
        
        curr_max = array[0]
        for i in range(0, len(array)):
            curr_sum = array[i]
            for j in range(i + 1, len(array)):
                curr_sum += array[j]
                if curr_max < curr_sum:
                    curr_max = curr_sum
        
        return curr_max
    
    def FindGreatestSumOfSubArray3(self, array):
        """
        第一次解法，动态规划
        """
        if array == []:
            return 0

        length = len(array)
        if length == 1:
            return array[0]

        curr_sum = array[0]
        curr_max = array[0]

        for i in range(1, length):
            if curr_sum >= 0:
                curr_sum += array[i]
            else:
                curr_sum = array[i]

            if curr_sum > curr_max:
                curr_max = curr_sum

        return curr_max
    
    def FindGreatestSumOfSubArray(self, array):
        """
        动态规划，高效
        """
        if array == []:
            return 0
        
        curr_sum = -1
        curr_max = array[0]
        for i in array:
            curr_sum = i + (curr_sum if curr_sum > 0 else 0)
            curr_max = max(curr_max, curr_sum)
        
        return curr_max

    def test(self, array):
        """
        测试函数
        """
        func_vec = [self.FindGreatestSumOfSubArray1,
                    self.FindGreatestSumOfSubArray2,
                    self.FindGreatestSumOfSubArray3,
                    self.FindGreatestSumOfSubArray]
        for func in func_vec:
            start = time.time()
            result = func(array)
            end = time.time()
            print("result: {:d}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    array = [6, -3, -2, 7, -15, 1, 2, 2]
    s = Solution()
    s.test(array)


if __name__ == "__main__":
    main()