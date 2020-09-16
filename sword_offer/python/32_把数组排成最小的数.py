#!/bin/bash python3
#-*- coding:utf-8 -*-

from itertools import permutations
import functools
import time

class Solution():
    def PrintMinNumber1(self, numbers):
        """
        暴力枚举，全排列字符串遍历
        """
        if numbers == []:
            return ""
        
        ret = "".join(str(i) for i in numbers)
        for item in permutations(numbers):
            curr = "".join(str(i) for i in item)
            if ret > curr:
                ret = curr
        
        return ret


    def PrintMinNumber2(self, numbers):
        """
        第一次的方式
        """
        if numbers == []:
            return ""

        length = len(numbers)
        num = [str(x) for x in numbers]

        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if num[i] + num[j] > num[j] + num[i]: 
                    num[i], num[j] = num[j], num[i]

        return "".join(num)

    def PrintMinNumber3(self, numbers):
        """
        高效方式，冒泡排序修改版
        """
        if numbers == []:
            return ""

        num = [str(x) for x in numbers]
        for i in range(len(numbers) - 1, 0, -1):
            for j in range(0, i):
                if num[i] + num[j + 1] > num[j + 1] + num[i]: 
                    num[i], num[j + 1] = num[j + 1], num[i]
        
        return "".join(num)

    def PrintMinNumber4(self, numbers):
        """
        高效方式，stl排序
        """
        if numbers == []:
            return ""

        num = [str(x) for x in numbers]
        num.sort(key=functools.cmp_to_key(lambda x, y: x + y < y + x))
        
        return "".join(num)

    def PrintMinNumber(self, numbers):
        """
        高效方式：快速排序（待补充）
        """
        pass

    def test(self, numbers):
        """
        测试函数
        """
        func_vec = [self.PrintMinNumber1,
                    self.PrintMinNumber2,
                    self.PrintMinNumber3,
                    self.PrintMinNumber4]

        for func in func_vec:
            start = time.time()
            result = func(numbers)
            end = time.time()
            print("result: {:s}, time(us): {:>5.2f}".format(result, (end - start)*10**6))
        

def main():
    numbers = [3, 32, 321]
    numbers2 = [13, 21, 4, 41, 323, 3, 210, 4145]

    s = Solution()
    s.test(numbers)
    print("=====")
    s.test(numbers2)


if __name__ == "__main__":
    main()