#!/bin/bash/ python3
#-*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(s) != 0 and len(pattern) == 0:
            return False
        elif len(s) == 0  and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False
        else: # 二者都非空
            if len(pattern) == 1 or pattern[1] != "*": # 后一位不是 *
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False
            else: # 后一位是 *
                if s[0] != pattern[0] and pattern[0] != ".":
                    return self.match(s, pattern[2:])
                else:
                    return self.match(s[1:], pattern) or self.match(s, pattern[2:])

    # 递归回溯法
    def match(self, s, pattern):
        # write code here
        if len(pattern) == 0:
            return len(s) == 0
        
        # 此时pattern非空
        first_match = False
        if len(s) != 0 and (s[0] == pattern[0] or pattern[0] == "."):
            first_match = True
        
        # 此时pattern长度为1或者后一个元素不是"*"
        if len(pattern) == 1 or pattern[1] != "*":
            return first_match and self.match(s[1:], pattern[1:])
        else: # 此时pattern后一个元素为"*"
            return self.match(s, pattern[2:]) or (first_match and self.match(s[1:], pattern))