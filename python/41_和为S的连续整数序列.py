#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def FindContinuousSequence1(self, tsum):
        """
        个人解法，利用等差序列性质，更加高效
        midTwice * num = tsum * 2
        """
        if tsum < 3:
            return []

        l = 0
        h = 0
        midTwice = 0
        num = tsum // 2 + 1
        result = []

        while num >= 2:
            if (tsum * 2) % num == 0:
                midTwice = (tsum * 2) // num
                if num % 2 == 1 and midTwice % 2 == 0:
                    l = midTwice // 2 - num // 2
                    h = midTwice // 2 + num // 2
                    self.add_vec(result, l, h)
                elif num % 2 == 0 and midTwice % 2 == 1:
                    l = midTwice // 2 - num // 2 + 1
                    h = midTwice // 2 + num // 2
                    self.add_vec(result, l, h)
            num -= 1 

        return result

    def FindContinuousSequence2(self, tsum):
        """
        个人解法究极优化版
        num:      目标序列的数量（长度），倒序遍历保证输出正序
        midTwice: 目标序列中间值的二倍
        """
        result = []
        for num in range(tsum // 2 + 1, 1, -1):
            midTwice = (tsum * 2) // num
            if num * midTwice == tsum * 2 and (num + midTwice) % 2 == 1:
                # 存在约数，且是一奇一偶
                l = midTwice // 2 - num // 2 + midTwice % 2
                h = midTwice // 2 + num // 2
                if l > 0: # 去除l为负数的情况
                    result.append(list(range(l, h + 1)))

        return result

    def FindContinuousSequence(slef, tsum):
        """
        参考解法
        """
        if tsum < 3:
            return []

        l = 1
        h = 2
        result = []

        while l <= tsum // 2 + 1:
            currSum = (l + h) * (h - l + 1) // 2
            if currSum > tsum:
                l += 1
            elif currSum < tsum:
                h += 1
            else:
                result.append(list(range(l, h + 1))) # 此时相等
                l += 1

        return result

    def add_vec(self, result, l, h):
        """
        用于添加的函数
        注意要去除l为负的情况
        """
        if l <= 0:
            return
        else:
            result.append(list(range(l, h + 1)))

    def test(self, tsum):
        """
        测试函数
        """
        func_vec = [self.FindContinuousSequence1,
                    self.FindContinuousSequence2,
                    self.FindContinuousSequence]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(tsum)
            end = time.time()
            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    s = Solution()
    s.test(0)
    s.test(15)
    s.test(77)
    s.test(100)


if __name__ == "__main__":
    main()