#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def FindNumbersWithSum1(self, array, tsum):
        """
        暴力枚举
        """
        result = []
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == tsum:
                    return [array[i], array[j]]

        return result

    def FindNumbersWithSum2(self, array, tsum):
        """
        dict法
        """
        if array == []:
            return
        
        result = []
        dic = dict()

        for i in array:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in array:
            if dic.get(tsum - i):
                result.append(i)
                result.append(tsum - i)
                break

        return result

    def FindNumbersWithSum(self, array, tsum):
        """
        高效方式：双指针
        """
        l = 0
        h = len(array) - 1
        result = []

        while l < h:
            currSum = array[l] + array[h]
            if currSum == tsum:
                result += [array[l], array[h]]
                break
            elif currSum < tsum:
                l += 1
            elif currSum > tsum:
                h -= 1

        return result

    def test(self, array, tsum):
        """
        测试函数
        """
        func_vec = [self.FindNumbersWithSum1,
                    self.FindNumbersWithSum2,
                    self.FindNumbersWithSum]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(array, tsum)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))

        
def main():
    array = [1, 2, 3, 4, 5, 6, 7]
    array2 = [1, 1, 2, 2, 3, 5, 6, 9, 10, 12, 14, 15, 19, 20]

    s = Solution()
    s.test(array, 6)
    s.test(array2, 19)


if __name__ == "__main__":
    main()