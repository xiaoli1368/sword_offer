#!/bin/bash python3
#-*- coding:utf-8 -*-

class Solution:
    def printMatrix(self, matrix):
        """
        顺时针打印矩阵
        """
        if matrix == []:
            return

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        result = []
        while top <= bottom and left <= right:
            # 上横线
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # 右竖线
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])
            # 下横线
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[bottom][i])
            # 左竖线
            if left != right:
                for i in range(bottom-1, top, -1):
                    result.append(matrix[i][left])
            # 更新        
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return result


def main():
    s = Solution()

    array = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    for i in array:
        print(i)
        
    print(s.printMatrix(array))


if __name__ == "__main__":
    main()