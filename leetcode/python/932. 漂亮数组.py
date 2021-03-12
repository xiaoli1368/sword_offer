#!/bin/bash python
"""
932. 漂亮数组

思路：
分治
"""

class Solution(object):
    # ===== 基本思路（夭折） =====
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        求1-N的一个全排列，保证：
        不存在 i < k < j, A[i] A[k] A[j] 为等差序列
        也就是该全排列，不存在等差子序列

        暴力方法：
        回溯，每次选择可选的元素，同时生成下一层元素的禁止选用的元素
        保证添加下一层之后不会引入等差子序列

        分治法：
        递归，选择中间值mid，然后递归形成左右两个漂亮数组
        然后二重循环，判断当前层是否存在：left + right == 2 * mid
        """
        pass

    # ===== 分治 =====
    def beautifulArray(self, N: int) -> List[int]:
        """
        技巧性太强，想不出来，首先明确几条性质：
        参考链接：https://leetcode-cn.com/problems/beautiful-array/solution/piao-liang-shu-zu-by-leetcode/
                 https://leetcode-cn.com/problems/beautiful-array/solution/c-fen-zhi-fa-dai-tu-pian-jie-shi-by-avphn4vwuo/
        1. 如果A为漂亮数组，那么线性变换后k*A+b也是漂亮数组
        2. 奇数 + 偶数 = 奇数
        3. 如果A为漂亮数组且全部是奇数，B为漂亮数组全部为偶数，则[A, B]一定也是漂亮数组
           因为 A[i] + 2*A[j] = B[k]，或者 A[i] + 2*B[j] = B[k] 由于奇偶性质一定不成立
        本题的分治策略如下：
        1. 按照奇偶，划分当前层次为左右两部分
        2. 递归保证左右两部分都是漂亮数组
           对于偶数部分，每部分元素对应的变换为：A//2，例如[2, 4]变换为[1, 2]再次划分
           同理奇数部分，每部分元素对应的变换为：(A+1)//2，例如[1, 3]变换为[1, 2]
        自底向上的分治策略：
        1. 对N，生成左右两部分的漂亮数组
        2. 两部分数组分别进行变换，合成后输出
        3. 记忆化搜索，增加字典
        记忆化搜索比DP优秀的地方：不会产生一些不需要使用的冗余状态
        """
        d = {1: [1]}
        def getArray(n):
            if n not in d:
                left, right = getArray((n + 1) // 2), getArray(n // 2)
                d[n] = [2 * x - 1 for x in left] + [2 * x for x in right]
            return d[n]
        return getArray(N)