#!/bin/bash python3
#-*- coding:utf-8 -*-

import time
import itertools

class Solution:
    def __init__(self):
        self.ret = []

    # ===== 外部接口 =====
    def Permutation1(self, ss):
        """
        1. 使用stl求解（有序，无重复）
        注意：
            [1] stl中的全排列函数，存在重复，且不排序
            [2] 返回值是一个迭代器，使用list()后，内部元素都是tuple
        """
        if len(ss) == 0:
            return []
        
        tmp_ss = sorted(ss)
        tmp_ret = ["".join(i) for i in itertools.permutations(tmp_ss)]

        # 利用set去重并排序
        tmp_ret = list(set(tmp_ret))
        tmp_ret.sort()
        return tmp_ret
    
    def Permutation2(self, ss):
        """
        2. 递归传递引用，set，sort（有序，无重复）
        """
        if len(ss) == 0:
            return []
        
        # 无序版本
        self.perm0(list(ss), 0)

        # 利用set去重并排序
        self.ret = list(set(self.ret))
        self.ret.sort()
        return self.ret
    
    def Permutation3(self, ss):
        """
        3. 递归传递引用，内部使用stl排序（有序，重复）
        """
        if len(ss) == 0:
            return []
        
        self.perm1(sorted(list(ss)), 0)
        return self.ret

    def Permutation4(self, ss):
        """
        4. 递归传递值，不使用使用stl排序，循环替换实现（有序，重复）
        """
        if len(ss) == 0:
            return []
        
        self.perm2(sorted(list(ss)), 0)
        return self.ret

    # ===== 递归函数 =====

    def perm0(self, strList, start):
        """
        无序版本，递归传递引用
        输入字符串ss对应的列表strList，以及起始索引start
        原始字符串无法快速交换元素值
        """
        if start == len(strList) - 1:
            self.ret.append("".join(strList))
            return
        
        for i in range(start, len(strList)):
            strList[i], strList[start] = strList[start], strList[i]
            self.perm0(strList, start + 1)
            strList[i], strList[start] = strList[start], strList[i]
        return
    
    def perm1(self, strList, start):
        """
        有序版本，递归传递引用
        输入字符串ss对应的列表strList，以及起始索引start
        注意：
            [1] 每次递归调用sort排序
            [2] 如果不要求有序，可以省去sort()步骤
            [3] 需要额外的步骤，来检测重复性
        """
        if start == len(strList) - 1:
            self.ret.append("".join(strList))
            return
        
        # 为了防止排序会打乱索引，导致上一层调用无法恢复
        # 这里保存排序之前的str
        oriStr = strList[:]
        strList = strList[0:start] + sorted(strList[start:])
        
        for i in range(start, len(strList)):
            if i == start or (strList[i] not in strList[start:i]):
                strList[i], strList[start] = strList[start], strList[i]
                self.perm1(strList, start + 1)
                strList[i], strList[start] = strList[start], strList[i]
        
        strList = oriStr
        return

    def perm2(self, oriStrList, start):
        """
        有序版本，递归传递值
        输入字符串ss对应的列表strList，以及起始索引start
        注意：
            [1] 这种方式传递了很多次形式参数
            [2] 不需要额外的步骤
        """
        if start == len(oriStrList) - 1:
            self.ret.append("".join(oriStrList))
            return
        
        # 保证值传递
        strList = oriStrList[:]
        
        for i in range(start, len(strList)):
            if i == start or strList[i] != strList[start]:
                strList[i], strList[start] = strList[start], strList[i]
                self.perm1(strList, start + 1)
        
        return
        
    # ===== 工具函数 =====
    
    def printf_vecStr(self, ret):
        """
        打印list[str]结果
        仅显示结果个数不超过24的情况
        """
        if len(ret) > 24:
            print("{:d} numbers, too many to display!".format(len(ret)))
        else:
            print(", ".join(ret))


    def test(self, ss):
        """
        测试函数
        """
        func_vec = [self.Permutation1,
                    self.Permutation2,
                    self.Permutation3,
                    self.Permutation4]
        print("=====")
        for func in func_vec:
            self.ret = []
            tmp_ss = ss[:]

            start = time.time()
            result = func(tmp_ss)
            end = time.time()

            print("tims(us): {:>7.2f}, result: ".format((end - start)*10**6), end="")
            self.printf_vecStr(result)


def main():
    str1 = "cab"
    str2 = "abac"
    str3 = "cbba"
    str4 = "sghi"
    str5 = "iugoa"
    str6 = "sadjbg"

    s = Solution()
    s.test(str1)
    s.test(str2)
    s.test(str3)
    s.test(str4)
    s.test(str5) #结果个数：5! = 120
    s.test(str6) # 结果个数：6! = 720


if __name__ == "__main__":
    main()