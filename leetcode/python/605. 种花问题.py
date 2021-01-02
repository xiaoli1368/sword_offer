#!/bin/bash python
"""
605. 种花问题

思路：
1. 问题抽象，在仅含有0/1的数组中，能否翻转k个0为1，满足没有1相邻
2. 暴力解法，假设原数组有m个0，则枚举时间复杂度为O(2^m)，因为每个0都有翻转或者不翻转两种情况，最终统计可以翻转0的总个数是否达到了k个
3. 优化空间，对暴力加法的实现为dfs回溯，常用的优化就是剪枝了。（1）使用cnt统计当前已经成功翻转0的个数，当cnt达到k时直接退出。（2）思考最优解的选择，例如对[1, 0, 0, 0, 0, 1]这种情况，显然在两个1之间只能翻转1个0，但是应该优先选择靠左侧的0，因为这样可以给后面的子问题更优的条件，因此这是一个贪心的解。
4. 算法流程：（1）依次遍历数组，找到满足情况的可翻转的0，进行翻转为1.（2）统计cnt。
"""

class Solution(object):
    def canPlaceFlowers(self, k, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
		早期个人版本
        """
        if k == [] or n < 0 or n > len(k):
            return False
        
        cnt = 0
        for i in range(len(k)):
            l = i - 1 if i > 0 else i
            h = i + 1 if i < len(k) - 1 else i
            if k[l] + k[i] + k[h] == 0:
                k[i] = 1 
                cnt += 1
        
        return cnt >= n

    def canPlaceFlowers(self, vec: List[int], n: int) -> bool:
        """
        后期个人版本
        依次遍历，找到所有可能把0变为1的位置
        """
        cnt = 0
        for i in range(len(vec)):
            if vec[i] == 1 or (i - 1 >= 0 and vec[i - 1] == 1) or (i + 1 < len(vec) and vec[i + 1] == 1):
                continue 
            else:
                vec[i] = 1
                cnt += 1
                if cnt >= n:
                    break
        return cnt >= n
	
    def canPlaceFlowers(self, vec: List[int], n: int) -> bool:
        """
        优化版
        依次遍历，找到所有可能把0变为1的位置
        """
        cnt = 0
        for i in range(len(vec)):
            if vec[i] == 0 and (i - 1 < 0 or vec[i - 1] == 0) and (i + 1 >= len(vec) or vec[i + 1] == 0):
                vec[i] = 1
                cnt += 1
                if cnt >= n:
                    break
        return cnt >= n