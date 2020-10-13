#!/bin/bash python
"""
获取所有的topk最大值，返回一个数组
（直接堆排序法）

思路一：
自带的堆接口

思路二：
自行建堆
"""

import heapq

class Solution(object):
    def getAllTopK(self, num, k):
        """
        使用API
        因为heapq默认是小顶堆，因此要取相反数变为大顶堆
        每次pop出小顶，自动保证堆内有序
        """
        tmp = []
        vec = [-x for x in num] # 拷贝同时取相反数
        heapq.heapify(vec)      # 构建小顶堆
        for _ in range(k):
            tmp.append(-heapq.heappop(vec))
        return tmp

    def heapify(self, num, n, i):
        """
        heapify的本意是堆化 
        建立大顶堆，最大值位置保证为索引为i
        其实这个函数的作用是下沉一次，假定i是新加入的一个节点
        这里只考虑根节点i，左子树l，右子树r
        不满足大顶关系，则交换，然后递归下一层，直到这个元素到了满足的位置
        因此，如果当前层满足大小关系，则不上浮，否则交换去递归下一棵子树
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and num[i] < num[l]: # 这里很神奇，必须保证是largest，因为影响到下一层了
            largest = l
        if r < n and num[i] < num[r]:
            largest = r
        if largest != i:
            num[largest], num[i] = num[i], num[largest]
            self.heapify(num, n, largest)

    def getAllTopK2(self, num, k):
        """
        自行构建堆，求topk
        """
        n = len(num)
        # 从
        for i in range(n, -1, -1):
            self.heapify(num, n, i)
        for i in range(n - 1, 0, -1):
            num[i], num[0] = num[0], num[i]
            self.heapify(num, i, 0)
        return num

if __name__ == "__main__":
    k = 5
    num = [3, 0, 5, 8, 3, 3, 4, 9, 1]
    s = Solution()
    print(num)
    print(s.getAllTopK(num[:], k))
    print(s.getAllTopK2(num[:], k))