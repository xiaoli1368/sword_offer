#!/bin/bash python
"""
703. 数据流中的第 K 大元素

思路：
直接按顺序插入，或者是堆排序的思路
"""

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        先按从大到小的顺序插入，然后返回
        """
        # 找到位置
        index = 0
        while index < len(self.nums):
            if self.nums[index] < val:
                break
            index += 1
        # 插入
        self.nums.insert(index, val)
        # 尝试返回第k大
        return self.nums[self.k - 1] if 1 <= self.k <= len(self.nums) else -1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# ===== 堆方法 =====
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        初始化，小顶堆，容量为k
        则堆顶就是这k个数中最小的
        而有可能进入这个堆的条件是：容量不足k，或者大于堆顶元素
        """
        self.k = k
        self.vec = []
        for item in nums:
            self.add(item)
    
    def _swap(self, i, j):
        """
        交换元素
        """
        self.vec[i], self.vec[j] = self.vec[j], self.vec[i]
    
    def push(self, item, fromBack=True):
        """
        从添加元素
        容量不足k时，从末尾直接添加，然后上浮
        容量达到k时，直接替换堆首元素，然后下沉
        """
        if fromBack:
            self.vec.append(item)
            self._shift_up(len(self.vec) - 1)
        else:
            self.vec[0] = item
            self._shift_down(0)
    
    def _shift_up(self, index):
        """
        上浮函数
        """
        while index:
            parent = (index - 1) // 2
            if self.vec[parent] <= self.vec[index]:
                break
            self._swap(parent, index)
            index = parent
    
    def _shift_down(self, index):
        """
        小顶堆下沉
        """
        i, n = index, len(self.vec)
        while 2 * i + 1 < n:
            smallest, l, r = i, 2 * i + 1, 2 * i + 2
            if l < n and self.vec[l] < self.vec[smallest]:
                smallest = l
            if r < n and self.vec[r] < self.vec[smallest]:
                smallest = r
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def add(self, val: int) -> int:
        """
        只有容量不足k或者大于小顶堆的堆顶
        """
        if len(self.vec) < self.k:
            self.push(val, fromBack=True)
        elif val > self.vec[0]:
            self.push(val, fromBack=False)
        return self.vec[0] if self.vec else -1