#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s == None or len(s) == 0:
            return False
        
        e_cnt = 0
        dot_cnt = 0
        has_value = False
        
        i = 0 if s[0] != "+" and s[0] != "-" else 1
        for j in range(i, len(s)):
            if s[j] >= "0" and s[j] <= "9":
                has_value = True
            else:
                has_value = False
                if s[j] == "." and e_cnt == 0:
                    dot_cnt += 1
                elif s[j] == "e" or s[j] == "E":
                    e_cnt += 1
                elif (s[j] == "+" or s[j] == "-") and (s[j-1] == "e" or s[j-1] == "E"):
                    continue
                else:
                    return False
                
                if e_cnt >= 2 or dot_cnt >= 2:
                    return False
        
        return has_value


    # 投机取巧解法
    def func(self, s):
        try:
            ss = float(s)
            return True
        expect:
            return False
