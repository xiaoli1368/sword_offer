#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def multiply1(self, A):
        """
        使用除法的方式，复杂度也是O(2n)
        然而题目要求不能使用除法
        """
        if A == []:
            return []
        
        tmp = 1
        for i in A:
            tmp *= i
        
        result = []
        for i in A:
            result.append(tmp // i)
        
        return result

    def multiply2(self, A):
        """
        其它思路，两层遍历，每次使用1修改当前元素，复杂度O(n^2)
        这种方法低效
        """
        if A == []:
            return []
        
        result = []
        for i in range(len(A)):
            curr = A[i]
            A[i] = 1
            tmp = 1
            for j in A:
                tmp *= j
            A[i] = curr
            result.append(tmp)
        
        return result
    
    def multiply3(self, A):
        """
        常规思路，左右延伸计算，复杂度O(n*(n-1))
        """
        if A == []:
            return []
        
        result = []
        for i in range(len(A)):
            tmp = 1
            for j in range(len(A)):
                if j != i:
                    tmp *= A[j]
            result.append(tmp)
        
        return result

    def multiply(self, A):
        """
        高效思路，两次遍历，复杂度O(2n)
        """
        if A == []:
            return []
        
        tmp = 1
        result = []
        for i in A:
            result.append(tmp)
            tmp *= i
        
        tmp = 1
        for i in range(len(A) - 1, -1, -1):
            result[i] *= tmp
            tmp *= A[i]
        
        return result

    def test(self, A):
        """
        测试函数
        """
        func_vec = [self.multiply1,
                    self.multiply2,
                    self.multiply3,
                    self.multiply]
        for func in func_vec:
            start = time.time()
            result = func(A)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    vec = [1, 2, 3, 4, 5]
    vec2 = [8, 3, 5, 2, 2, 4, 1, 6, 7]

    s = Solution()
    s.test(vec)
    print("=====")
    s.test(vec2)


if __name__ == "__main__":
    main()