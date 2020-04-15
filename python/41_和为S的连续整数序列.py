#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def add_vec(self, array, l, h):
        """
        用于添加的函数
        """
        if l <= 0:
            return
        array.append(list(range(l, h + 1)))

    def FindContinuousSequence(slef, tsum):
        """
        参考解法
        """
        if tsum < 3:
            return []

        l = 1
        h = 2
        currSum = 3
        result = []

        while l <= tsum // 2 + 1:
            if currSum > tsum:
                currSum -= l
                l += 1
            elif currSum < tsum:
                h += 1
                currSum += h
            else:
                # 此时相等
                result.append(list(range(l, h + 1)))
                currSum -= l
                l += 1

        return result

    def FindContinuousSequence2(self, tsum):
        """
        个人解法
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


def main():
    s = Solution()
    print(s.FindContinuousSequence(100))
    print(s.FindContinuousSequence2(100))


if __name__ == "__main__":
    main()