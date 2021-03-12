#!bin/bash python
"""
1000. 合并石头的最低成本

思路：
分治，递归，记忆化搜索，直到DP

1. 什么情况下无法合并为一堆？
   每次合并会减少k-1个石头，要求最终剩余1个石头，因此条件为：n % (k - 1) == 1 ?
   最终整理为：k==1满足，否则判断(n-1)%(k-1)==0
2. 检索空间：第1次可选的合并方案有n+1-k种，最后1次有1种，遍历复杂度为O((n+1-k)!)
3. 直接递归：每次选择长为k的区间合并为1个元素，然后生成新的list递归下一层
   注意这种方法其实是DFS的先序遍历，先计算了根节点，也就是当前层的合并选择，然后递归计算后续层
   缺点：1) 大量传递新的list，而非引用。2) 大量重复的遍历节点
4. 改进递归：修改拷贝list为引用，不去生成新的下一层list，此时需要明确递归子问题的分治策略
   之前的策略是，将当前的N堆，选取一个区间合并为1堆，然后整体再合并为1堆
   这种方式等价，将当前的N堆，选定一个区间合并为1堆，然后其余的区间合并为k-1堆，然后这k堆合并为1堆
   关于划分方式，之前是选定一个长为k的连续区间，现在要想不生成新的list，必须在原list上操作划分
   现在划分方式，将区间[i:j]划分为[i:m]和[m+1:j]，左侧合并为1堆，右侧合并为k-1堆，然后整体合并为1堆
5. 动态规划：自底向上生成某个区间的最优合并结果
   dp[i][j][k]表示区间[i:j]合并为k堆的最小成本
   if k = 1: dp[i][j][k] = dp[i][j][kk] + sum(stones[i:j])
   if k > 1: dp[i][j][k] = dp[i][m][1] + dp[m+1][j][k-1]
   注意到i依赖于更大的值，j依赖更小的值，同一位置的[i,j]下的k依赖更大的值
   因此i和k从大到小遍历，j从小到大遍历，m正常从i到j遍历即可
   保证i<=j，否则表示区间为空，成本为0，而k=0也表示花费为0
6. 动态规划优化: 之前的版本存在冗余，例如dp[i][j][k]表示区间[i:j]合并为k堆的最小成本
   有的情况下dp[i][j][k]必定无意义，没有必有去遍历
   优化版的状态定义：dp[i][j]表示区间[i:j]合并为最少堆的最小成本
"""

class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        简单递归方法
        缺点 1. 大量传递新的list，而非引用
        缺点 2. 大量重复的遍历节点
        """
        # 特殊情况
        n = len(stones)
        if n <= 1 or k <= 1:
            return 0
        if k != 2 and n % (k - 1) != 1:
            return -1
        # 递归分治，当前合并区间为：[i:i+k]
        ret = float("+inf")
        for i in range(n - k + 1):
            currScore = sum(stones[i:i+k])
            nextStones = stones[:i] + [currScore] + stones[i+k:]
            nextScore = self.mergeStones(nextStones, k)
            ret = min(ret, currScore + nextScore)
        return ret

    def mergeStones2(self, stones, k):
        """
        改进的递归法
        改进：将stones的拷贝改为了引用
        缺点：使用了float("+inf)来表示无法完成的情况
        """
        def merge(stones, kk, i, j, k):
            """
            表示在每次允许合并kk堆情况下，将[i:j]合并为k堆的最小成本
            k > n, 无法完成
            k = 0, 本来就满足要求，返回0
            k = 1, 先确定能否合成，然后将[i:j]合并为kk堆，然后进行最后一次合并
                dp[i][j][k] = dp[i][j][kk] + sum(dp[i:j])
            k > 1, 先将[i:j]划分出左侧区间[i:m]来合成1堆，剩余的[m+1:j]合成k-1堆
                dp[i][j][k] = dp[i][m][1] + dp[m+1][j][k-1]，对m遍历，同时取最小值
            """
            n = j - i + 1
            ret = float("+inf")
            if k > n: # 无法增加堆数
                return ret
            elif k == n: # 本来就满足要求
                return 0
            elif k == 1: # 合并为1堆
                if (n - 1) % (kk - 1) != 0: # 无法合并
                    return ret
                elif n == kk: # 可以直接一次操作完成
                    return sum(stones[i:j+1])
                else: # 需要多次操作完成
                    return merge(stones, kk, i, j, kk) + sum(stones[i:j+1])
            else: # 合并为多堆
                for m in range(i, j):
                    left = merge(stones, kk, i, m, 1)
                    right = merge(stones, kk, m + 1, j, k - 1)
                    ret = min(ret, left + right)
                return ret
        # ===================================================
        return merge(stones, k, 0, len(stones) - 1, 1)

    def mergeStones3(self, stones, k):
        """
        改进的递归法
        1. 使用了lru缓存（相当于记忆化搜素）
        2. 增加了前缀和优化
        3. 考虑了输出-1
        4. 优化了条件分支
           划分区间后须满足的条件：[i:m] -> (m - i + 1 - 1) % (kk - 1) == 0
                                 [m+1:j] -> j - m - 1 + 1 >= k - 1
                                 m <= j - k + 1
                                 m = i + p * (kk - 1), p为整数
                                 m = range(i, j - k + 2, kk - 1)
        """
        curr, preSum = 0, [0]
        for stone in stones:
            curr += stone
            preSum.append(curr)
        from functools import lru_cache
        @lru_cache()
        def merge(kk, i, j, k):
            n = j - i + 1
            ret = float("+inf")
            if k > n or (k == 1 and (n - 1) % (kk - 1) != 0): # 无法完成合并
                return ret
            elif k == n: # 已经满足要求
                return 0
            elif k == 1:
                return merge(kk, i, j, kk) + preSum[j+1] - preSum[i] 
            else: # 合并为多堆
                for m in range(i, j - k + 2, kk - 1):
                    left = merge(kk, i, m, 1)
                    right = merge(kk, m + 1, j, k - 1)
                    ret = min(ret, left + right)
                return ret
        # ===================================================
        ret = merge(k, 0, len(stones) - 1, 1)
        return ret if ret != float("+inf") else -1

    def mergeStones4(self, stones, kk):
        """
        :type stones: List[int]
        :type kk: int
        :rtype: int
        动态规划
        dp[i][j][k]表示区间[i:j]合并为k堆的最小成本
        if k = 1: dp[i][j][k] = dp[i][j][kk] + sum(stones[i:j])
        if k > 1: dp[i][j][k] = dp[i][m][1] + dp[m+1][j][k-1]
        注意到i依赖于更大的值，j依赖更小的值，k依赖更大的值
        因此i和k从大到小遍历，j从小到大遍历，m正常从i到j遍历即可
        保证i<=j，否则表示区间为空，成本为0，而k=0也表示花费为0
        """
        n = len(stones)
        preSum = [0] * (n + 1)
        dp = [[[0] * (kk + 1) for _ in range(n)] for _ in range(n)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                for k in range(kk, 0, -1):
                    r = j - i + 1
                    if k > r or (k == 1 and (r - 1) % (kk - 1) != 0):
                        dp[i][j][k] = float("+inf")
                    elif k == r:
                        dp[i][j][k] = 0
                    elif k == 1:
                        dp[i][j][k] = dp[i][j][kk] + preSum[j+1] - preSum[i]
                    else:
                        dp[i][j][k] = float("+inf")
                        for m in range(i, j - k + 2, kk - 1):
                            dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
        return -1 if dp[0][n-1][1] == float("+inf") else dp[0][n-1][1]

    def mergeStones5(self, stones, kk):
        """
        :type stones: List[int]
        :type kk: int
        :rtype: int
        动态规划
        之前的版本存在冗余，例如dp[i][j][k]表示区间[i:j]合并为k堆的最小成本
        有的情况下dp[i][j][k]必定无意义，没有必有去遍历

        优化版的状态定义：dp[i][j]表示区间[i:j]合并为最少堆的最小成本
        1. 当前区间由m进行划分，左侧合并为1堆，右侧合并为尽可能少的堆，dp[i][m] + dp[m+1][j]
        2. 划分之前的划分，如果当前层最终可以合并为1堆，则花费sum(stones[i:j])，否则花费0
        curr_cost = sum(stones[i:j]) if (j - 1) % (kk - 1) == 0 else 0
        dp[i][j] = min(dp[i][j], dp[i:m] + dp[m+1:j] + curr_cost)
        注意到i依赖于更大的值，j依赖更小的值，因此i从大到小，j从小到大遍历，m正常从i到j遍历
        保证i<=j，否则表示区间为空，成本为0，而k=0也表示花费为0
        此时对于一些没有意义的遍历区间dp[i][j][k]，则不进行处理，初始化为0，表示不处理

        最终的结果无法表示可以合并为1堆，所以需要提前判断
        """
        n = len(stones)
        if (n - 1) % (kk - 1) != 0:
            return -1
        preSum = [0] * (n + 1)
        dp = [[0] * n for _ in range(n)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                mmin_cost = float("+inf")
                for m in range(i, j, kk - 1):
                    curr_cost = (preSum[j+1] - preSum[i]) if (j - i) % (kk - 1) == 0 else 0
                    mmin_cost = min(mmin_cost, dp[i][m] + dp[m+1][j] + curr_cost)
                dp[i][j] = mmin_cost if mmin_cost != float("+inf") else 0
        return dp[0][n-1]


if __name__ == "__main__":
    import time
    k = 3
    s = Solution()
    stones = [3, 5, 1, 2, 6, 4, 7, 9, 2, 1, 5, 4, 3, 2, 6]

    start = time.time()
    ret = s.mergeStones(stones, k)
    end = time.time()
    print("result: {}, time(ms): {}".format(ret, (end - start) * 1e6))

    start = time.time()
    ret = s.mergeStones2(stones, k)
    end = time.time()
    print("result: {}, time(ms): {}".format(ret, (end - start) * 1e6))

    start = time.time()
    ret = s.mergeStones3(stones, k)
    end = time.time()
    print("result: {}, time(ms): {}".format(ret, (end - start) * 1e6))

    start = time.time()
    ret = s.mergeStones4(stones, k)
    end = time.time()
    print("result: {}, time(ms): {}".format(ret, (end - start) * 1e6))

    start = time.time()
    ret = s.mergeStones5(stones, k)
    end = time.time()
    print("result: {}, time(ms): {}".format(ret, (end - start) * 1e6))