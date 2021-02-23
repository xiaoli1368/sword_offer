#!/bin/bash python
"""
313. 超级丑数

思路：
动态规划，多指针法
"""

class Solution(object):
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        思考：
        1. 假设质数因子只有[a, b, c]，则丑数为：a^x * b^y * c^z
        2. 如果获取前10个丑数，暴力方法是分别为xyz遍历10次，然后得到1000个解，排序得到前10个
        3. 思考联系：后面的丑数一定是前面的丑数乘以[a, b, c]得到的
        4. 设置三个指针[ta, tb, tc]，分别与[a, b, c]相乘来产生新的丑数
        5. 其中[ta, tb, tc]的含义是：与当前的固定因子相乘的最小的丑数，从已生成的丑数中顺序得到
        6. 如何更新[ta, tb, tc]，只要可以通过乘以固定因子来得出当前丑数，则指针移动
        """
        if n <= 1 or primes == []:
            return 1
        m = len(primes)
        pointer = [0] * m
        ret = [1] + [float("+inf")] * (n - 1)
        for i in range(1, n):
            for j in range(m):
                ret[i] = min(ret[i], primes[j] * ret[pointer[j]]) # 更新下一个丑数
            for j in range(m):
                if ret[i] == primes[j] * ret[pointer[j]]: # 更新指针
                    pointer[j] += 1
        return ret[-1]]