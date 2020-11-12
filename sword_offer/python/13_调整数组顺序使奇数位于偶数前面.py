#!bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def reOrderArray1(self, array):
        """
        两个额外数组，一次遍历，使用stl完成拼接
        """
        tmp1 = []
        tmp2 = []
        for i in array:
            if i % 2 == 1:
                tmp1.append(i)
            else:
                tmp2.append(i)
        return tmp1 + tmp2

    def reOrderArray2(self, array):
        """
        一个数组，两次遍历
        首先插入奇数，然后插入偶数
        """
        tmp = []
        for i in array:
            if i % 2 == 1:
                tmp.append(i)
        for i in array:
            if i % 2 == 0:
                tmp.append(i)
        return tmp

    def reOrderArray3(self, array):
        """
        一个数组，两次遍历
        首先确定奇偶分界索引，之后分别插入
        """
        if array == []:
            return
        
        odd_index = 0
        even_index = 0
        tmp = [0] * len(array)

        for i in array:
            if i % 2 == 1:
                even_index += 1

        for i in array:
            if i % 2 == 1:
                tmp[odd_index] = i
                odd_index += 1
            else:
                tmp[even_index] = i
                even_index += 1
        
        return tmp

    def reOrderArray4(self, array):
        """
        二重循环，冒泡方式，将偶数放到最右边
        未优化，时间复杂度较大
        """
        for i in range(len(array)):
            for j in range(len(array)-1):
                if array[j] % 2 == 0 and array[j+1] % 2 == 1:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def reOrderArray5(self, array):
        """
        二重循环，冒泡方式，部分优化
        依次需要将当前偶数放到最右侧，次右侧...
        """
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] % 2 == 0 and array[j + 1] % 2 == 1:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def reOrderArray6(self, array):
        """
        pythonic方式
        """
        return sorted(array, key=lambda x: x%2, reverse=True)

    def reOrderArray7(self, array):
        """
        高效方式，类似插入排序，不借助额外数组，两层遍历
        """
        if array == []:
            return array
        
        for i in range(len(array)):
            if array[i] % 2 == 1:
                # 确定上一个奇数的位置
                # 寻找相邻两个奇数之间的偶数段
                # [last_odd], [last_odd + 1, i - 1], [i]
                # 交换[i]与[last_odd + 1, i - 1]
                curr_odd = array[i]
                last_odd = i - 1

                while last_odd >= 0 and array[last_odd] % 2 == 0:
                    last_odd -= 1
                
                for j in range(i - 1, last_odd, -1):
                    array[j + 1] = array[j]
                array[last_odd + 1] = curr_odd
        
        return array
    
    def reOrderArray(self, array):
        """
        更加高效的方式，双指针（但是这种方式破坏了原来的内部顺序）
        """
        if array == []:
            return array
        
        odd, even = 0, len(array) - 1
        while odd < even:
            # 找到指向偶数的odd指针
            while odd < even and array[odd] % 2 == 1:
                odd += 1
            # 找到指向奇数的even指针
            while odd < even and array[even] % 2 == 0:
                even -= 1
            # 如果不越界则交换
            if odd < even:
                array[odd], array[even] = array[even], array[odd]
        
        return array

    def test(self, array):
        """
        测试函数
        """
        func_vec = [self.reOrderArray1,
                    self.reOrderArray2,
                    self.reOrderArray3,
                    self.reOrderArray4,
                    self.reOrderArray5,
                    self.reOrderArray6,
                    self.reOrderArray7,
                    self.reOrderArray]
        for func in func_vec:
            # 这里需要建立临时的空间
            tmp_array = array[:]
            start = time.time()
            result = func(tmp_array)
            end = time.time()
            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))

def main():
    array = [1, 8, 5, 6, 7, 2, 6, 9, 3]
    s = Solution()
    s.test(array)
 

if __name__ == "__main__":
    main()