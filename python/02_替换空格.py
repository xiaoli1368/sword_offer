#!bin/bash python3
# -*- coding:utf-8 -*-

class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        tmp = ""
        for i in s:
            if i == " ":
                tmp += "%20"
            else:
                tmp += i
        return tmp


def main():
    s = Solution()
    input_str = " A B "
    #input_str = " 1 2 "
    #input_str = " "
    print(s.replaceSpace(input_str))
    print(s.replaceSpace2(input_str))


if __name__ == "__main__":
    main()