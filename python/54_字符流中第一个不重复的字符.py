#!/bin/bash/ python3
#-*- coding:utf-8 -*-

class Solution:
    # 返回对应char
    def __init__(self):
        self.hash = []
    
    def Insert(self, ch):
        if ch != None:
            self.hash.append(ch)
    
    def FirstAppearingOnce(self):
        for i in self.hash:
            if self.hash.count(i) == 1:
                return i
        return "#"