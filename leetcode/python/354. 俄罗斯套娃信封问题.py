#!/bin/bash python
"""
354. 俄罗斯套娃信封问题

思路：动态规划
1. 直接对area排序，然后两重循环的dp，其实就是对[len, hei]均递增排序，O(n^2) + O(n)
2. 考虑为什么出现了两重循环，因为len依次递增，hei依次递增，但二者组合就不一定递增了
   考虑[[2, 3], [5, 4], [6, 5], [6, 7]]，对length已经排序，如果直接对height求最长递增子序列
   结果为[3, 4, 5, 7]，但是显然错误，因为[6, 5]不能被[6, 7]包含，也就是当存在length相等的时候
   height不能升序，而应该反序来表面相同的length不能包含，因此整体的思路就是length升序，hegiht降序
   然后在height上进行求最长递增子序列，O(n^2) + O(n)
3. 在此基础上，使用二分对LIS进行优化，O(nlogn) + O(n)
4. follow up: 如果允许旋转信封呢？也就是[len,hei]可以互换，则第一种方法是ok的
   能否先互换保证length更小，然后使用第二种方法呢？好像不行，不能确定互换是否就一定是好的。
5. follow up：升级为三维，也就是嵌套箱子呢？直接递推到三维是不行的，这是一个偏序问题，需要树状数组
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        如果信封A可以被B装下，则必有：A.length < B.length, A.height < B.height
        因此必然有：A.area < B.area
        所以可以使用面积来排序，但是面积存在大小关系，不一定各边长同样大小
        """
        if envelopes == []:
            return 0
        
        vec = envelopes
        n = len(envelopes)
        vec.sort(key=lambda x : x[0] * x[1])
        ret, dp = 1, [1] * n

        for i in range(n):
            for j in range(i):
                if vec[j][0] < vec[i][0] and vec[j][1] < vec[i][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ret = max(ret, dp[i])
        return ret

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        方法二，在height上进行LIS
        """
        if envelopes == []:
            return 0
        
        vec = envelopes
        n = len(envelopes)
        vec.sort(key=lambda x : (x[0], -x[1]))
        ret, dp = 1, [1] * n

        for i in range(n):
            for j in range(i):
                if vec[j][1] < vec[i][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ret = max(ret, dp[i])
        return ret

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        方法二，在height上进行LIS
        """
        if envelopes == []:
            return 0
        
        vec = envelopes
        dp, n = [], len(envelopes)
        vec.sort(key=lambda x : (x[0], -x[1]))

        # 在vec[:][1]上进行LIS
        for i in range(n):
            target = vec[i][1]
            if dp == [] or dp[-1] < target:
                dp.append(target)
                continue
            # 进行二分，找到dp中最左侧的大于target的索引
            l, h = 0, len(dp) - 1
            while l < h:
                m = (l + h) // 2
                if dp[m] < target:
                    l = m + 1
                else:
                    h = m
            dp[l] = target
        return len(dp)