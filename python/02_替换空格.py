#!bin/bash python3
# -*- coding:utf-8 -*-

import time

class Solution:
    def replaceSpace1(self, s):
        """
        pythonic方法
        """
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        """
        扩容替换法
        """
        tmp = ""
        for i in s:
            if i == " ":
                tmp += "%20"
            else:
                tmp += i
        return tmp

    def test(self, s):
        """
        测试函数
        """
        func_vec = [self.replaceSpace1, self.replaceSpace2]
        print("=====")
        for func in func_vec:
            tmp_s1 = s[:]
            start = time.time()
            result = func(tmp_s1)
            end = time.time()
            print("tims(us): {:>5.2f}, result: {:s}".format((end - start)*10**6, result))


def main():
    str1 = " A B "
    str2 = " 23sa  woj fpqfm qo jsa ";

    s = Solution()
    s.test(str1)
    s.test(str2)


if __name__ == "__main__":
    main()