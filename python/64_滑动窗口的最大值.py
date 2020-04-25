#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        length = len(num)
        ret = []
        
        if size > length or size <= 0:
            return ret
        
        for i in range(0, length - size + 1):
            ret.append(max(num[i: i + size]))
        
        return ret