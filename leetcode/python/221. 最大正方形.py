#!/bin/bash python
"""
221. 最大正方形

思路：
动态规划，本题比85题要简单，因为直接dp即可
但是85题，直接dp找不到递归关系，还需要一层循环

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        思路：
        这道题和之前的最大矩形是一致的，只需要添加限定 width == height 即可
        但是考虑到本题是正方形，那么有没有好的思路呢？
        动态规划，dp[i][j]定义为，以(i,j)为右下角的最大正方形边长
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        """
        if matrix == [] or matrix[0] == []:
            return 0
        
        ret = 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    ret = max(ret, dp[i][j]**2)
        return ret