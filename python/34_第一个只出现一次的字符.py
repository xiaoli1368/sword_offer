#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
    def FirstNotRepeatingChar(self, s):
        """
        暴力枚举
        """
        length = len(s)
        if length == 0:
            return -1
        if length == 1:
            return 0

        for i in range(0, length):
            sign = True
            for j in range(0, length):
                if i != j and s[i] == s[j]:
                    sign = False
                    break
            if sign:
                return i
        
        return -1

    def FirstNotRepeatingChar2(self, s):
        """
        使用字典方法
        """
        if s == "":
            return -1

        d = {} # d = dict()
        for i in s:
            """
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            """
            d[i] = d.get(i, 0) + 1
        for index, i in enumerate(s):
            if d[i] == 1:
                return index
        return -1

    def FirstNotRepeatingChar3(self, s):
        """
        使用数组来构建hash的方法
        """
        if s == "":
            return -1

        d = [0] * 256
        for i in s:
            d[ord(i)] += 1
        for index, i in enumerate(s):
            if d[ord(i)] == 1:
                return index
        return -1

    def FirstNotRepeatingChar4(self, s):
        """
        字符串高效方法
        """
        if len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1;

    def FirstNotRepeatingChar5(self, s):
        """
        一行解法
        """
        return s.index(list(filter(lambda c: s.count(c) == 1, s))[0]) if s else -1


def main():
    s = Solution()
    input_str = "google"

    print(s.FirstNotRepeatingChar(input_str))
    print(s.FirstNotRepeatingChar2(input_str))
    print(s.FirstNotRepeatingChar3(input_str))
    print(s.FirstNotRepeatingChar4(input_str))


if __name__ == "__main__":
    main()