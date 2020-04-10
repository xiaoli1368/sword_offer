#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.ret = []
        
    def perm(self, ss, low, high):
        if low == high:
            tmp = "".join(ss)
            self.ret.append(tmp)
            return
        
        # 这里是个坑，需要补上之前的那一小段才可以
        curr = ss[0:low] + sorted(ss[low:high + 1])
        
        for i in range(low, high + 1):
            if i == low or curr[i] != curr[low]:
                curr[i], curr[low] = curr[low], curr[i]
                self.perm(curr, low + 1, high)
                curr[i], curr[low] = curr[low], curr[i]
                
        return
    
    def Permutation(self, ss):
        # write code here
        if ss == None:
            return self.ret
        
        strList = list(ss)
        self.perm(strList, 0, len(strList) - 1)
        
        return self.ret


def main():
    ss = "aabc"
    s = Solution()
    result = s.Permutation(ss)

    print(ss)
    print(result)


if __name__ == "__main__":
    main()