#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution:
    def IsPopOrder(self, pushVec, popVec):
        """
        参考答案的方法
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

    def IsPopOrder2(self, pushVec, popVec):
        """
        自己的方法，根据配对数量
        这种方式，自己使用del实现了一些pop操作
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


def main():
    s = Solution()
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popV2 = [4, 3, 5, 1, 2]
    
    print(s.IsPopOrder(pushV, popV))
    print(s.IsPopOrder(pushV, popV2))

    print(s.IsPopOrder2(pushV, popV))
    print(s.IsPopOrder2(pushV, popV2))


if __name__ == "__main__":
    main()