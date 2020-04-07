#!/bin/python3
#-*- coding:utf-8 -*-

class solution():
    # 需要赋值到duplication[0]
    # 函数返回bool
    def duplicate(self, numbers, duplication):
        i = 0
        while (i < len(numbers)):
            if numbers[i] == i:
                i += 1
            elif numbers[i] != numbers[numbers[i]]:
                index = numbers[i]
                numbers[i], numbers[index] = numbers[index], numbers[i]
            else:
                duplication[0] = numbers[i]
                return True
        return False


if __name__ == "__main__":
    test = [2, 3, 1, 0, 2, 5, 3]
    duplication = [0]
    s = solution()
    print(s.duplicate(test, duplication), duplication[0])

