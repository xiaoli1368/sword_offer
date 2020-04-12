#!/bin/bash python3 
#-*- coding:utf-8 -*-

class Solution():
    def GetUglyNumber_Solution(self, index):
        """
        暴力解法，复杂度较大
        """
        cnt = 0
        result = 0

        while cnt < index:
            result += 1
            num = result

            while num % 5 == 0:
                num //= 5
            while num % 3 == 0:
                num //= 3
            while num % 2 == 0:
                num //= 2
            
            if num == 1:
                cnt += 1

        return result

    def GetUglyNumber_Solution2(self, index): 
        """
        高效解法
        """
        result = index * [1]
        t2 = t3 = t5 = 0

        for i in range(1, index):
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5)
            if result[i] == 2 * result[t2]:
                t2 += 1
            if result[i] == 3 * result[t3]:
                t3 += 1
            if result[i] == 5 * result[t5]:
                t5 += 1
        
        return result[index - 1]


def main():
    s = Solution()
    for i in range(1, 21):
        print(s.GetUglyNumber_Solution(i),
              s.GetUglyNumber_Solution2(i))


if __name__ == "__main__":
    main()