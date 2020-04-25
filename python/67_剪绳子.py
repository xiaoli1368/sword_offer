#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, n):
        # write code here
        if n <= 3:
            return n - 1
        cnt3 = n // 3 - 1 if n % 3 == 1 else n // 3
        cnt2 = (n - cnt3 * 3) // 2
        return 2**cnt2 * 3**cnt3