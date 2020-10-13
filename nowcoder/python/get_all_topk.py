#!/bin/bash python
"""
获取所有的topk最大值，返回一个数组
（直接堆排序法）

思路一：
自带的堆接口

思路二：
自行建堆

关于建堆也有不同的选择方式：
使用大顶堆，对整个vec建堆，每次取堆顶最大值，这样取k次即可
使用小顶堆，对前k个数建堆，每次取后面的元素与堆顶比较，这样取n-k次
（两种方式对比，方式一得到的k个值是有序的，方式二得到的结果未必有序）
"""

import heapq

class Solution(object):
    def getAllTopK_bigheap(self, num, k):
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
	
    def getAllTopK_smallheap(self, num, k):
        """
        维护一个长度为k的小顶堆，每次与堆顶比较并添加元素
        返回结果是topk，未必有序，只是满足小顶堆关系
        """
        vec = []
        for i in range(len(num)):
            if i < k: # 前k个元素直接添加
                heapq.heappush(vec, num[i])
            elif num[i] > vec[0]:
                heapq.heappushpop(vec, num[i])
        return vec

    def heapify_bigheap(self, num, n, i):
        """
        heapify的本意是堆化
        n控制的是num中建堆的长度
        i表示当前下沉的位置（下沉后i处应是该子树的最大值）
        这个函数的作用是：对num数组前n个数建队，同时从i位置开始下沉，最终保证i为最大值
        根节点i，左子树l，右子树r
        三者如果满足大顶关系，则停止（这只表示当前这一层，三个数满足关系，不必下浮，但是下一层未必满足）
        如果当前层不满足，则交换，然后递归下一层，直到原本i处的元素到了满足的位置（下浮到合适位置）
        因此，要想整颗树大顶，需要从底到顶调用下沉函数
        """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and num[largest] < num[l]:
            largest = l
        if r < n and num[largest] < num[r]:
            largest = r
        if largest != i:
            num[largest], num[i] = num[i], num[largest]
            self.heapify_bigheap(num, n, largest)
    
    def heapify_smallheap(self, num, n, i):
        """
        小顶堆的下沉
        """
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and num[smallest] > num[l]:
            smallest = l
        if r < n and num[smallest] > num[r]:
            smallest = r
        if smallest != i:
            num[smallest], num[i] = num[i], num[smallest]
            self.heapify_smallheap(num, n, smallest)

    def getAllTopK2_bigheap(self, num, k):
        """
        自行构建堆，求topk
        """
        n = len(num)
        # 从第末尾位置开始建堆（大顶堆）
        for i in range(n - 1, -1, -1):
            self.heapify_bigheap(num, n, i)
        # 依次交换堆顶与堆尾，然后下浮保证堆顶为最大值，交换k次
        for i in range(n - 1, n - k - 1, -1):
            num[i], num[0] = num[0], num[i]
            self.heapify_bigheap(num, i, 0)
        # 输出倒数的k个元素
        return num[-k:]
    
    def getAllTopK2_smallheap(self, num, k):
        """
        自行编写，维护一个长度为k的小顶堆
        """
        n = len(num)
        vec = num[0:k]
        for i in range(k - 1, -1, -1):
            self.heapify_smallheap(vec, k, i)
        for i in range(k, n):
            if num[i] > vec[0]:
                vec[0] = num[i]
                self.heapify_smallheap(vec, k, 0)
        return vec

if __name__ == "__main__":
    k = 5
    num = [3, 0, 5, 8, 3, 3, 4, 9, 1]
    s = Solution()
    print(num)
    print(s.getAllTopK_bigheap(num[:], k))
    print(s.getAllTopK_smallheap(num[:], k))
    print(s.getAllTopK2_bigheap(num[:], k))
    print(s.getAllTopK2_smallheap(num[:], k))
