#!/bin/bash python
"""
279. 完全平方数

思路：
DP
"""

class Solution:
    # ===== 超时 =====
    def numSquares1(self, n):
        """
        思路
        1. 一定可以表示为平方数的和吗？答案是一定，应为全部为1即可。
        2. 状态递推方程：dp[i] = min(dp[i], dp[j][i-j]), j = 0:i
        3. 把数字i分为两部分，j和i-j，各自分解即可。
        """
        if n <= 0:
            return 0
        sqrt, dp = 1, [n] * (n + 1)
        for i in range(1, n + 1):
            if i == sqrt ** 2:
                dp[i] = 1
                sqrt += 1
                continue
            for j in range(1, i // 2 + 1):
                dp[i] = min(dp[i], dp[j] + dp[i - j])
        return dp[n]

    # ===== 优化版本 =====
    # 继续超时，但是cpp可以AC
    def numSquares2(self, n):
        """
        dp[i] = min(dp[i], dp[sqrt**2], dp[i - sqrt**2])
        """
        if n <= 0:
            return 0
        sqrt, dp = 1, [n] * (n + 1)
        for i in range(1, n + 1):
            if i == sqrt ** 2:
                dp[i] = 1
                sqrt += 1
            else:
                for j in range(1, sqrt):
                    dp[i] = min(dp[i], 1 + dp[i - j ** 2])
        return dp[n]
    
    # ===== 后续优化版 =====
    def numSquares3(self, n):
        """
        这个版本可以AC
        但是对于i为完全平方数时，明确多循环了几次
        想不通为什么速度更快
        """
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[-1]


if __name__ == "__main__":
    import time
    s = Solution()
    n = 5360

    start = time.time()
    ret = s.numSquares1(n)
    end = time.time()
    print("result: {}, times: {}".format(ret, end - start))

    start = time.time()
    ret = s.numSquares2(n)
    end = time.time()
    print("result: {}, times: {}".format(ret, end - start))

    start = time.time()
    ret = s.numSquares3(n)
    end = time.time()
    print("result: {}, times: {}".format(ret, end - start))