#!/bin/bash python
"""
977. 有序数组的平方

思路一：
暴力法，O(n + nlgn)

思路二：
二分查找找到负数和非负数的区分点
然后从中间向两头归并
也就是从最小值往最大值归并

思路三：
直接从两头向中间归并（厉害了，要去除思维定式）
也就是从最大值往最小值归并
"""

class Solution(object):
    def sortedSquares(self, a):
        """
        暴力法
        """
        ret = [x ** 2 for x in a]
        return sorted(ret)

    def sortedSquares2(self, a):
        """
        二分+归并
        """
        # 输出二分查找分界点l，l及其右侧都是非负数
        # 特殊情况，l遍历到右边界需要处理
        l, h = 0, len(a) - 1
        while l < h:
            m = l + (h - l) // 2
            if a[m] < 0:
                l = m + 1
            elif a[m] >= 0:
                h = m
        # 归并合并a[0:m-1], a[m:]，注意m有可能等于h
        m = l + 1 if a[l] < 0 else l
        p, q = m - 1, m
        # 归并合并
        ret = [0] * len(a)
        for i in range(len(a)):
            if p >= 0 and (q > len(a) - 1 or a[p] ** 2 < a[q] ** 2):
                ret[i] = a[p] ** 2
                p -= 1
            else:
                ret[i] = a[q] ** 2
                q += 1
        return ret

    def sortedSquare3(self, a):
        """
        直接归并
        """
        ret = a[:]
        p, q = 0, len(a) - 1
        for i in range(len(a) - 1, -1, -1):
            if p <= q and a[p] ** 2 >= a[q] ** 2:
                ret[i] = a[p] ** 2
                p += 1
            else:
                ret[i] = a[q] ** 2
                q -= 1
        return ret

    def test(self, lst):
        """
        测试函数
        """
        func_vec = [self.sortedSquares,
                    self.sortedSquares2,
                    self.sortedSquare3]
        for a in lst:
            print("=====")
            print("input data: {}".format(a))
            for fun in func_vec:
                print(fun(a))

if __name__ == "__main__":
    s = Solution()
    lst = [[-4,-1,0,3,10],
           [-7,-3,2,3,11],
           [-7,-3,-2],
           [2,3,11]]
    s.test(lst)