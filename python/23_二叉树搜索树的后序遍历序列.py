#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution():
    def VerifySeqenceOfBST(self, sequence):
        """
        1. 递归法
        """
        if sequence == []:
            return False

        return self.VerifyBST(sequence, 0, len(sequence) - 1)

    def VerifyBST(self, seq, first, last):
        """
        递归检测是否为BST
        """
        # 到达叶节点时
        if first >= last:
            return True

        # 找到当前层次下，左右节点的区分
        rootVal = seq[last]
        cutIndex = first
        while cutIndex < last and seq[cutIndex] < rootVal:
            cutIndex += 1

        # 检测右子树节点是否满足大于根节点
        for i in range(cutIndex, last):
            if seq[i] < rootVal:
                return False

        # 当前层次已经正确，递归判断下一层次
        # 需要注意cutIndex - 1 有可能为 -1，不过可以 hold 住
        return self.VerifyBST(seq, first, cutIndex - 1) and self.VerifyBST(seq, cutIndex, last - 1)

    def VerifySeqenceOfBST2(self, seq):
        """
        2. 单调栈
        """
        if seq== []:
            return False
        
        stack, root = [], float("+inf")

        for i in range(len(seq) - 1, -1, -1):
            if seq[i] > root:
                return False
            while stack and stack[-1] > seq[i]:
                root = stack.pop()
            stack.append(seq[i])
        
        return True

    def test(self, vec):
        """
        测试函数
        """
        func_vec = [self.VerifySeqenceOfBST,
                    self.VerifySeqenceOfBST2]
        print("=====")
        for func in func_vec:
            start = time.time()
            result = func(vec)
            end = time.time()
            print("result: {}, times(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    seq = [2, 9, 5, 16, 17, 15, 19, 12]
    seq2 = [4, 5, 2, 6, 7, 3, 1]

    s = Solution()
    s.test(seq)
    s.test(seq2)


if __name__ == "__main__":
    main()