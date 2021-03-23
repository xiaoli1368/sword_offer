#!/bin/bash python
"""
307. 区域和检索 - 数组可修改

思路：
直接方法超时了
树状数组，线段树
参考：https://leetcode-cn.com/problems/range-sum-query-mutable/solution/python-shu-zhuang-shu-zu-binary-indexed-tree-by-ze/
"""

# ===== 个人暴力方法 =====
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        二维前缀和
        """
        n = len(nums)
        self.nums = nums
        self.dp = [0] * (n + 1)
        for i in range(n):
            self.dp[i + 1] = self.dp[i] + nums[i]


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        更新index后续影响的位置
        """
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.dp[i + 1] = self.dp[i] + self.nums[i]


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.dp[right + 1] - self.dp[left]

# ===== 树状数组 =====
class NumArray:
    def __init__(self, nums: List[int]):
        ''' 初始化sum 数组, 从一计数, 0 号不用
        '''
        self.tree = [0 for _ in range(len(nums)+1)]     # 从第一个数计算下标和
        for k in range(1, len(self.tree)):
            self.tree[k] = sum(nums[k-(k&-k):k])  # 原来的nums从0计数, tree从1计数
        
    def update(self, i: int, val: int) -> None:
        diff = val - self.sumRange(i,i)  # 计算更新的值和原数的差值, i,j从0 计数
        k = i+1
        while k<=len(self.tree)-1:
            self.tree[k] += diff
            k += k&-k

    def sumRange(self, i: int, j: int) -> int:
        # i, j 是从 0计数
        if i+1 == 1:
            return self.sum1k(j+1)
        else:
            return self.sum1k(j+1) - self.sum1k(i)

    def sum1k(self, k: int) -> int:
        res = 0
        while k>=1:
            res += self.tree[k]
            k -= k&-k
        return res

# ===== 线段数组 =====
class NumArray:
    def __init__(self, nums: List[int]):
        # 获取接近数组最大的 2 次幂
        n = 1
        while n < len(nums): n<<=1
        self.n = n
        # segment_tree
        self.seg_tree = [0]*n+nums+[0]*(n-len(nums))
        # 初始化赋值, 像堆一样
        for k in range(n-1, 0, -1):
            self.seg_tree[k]=self.seg_tree[2*k]+self.seg_tree[2*k+1]

    def update(self, i: int, val: int) -> None:
        k = i + self.n
        diff = val - self.seg_tree[k]
        while k>0:
            self.seg_tree[k] += diff
            k//=2

    def sumRange(self, i: int, j: int) -> int:
        i, j, res = self.n + i, self.n + j, 0
        while i<=j:
            if i%2 == 1:
                res+=self.seg_tree[i]
                i+=1
            if j%2 == 0:
                res+=self.seg_tree[j]
                j-=1
            i,j = i//2, j//2
        return res

# ===== 个人理解版 =====
class NumArray:

    def __init__(self, nums: List[int]):
        """
        注意tree的长度为2倍
        后半部分初始化为Nums的值
        前半部分按照二叉树来求和
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]


    def update(self, index: int, val: int) -> None:
        """
        先更新tree数组中的值
        然后依次向上更新sum
        注意left,right的不同取值
        """
        pos = self.n + index
        self.tree[pos] = val
        while pos > 0:
            if pos % 2 == 0:
                left, right = pos, pos + 1
            else:
                left, right = pos - 1, pos
            self.tree[pos // 2] = self.tree[left] + self.tree[right]
            pos //= 2


    def sumRange(self, left: int, right: int) -> int:
        """
        由nums中的索引转换为tree中的索引
        然后依次向上查找
        """
        ssum, l, r = 0, self.n + left, self.n + right 
        while l <= r:
            if l % 2 == 1:
                ssum += self.tree[l]
                l += 1
            if r % 2 == 0:
                ssum += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return ssum