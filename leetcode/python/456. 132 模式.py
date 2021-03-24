#!/bin/bash python
"""
456. 132 模式

思路：
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1. 暴力方法：三重循环，O(n^3)
        2. 优化方法：由于下标满足 i < j < k，取值满足 a[i] < a[j] > a[k], a[i] < a[k]
                    先选定j，然后分别左右进行延申，贪心的策略
                    a[i]取左侧比a[j]小的最小值，a[k]取右侧比a[j]小的最大值，O(n)
                    总体的复杂度O(n^2)
        3. 优化方法：需要求出a[j]右侧比a[j]小的最大值，考虑右侧的单调递减栈
                    从后往前遍历的单调递减栈，-1 3 2 0
                    当不满足递减时，说明存在了 a > b的关系，依次弹出b，最后一个弹出的
                    就是小于a的最大值
        4. 思考问题：由于采用了右侧的反向单调递减栈，当扫描nums[i]时，需要弹出所有比nums[i]小的元素
                    最后一个弹出的就是比nums[i]小的最大元素，那么存在一个问题，是否弹出的那些元素后续场景会使用到？
                    例如：[4, 5, 1, 2, 3, 6]
                    可以发现对应5，需要连续弹出[1, 2, 3]才能找到比5小的最大元素是3
                    如果3满足要求，则返回true，如果不满足要求，则说明left_min >= 3
                    此时遍历5的左侧元素4时，一定有left_min>=3，之前弹出的[1, 2]没有影响
                    注意本次的3也会被记录到下一次中判断
        """
        n = len(nums)
        right_st, left_min = [], [float("+inf")] * n
        # 左侧最小值
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        # 右侧单调栈找特定的最大值
        for i in range(n - 1, -1, -1):
            curr, left, right = nums[i], left_min[i], float("-inf")
            while right_st and right_st[-1] < curr:
                right = right_st.pop()
            right_st.append(curr)
            if left < right < curr:
                return True
        return False

    # ===== 优化版 =====
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        对应(i, j, k)需要实现(1, 3, 2)的大小模式
        贪心思路：设定i为j左侧的最小值，设定k为j右侧比j小的最大值，然后判断是否为132
                 左侧直接遍历更新left_min，右侧反向单调递减栈right_stack，获取更小的最大值
        高效思路：在反向单调栈的时候，同时枚举(i, j)，此时并不要求i为j左侧的最小值，而是i为j左侧更小的值即可
                 由于单调递减栈，因此总能保证 j > k，并且上一次的i与本次的j是重叠的
                 因此先判断 上次i < 上次k
                 然后去更新 本次j   本次k
        """
        lastk, stack = float("-inf"), []
        for j in range(len(nums) - 1, -1, -1):
            lasti = currj = nums[j]
            if lasti < lastk:
                return True
            while stack and stack[-1] < currj:
                lastk = stack.pop()
            stack.append(nums[j])
        return False