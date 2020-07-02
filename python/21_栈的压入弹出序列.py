#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def IsPopOrder1(self, pushVec, popVec):
        """
        自己的方法，比较麻烦
        根据配对数量，自己使用del实现了一些pop操作
        """
        if pushVec == [] or popVec == []:
            return False
        else:
            pushV = pushVec.copy()
            popV = popVec.copy()

        length = len(pushV)
        pair = 0
        tmp = [pushV[0]]

        while pair < length:
            if tmp[-1] != popV[0]:
                if pushV != []:
                    tmp.append(pushV[0])
                    del pushV[0]
                else:
                    return False
            else:
                del tmp[-1]
                del popV[0]
                pair += 1

        return True

    def IsPopOrder2(self, pushVec, popVec):
        """
        高效方法，模拟出栈
        """
        if pushVec == [] or popVec == []:
            return False
        else:
            # 进行值传递，排除对外界的影响
            pushV = pushVec.copy()
            popV = popVec.copy()

        stack = []
        for i in pushV:
            stack.append(i)
            while stack != [] and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if stack:
            return False
        else:
            return True

    def IsPopOrder3(self, pushV, popV):
        """
        高效方法优化版，使用计数代替了pop
        """
        if pushV == [] or popV == []:
            return False

        i = 0
        stack = []
        for num in pushV:
            stack.append(num)
            while stack != [] and stack[-1] == popV[i]:
                i += 1
                stack.pop()

        return stack == []

    def test(self, pushV, popV):
        """
        测试函数
        """
        func_vec = [self.IsPopOrder1,
                    self.IsPopOrder2,
                    self.IsPopOrder3]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(pushV, popV)
            end = time.time()

            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popV2 = [4, 3, 5, 1, 2]

    s = Solution()
    s.test(pushV, popV)
    s.test(pushV, popV2)
    

if __name__ == "__main__":
    main()