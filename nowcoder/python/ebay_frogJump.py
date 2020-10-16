#!/bin/bash python
"""
https://www.nowcoder.com/discuss/524263?type=post&order=time&pos=&page=1&channel=1009&source_id=search_post

青蛙跳台阶
dp方法
"""

class Solution(object):
    def jump(self, n):
        """
        可行的跳跃总数
        """
        if n <= 1:
            return 0
        dp = [1] * 2 + [0] * (n - 1)
        for i in range(1, n + 1):
            j = 0
            while i - 2**j >= 1:
                dp[i] += dp[i - 2**j]
                j += 1
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.jump(5))