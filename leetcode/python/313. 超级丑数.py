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
        return ret[-1]

    # ===== 其它版本 =====
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        以 2 3 5 为例
        较大的丑数，都是由较小的丑数乘以 2 3 5 得到的
        因此每个 2 3 5 需要维护一个val，该val表示的当前丑数质因数接下来要乘的最小丑数
        val的更新应按照丑数由小到大，也就是最终的ret
        这里用pointers来表示ret，内部保存的是在ret中的索引
        本质是动态规划：
        dp[i] = min(primes[j] * dp[pointers[j]]) j = 0:len(primes)
        """
        k = len(primes)
        ret, pointers = [1], [0] * k
        for i in range(n - 1):
            mmin = float("+inf")
            for j in range(k):
                mmin = min(mmin, primes[j] * ret[pointers[j]])
            ret.append(mmin)
            for j in range(k):
                if primes[j] * ret[pointers[j]] == mmin:
                    pointers[j] += 1
        return ret[-1]

    # ===== 堆思路 =====
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        堆
        使用最小堆迭代n次，就能得到第n小的超级丑数
        每次都要使用当前的最小丑数来乘以primes中的各个因子
		每次将k个构造出来的丑数送入堆，不一定都满足要求，而且存在重复
		始终明确：更大的丑数 = 较小的丑数 * 所有的因子
        注意防止重复
        """
        vec = [1]
        for _ in range(n - 1):
            curr = heappop(vec)
            while vec and curr == vec[0]: # 去除重复元素
                heappop(vec)
            for p in primes:
                heappush(vec, curr * p)
        return heappop(vec)