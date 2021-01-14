#!/bin/bash python
"""
1018. 可被 5 整除的二进制前缀

思路：
1. 暴力模拟法，在cpp中会出现溢出问题
2. 使用取模进行优化，需要证明一个问题，就是使用余数进行迭代结果依然正确

取模公式：
1. (a + b) % p = (a % p + b % p) % p 
2. (a - b) % p = (a % p - b % p) % p 
3. (a * b) % p = (a % p * b % p) % p 
4. (a^b) % p = ((a % p)^b) % p

本题证明：
注意A_k的取值只能是1或者0
N_k % 5 = (N_k_1 * 2 + A_k) % 5
        = ((N_k_1 * 2) % 5 + A_k % 5) % 5
		= ((N_k_1 % 5 * 2 % 5) % 5 + A_k % 5) % 5
如果使用M_k表示N_k对5的余数，则有：
M_k = ((M_k_1 * 2) % 5 + A_k % 5) % 5
    = (M_k_1 * 2 + A_k) % 5
因此直接使用余数的迭代即可。
"""

class Solution(object):
    def prefixesDivBy5(self, a):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        if a == []:
            return []
        
        n, ret = 0, []
        for i in a:
            n = n * 2 + i
            if n % 5 == 0:
                ret.append(True)
            else:
                ret.append(False)
        return ret

    def prefixesDivBy5(self, a):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        # 此时n代表每次的余数
        n, ret = 0, []
        for i in a:
            n = (n * 2 + i) % 5
            ret.append(n == 0)
        return ret