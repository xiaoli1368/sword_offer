#!/bin/bash python
"""
85. 最大矩形

思路：
1. 暴力法
2. 单调栈/动态规划
3. 三维dp
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        思路一：
        暴力方法，二重循环遍历两个点，当作对角线，判断是否为全1
        或者遍历每个点作为左上角，枚举宽和高

        思路二：
        二维dp，思考每个点当作右下角时，如何递推
        """
        if matrix == []:
            return 0
        
        # 按行向右累积宽度
        ret = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                # 计算最大宽度
                width = dp[i][j] = dp[i][j - 1] + 1 if j - 1 >= 0 else 1
                # 计算最大面积
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    ret = max(ret, width * (i - k + 1))
        
        return ret

    # ===== 二维DP优化版 =====
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]表示以[i,j]为右端的最大连续1的长度
        dp[i][j] = maxWidth * maxHeight
        需要统计每个元素左侧的连续为1的长度
        然后向上遍历，得到最好可能的矩形面积，更新最大值
        """
        if matrix == []:
            return 0
        area, row, col = 0, len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    width = dp[i][j] = (1 if j == 0 else 1 + dp[i][j - 1])
                    for k in range(i, -1, -1):
                        if dp[k][j] == 0: break
                        width = min(width, dp[k][j])
                        height = i - k + 1
                        area = max(area, width * height)
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        三维dp高效方法
        """
        if matrix == []:
            return 0
        
        ret = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[[0] * 3 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1": # 只有当前元素为1的时候，才对最大面积有贡献
                    if i == 0 and j == 0: # 左上角
                        dp[i][j] = [1, 1, 1]
                    elif i == 0: # 第一行
                        dp[i][j] = [dp[i][j - 1][0] + 1, 1, dp[i][j - 1][2] + 1]
                    elif j == 0: # 第一列
                        dp[i][j] = [1, dp[i - 1][j][1] + 1, dp[i - 1][j][2] + 1]
                    else:
                        col = dp[i][j][0] = dp[i][j - 1][0] + 1 # 向左连续1的个数
                        row = dp[i][j][1] = dp[i - 1][j][1] + 1 # 向上连续1的个数
                        for k in range(row): # 计算面积
                            col = min(col, dp[i - k][j][0])
                            dp[i][j][2] = max(dp[i][j][2], col * (k + 1))
                    ret = max(ret, dp[i][j][2])
        
        return ret