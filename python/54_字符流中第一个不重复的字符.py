#!/bin/bash/ python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def __init__(self):
        self.data = []
        self.hash = [0] * 256
        self.que = []
        self.str = ""
    
    # ===== 第一种方式： pythonic =====
    def Insert1(self, ch):
        if ch != None:
            self.data.append(ch)
    
    def FirstAppearingOnce1(self):
        for i in self.data:
            if self.data.count(i) == 1:
                return i
        return "#"
    
    # ===== 第二种方式： hash + str =====
    def Insert2(self, ch):
        if ch != None:
            self.str += ch
            self.hash[ord(ch)] += 1
    
    def FirstAppearingOnce2(self):
        for ch in self.str:
            if self.hash[ord(ch)] == 1:
                return ch
        return "#"
 
    # ===== 第三种方式： hash + que =====
    def Insert3(self, ch):
        if ch != None:
            self.hash[ord(ch)] += 1
            if self.hash[ord(ch)] == 1:
                self.que.append(ch)
    
    def FirstAppearingOnce3(self):
        while self.que != []:
            if self.hash[ord(self.que[0])] == 1:
                return self.que[0]
            else:
                self.que.pop(0)
        return "#"
    
    def test_inner(self, ss, Insert, Appear):
        """
        测试函数，内部调用
        输入测试字符串，insert函数指针，appear函数指针
        输入结果字符串
        """
        tmp = ""
        for ch in ss:
            Insert(ch)
            tmp += Appear()
        return tmp
 
    def test(self, ss):
        """
        测试函数
        """
        func_vec_Insert = [self.Insert1, self.Insert2, self.Insert3]
        func_vec_Appear = [self.FirstAppearingOnce1,
                           self.FirstAppearingOnce2,
                           self.FirstAppearingOnce3]
        print("=====")
        for i in range(len(func_vec_Insert)):
            self.__init__()
            start = time.time()
            result = self.test_inner(ss, func_vec_Insert[i], func_vec_Appear[i])
            end = time.time()
            print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))


def main():
    str1 = "google"
    str2 = "sasladfjslai65d13asfi2u"

    s = Solution()
    s.test(str1)
    s.test(str2)


if __name__ == "__main__":
    main()