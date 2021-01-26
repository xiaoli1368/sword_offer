#!/bin/bash python
"""
1128. 等价多米诺骨牌对的数量

思路：
哈希
1. 注意到统计的可以等级价的对数，例如[[1, 2], [1, 2], [1, 2]]结果为3
   最开始的思路是使用(i,j)和(j,i)作为相同的key，最后统计不同key的内部配对个数
   还有一种思路就是在生成key中统计总对数，也就是每次加入当前key时考虑新引入了多少个等价对
2. 关于key，有一个更加高效的方式是使用固定的key，也就是使用(min, max)作为固定的键
3. 另一种使用key的方式是，考虑到两个数子得范围，可以使用二者拼接成数字，使用num[100]作为hash
"""

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        固定使用(i,j)作为key，i为较小值
        """
        cnt = 0
        d = dict()
        for i, j in dominoes:
            key = (min(i, j), max(i, j))
            cnt += d.get(key, 0)
            d[key] = 1 + d.get(key, 0)
        return cnt

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0
        num = [0] * 100
        for i, j in dominoes:
            key = i * 10 + j if i < j else j * 10 + i
            cnt += num[key]
            num[key] += 1
        return cnt