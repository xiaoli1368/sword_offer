#!/bin/bash python
"""
308. 二维区域和检索 - 可变

思路：
因为存在update函数可以任意更新一点值
因此如果继续使用二维前缀和则会比较麻烦，因此更新点[i,j]值后
则需要更新其右下角所有位置的累加和

更加高效的思路是使用多次循环累加的行前缀和
1. 在获取目前结果时，需要累加各个行的累加和
2. 在update之后，只需要更新[i,j]右侧同一行的累加和即可

可以分析一下这二者的区别：
1. 二维前缀和，每次update花费O(n^2)，每次sumRange花费O(1)
2. 行前缀和，每次update花费O(n)，每次sumRange花费O(n)
猛一看好像二者性能差不太多，区别在于实际运行中update和sumRange的调用次数

更加高效的思路：树状数组，线段树

参考链接：https://michael.blog.csdn.net/article/details/107417676?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-8.control
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        二维前缀和
        使用行前缀和
        """
        self.vec = matrix
        row, col = len(matrix), len(matrix[0])
        self.dp = [[0] * (col + 1) for _ in range(row)]
        for i in range(row):
            for j in range(col):
                self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]


    def upate(self, row, col, val):
        """
        更新指定位置
        然后更新行前缀和
        """
        self.vec[row][col] = val
        for j in range(col, len(self.vec)):
            self.dp[row][j + 1] = self.dp[row][j] + self.vec[row][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        进行求和
        """
        ssum = 0
        for i in range(row1, row2 + 1):
            ssum += self.dp[i][col2 + 1] - self.dp[i][col1]
        return ssum


if __name__ == "__main__":
    matrix = [[0, 3, 4], [5, 0, 1], [2, 8, 7]]
    for mat in matrix:
        print(mat)
    cla = NumMatrix(matrix)
    print(cla.sumRegion(0, 0, 2, 2))
    cla.upate(0, 0, 3)
    print(cla.sumRegion(0, 0, 2, 2))