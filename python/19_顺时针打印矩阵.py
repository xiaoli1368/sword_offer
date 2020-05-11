#!/bin/bash python3
#-*- coding:utf-8 -*-

import time

class Solution:
    def printMatrix(self, matrix):
        """
        高效方式，顺时针打印矩阵
        """
        if matrix == []:
            return

        top = 0
        left = 0
        bottom = len(matrix) - 1
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

    def test(self, array):
        """
        测试函数
        """
        start = time.time()
        result = self.printMatrix(array)
        end = time.time()
        print("=====")
        print("time(us): {:>5.2f}, result: {}".format((end - start)*10**6, result))
    

def main():
    array = [[1, 2, 3, 4]]
    array2 = [[1], [5], [9], [13]]
    array3 = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

    s = Solution()
    s.test(array)
    s.test(array2)
    s.test(array3)


if __name__ == "__main__":
    main()