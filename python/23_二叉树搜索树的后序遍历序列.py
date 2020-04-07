#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution():
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

    def VerifySeqenceOfBST(self, sequence):
        if sequence == []:
            return False

        return self.VerfyBST(sequence, 0, len(sequence) - 1)


def main():
    s = Solution()
    sequence = [2, 9, 5, 16, 17, 15, 19, 12]
    sequence2 = [4, 5, 2, 6, 7, 3, 1]
    print(s.VerifySeqenceOfBST(sequence))
    print(s.VerifySeqenceOfBST(sequence2))


if __name__ == "__main__":
    main()