#!/bin/bash

class Solution(object):
    def __init__(self):
        self.ret = []
    
    def isValid(self, path):
        """
        给定的path是否合法，返回(bool, str)
        """
        hour, minu = 0, 0
        for i in range(4):
            hour = hour * 2 + path[i]
        for i in range(4, len(path)):
            minu = minu * 2 + path[i]
        if hour > 11 or minu > 59:
            return False, None
        else:
            ret = str(hour) + ":"
            if minu < 10:
                ret += "0"
            ret += str(minu)
            return True, ret
        
    def perm(self, path, i):
        if i == len(path):
            valid, s = self.isValid(path)
            if valid:
                self.ret.append(s)
            return
        self.perm(path, i + 1)
        for j in range(len(path)):
            if path[i] == path[j]: # 防止重复
                return
            path[i], path[j] = path[j], path[i]
            self.perm(path, i + 1)
            path[i], path[j] = path[j], path[i]

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0 or num > 10:
            return []
        path = [0] * (10 - num) + [1] * num # 提前排序
        self.perm(path, 0)
        return self.ret