#!bin/bash python3
#-*- coding:utf-8 -*-

import pdb

class Solution():
    def reOrderArray(self, array):
        """
        两个数组，一次遍历
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
        pythonic方式
        """
        return sorted(array, key=lambda x: x%2, reverse=True)

    def reOrderArray3(self, array):
        """
        一个数组，两次遍历
        """
        tmp = []
        for i in array:
            if i % 2 == 1:
                tmp.append(i)
        for i in array:
            if i % 2 == 0:
                tmp.append(i)
        return tmp

    def reOrderArray4(self, array):
        """
        冒泡的方式，移动偶数到最右边
        """
        index = 0
        length = len(array)
        evencnt = 0
        evenidx = 0
        
        for i in array:
            if i % 2 == 0:
                evencnt += 1

        while index < length and evenidx < evencnt:
            if array[index] % 2 == 0:
                tmp = array[index]
                array.append(tmp)
                del array[index]
                evenidx += 1
            else:
                index += 1
        return array

    def reOrderArray5(self, array):
        """
        二重循环方式的冒泡
        """
        for i in range(len(array)):
            for j in range(len(array)-1):
                if array[j] % 2 == 0 and array[j+1] % 2 == 1:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

def main():
    s = Solution()
    array = [1, 8, 5, 6, 7, 2, 6, 9, 3]
    print(s.reOrderArray(array))
    print(s.reOrderArray2(array))
    print(s.reOrderArray3(array))
    print(s.reOrderArray4(array))
    print(s.reOrderArray5(array))
 

if __name__ == "__main__":
    main()