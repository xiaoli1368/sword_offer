#!/bin/bash python
"""
650. 只有两个键的键盘

思路：
动态规划
1 2 3 4 5 6 7 8 9 10 11 12
0 2 3 4 5 5 7 6 6  7 11 7
思考倍数关系，如果 i = 2 * j，则有dp[i] = 2 + dp[j]，因为copy paste
             如果 i = 3 * j，则有dp[i] = 3 + dp[j]，因为copy paste paste
思考 n = 12 的情况，12 = 2 * 6 = 3 * 4 = 4 * 3 = 6 * 2
如果进行分配，最终比较发现是优先获取6，然后对6使用一次copy paste即可
也就是对i进行素数分解，保证j是更小的素数，此时有：dp[i] = j + dp[i // j]

类似的题目还有：338. 比特位计数
"""

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        1 2 3 4 5 6 10
        0 2 3 4 5 5 7
        """
        if n <= 1:
            return 0
        dp = list(range(n + 1))
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = j + dp[i // j]
                    break
        return dp[n]