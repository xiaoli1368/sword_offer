#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def FirstNotRepeatingChar1(self, s):
        """
        暴力枚举
        两重循环
        """
        if s == "":
            return -1

        for i in range(0, len(s)):
            sign = True
            for j in range(0, len(s)):
                if i != j and s[i] == s[j]:
                    sign = False
                    break
            if sign:
                return i
        
        return -1

    def FirstNotRepeatingChar2(self, s):
        """
        使用字典方法
        空字典的生成：d = {} 或 d = dict()
        判断有无的基础逻辑：（存在高效方式）
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        """
        if s == "":
            return -1

        d = dict()
        for i in s:
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
        if s == "":
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1;

    def FirstNotRepeatingChar5(self, s):
        """
        一行解法
        s.index(list(filter(lambda c: s.count(c) == 1, s))[0]) if s else -1
        这个解法，对list为空则报错，即无法处理"aabbcc"这种情况
        """
        try:
            return s.index(list(filter(lambda c: s.count(c) == 1, s))[0]) if s else -1
        except:
            return -1

    def test(self, s):
        """
        测试函数
        """
        func_vec = [self.FirstNotRepeatingChar1,
                    self.FirstNotRepeatingChar2,
                    self.FirstNotRepeatingChar3,
                    self.FirstNotRepeatingChar4,
                    self.FirstNotRepeatingChar5]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(s)
            end = time.time()

            if result >= 0:
                print("time(us): {:>6.2f}, result: {}".format((end - start)*10**6, s[result]))
            else:
                print("time(us): {:>6.2f}, result: no!".format((end - start)*10**6))


def main():
    str1 = ""
    str2 = "aabbcc"
    str3 = "abcthka"
    str4 = "leetcode"
    str5 = "aslkjflasflaskdflm;eoion3g"
    str6 = "a" * 1000

    s = Solution()
    s.test(str1)
    s.test(str2)
    s.test(str3)
    s.test(str4)
    s.test(str5)
    s.test(str6)


if __name__ == "__main__":
    main()