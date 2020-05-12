#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def FindNumsAppearOnce1(self, array):
        """
        Pythonic方式
        """
        if array == []:
            return []
        
        result = []
        for i in array:
            if array.count(i) == 1:
                result.append(i)
        
        return result

    def FindNumsAppearOnce2(self, array):
        """
        Pythonic方式，优化版
        """
        if array == []:
            return []
        
        return [i for i in array if array.count(i) == 1]

    def FindNumsAppearOnce3(self, array):
        """
        dict法
        """
        if array == []:
            return []
        
        dic = dict()
        for i in array:
            if not dic.get(i):
                dic[i] = 1
            else:
                dic[i] += 1
        
        return [i for i in array if dic[i] == 1]

    def FindNumsAppearOnce(self, array):
        """
        高效解法
        """
        if array == []:
            return []
        
        diff = 0
        for i in array:
            diff ^= i
        #diff &= (diff & 0xffffffff)
        diff &= -diff

        result = [0, 0]
        for i in array:
            if (i & diff) == 0: 
                result[0] ^= i
            else:
                result[1] ^= i
        return result

    def test(self, array):
        """
        测试函数
        """
        func_vec = [self.FindNumsAppearOnce1,
                    self.FindNumsAppearOnce2,
                    self.FindNumsAppearOnce3,
                    self.FindNumsAppearOnce]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(array)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    array2 = [1, 2]

    s = Solution()
    s.test(array)
    s.test(array2)


if __name__ == "__main__":
    main()