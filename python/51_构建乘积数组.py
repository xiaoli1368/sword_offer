#!/bin/bash/ python3
#-*- coding:utf-8 -*-

class Solution:
    def multiply(self, A):
        # write code here
        if len(A) == 0:
            return []
        ret = [0] * len(A)
        
        tmp = 1
        for i in range(0, len(A)):
            ret[i] = tmp
            tmp *= A[i]
        
        tmp = 1
        for i in range(len(A) - 1, -1, -1):
            ret[i] *= tmp
            tmp *= A[i]
        
        return ret