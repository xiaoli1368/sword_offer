#!/bin/bash python
"""
1793. 好子数组的最大分数

思路：
见注释
"""

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        类似最大矩形，分数和区间内部的最小值有关
        暴力方法：选定每个元素为最小值，左右两侧向更大的方向延申
        单调栈法：每个元素找到左右两侧最近的更小的元素位置[x, y]，则[x+1:y-1]为目标区间
                 单调递增栈，保存下标，注意增加前后0，栈内增加-1，并且k+1
        双指针法：由于要求i<=k<=j，则直接选定位置j向两端更大的方向遍历，优先移动更大值
        """
        ret, stack = 0, [-1]
        nums = [0] + nums + [0]
        for x in range(len(nums)):
            while len(stack) >= 2 and nums[stack[-1]] > nums[x]:
                min_val = nums[stack.pop()]
                i, j = stack[-1] + 1, x - 1
                if i <= k + 1 <= j:
                    ret = max(ret, min_val * (j - i + 1))
            stack.append(x)
        return ret

    # ===== 简化版（不易理解） =====
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        单调栈法：每个元素找到左右两侧最近的更小的元素位置[x, y]，则[x+1:y-1]为目标区间
                 单调递增栈，保存下标，注意增加前后0，栈内增加-1，并且k+1
        """
        ret, stack = 0, [-1]
        nums = [0] + nums + [0]
        for x in range(len(nums)):
            while len(stack) > 1 and nums[stack[-1]] > nums[x]:
                min_val = nums[stack.pop()]
                if stack[-1] <= k <= x - 2:
                    ret = max(ret, min_val * (x - stack[-1] - 1))
            stack.append(x)
        return ret

    # ===== 双指针法（错误版本） =====
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        双指针法：贪心，选定k索引后，向左右更大的区间进行遍历
        区间[i:j]表示合法的区间，并且最小值为mmin=nums[k]，初始ret为mmin
		当前版本错误，无法解决 [1, 4, 3, 7, 4, 5] 0
		根本原因在于mmin的更新有问题，mmin应该有机会变大
        """
        i = j = k
        n = len(nums)
        ret = mmin = nums[k]
        while 0 <= i and j < n:
            mmin = min(mmin, nums[i])
            mmin = min(mmin, nums[j])
            ret = max(ret, mmin * (j - i + 1))
            if i == 0 and j == n - 1:
                break
            if i == 0 or (j < n - 1 and nums[i] < nums[j]):
                j += 1
            else:
                i -= 1
        return ret

    # ===== 双指针（正解） =====
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        双指针，不太好理清楚，[i, j]为目标区间
        移动左右指针找到满足提交的区间，然后更新结果，没有后续遍历区间则退出
		注意更新时不是更新指针，而是贪心的去更新mmin，使其变大，并且尽可能更缓慢的变大
		注意两端有可能遇到边界
        """
        n = len(nums)
        i = j = k
        ret = mmin = nums[k]
        while True:
            # 找到左右两侧以mmin为最小值的边界
            while i - 1 >= 0 and nums[i - 1] >= mmin:
                i -= 1
            while j + 1 < n and nums[j + 1] >= mmin:
                j += 1
            # 更新结果
            ret = max(ret, mmin * (j - i + 1))
            # 退出循环的条件是全部遍历完成
            if i == 0 and j == n - 1:
                break
            # 更新mmin，优先贪心使用更大的一端作为min
            if i - 1 >= 0 and j + 1 < n:
                mmin = max(nums[i - 1], nums[j + 1])
            elif i - 1 < 0:
                mmin = nums[j + 1]
            elif j + 1 == n:
                mmin = nums[i - 1]
        return ret