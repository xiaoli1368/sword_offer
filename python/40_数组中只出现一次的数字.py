#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def FindNumsAppearOnce(self, array):
        # write code here
        # 投机取巧的方式
        result = []
        if array == []:
            return result
        
        for i in array:
            if array.count(i) == 1:
                result.append(i)
        
        return result

    def FindNumsAppearOnce2(self, array):
        """
        参考解法
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


def main():
    s = Solution()
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    print(s.FindNumsAppearOnce(array))
    print(s.FindNumsAppearOnce2(array))


if __name__ == "__main__":
    main()