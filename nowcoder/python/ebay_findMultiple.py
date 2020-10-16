#!/bin/bash python
"""
https://www.nowcoder.com/discuss/524263?type=post&order=time&pos=&page=1&channel=1009&source_id=search_post

核心是输入n,m,k,lst
明确是否存在要求的情况
（可以通过数学推导得出，满足的m个数，每个数都得是k的倍数）
"""

class Solution(object):
    def findMultiple(self, n, m, k, lst):
        """
        对lst遍历，统计是k的倍数的个数，是否大于等于m
        注意当m为2时，则变成了两数之和的情况
        """
        if m == 1:
            return False
        elif m == 2: # 两数之和
            l, h = 0, n - 1
            while l < h:
                if (lst[l] + lst[h]) % k == 0:
                    return True
                l += 1
                h -= 1
            return False
        # 其它情况
        cnt = 0
        for i in lst:
            if i % k == 0:
                cnt += 1
        return cnt >= m

if __name__ == "__main__":
    s = Solution()
    print(s.findMultiple(5, 4, 3, [3, 3, 6, 9, 3]))
    print(s.findMultiple(5, 4, 3, [3, 2, 6, 9, 2]))
    print(s.findMultiple(2, 2, 3, [1, 2]))