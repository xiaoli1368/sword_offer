#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    
    def GetMedian(self, not_used):
        # write code here
        length = len(self.data)
        if length == 0:
            return 0.0
        
        if length % 2 == 1:
            return self.data[length // 2]
        else:
            return float(self.data[length // 2] + self.data[length // 2 - 1]) / 2