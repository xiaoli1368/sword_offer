#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def IsContinuous(self, numbers):
        if len(numbers) != 5:
            return False
        
        nmin = 14
        nmax = 0
        zero_cnt = numbers.count(0)

        for i in numbers:
            if i == 0:
                continue
            if i < nmin:
                nmin = i
            if i > nmax:
                nmax = i
        
        if nmin < 0 or nmax > 13:
            return False

        if zero_cnt == 4 or (nmax - nmin <= 4 and nmax != nmin):
            return True
        else:
            return False

    def IsContinuous2(self, numbers):
        """
        参考答案，癞子补全法
        """
        if len(numbers) != 5:
            return False
        
        numbers.sort()
        cnt = numbers.count(0)

        for i in range(cnt, len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                return False
            cnt -= numbers[i + 1] - numbers[i] - 1
        
        return cnt >= 0


def main():
    s = Solution()
    numbers = [1, 3, 0, 0, 5]
    print(s.IsContinuous(numbers))
    print(s.IsContinuous2(numbers))


if __name__ == "__main__":
    main()