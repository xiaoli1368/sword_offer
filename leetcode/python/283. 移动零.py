#!/bin/bash python
"""
283. 移动零

思路：
0. 常见思路：冒泡排序，或者插入排序（本质上还是一个排序问题）
1. 快排分区，双指针，左指针指向已经排好部分的结尾，右指针指向待排的头部

举一反三：
1. 如果要求把0放到末尾，同时其它元素从小到大排序。（排序问题，直接快排）
2. 要求把0放到开头，其它元素保持相对顺序。（快排分区，从右往左）
3. 要求两个非零元素之前嵌入一个零，保持相对顺序，注意0过多时放到后面，也有可能0过少
  （这个题目有点意思，最直接的方法就是使用额外数组，如果要求空间O(1)，可以先用本体的思路）
  （先是快排分区，实现把所有的0移动到前端，然后遍历插入非零值，类似第二次的快排分区，注意间隔）
  （这个题目好像不能直接一次快排分区实现，因为步进为2时，start移动的比i快了，无法判断后续有没有0）
4. 一个数组，只含有0/1/2三种元素，把放到开头，2放到末尾。
  （一次遍历，两个快排分区，同时向左向右放置0和2，三指针，注意当前p1指针跳变的条件，见leetcode75）
5. 一个数组，把0放到开头，把1放到末尾，其它元素保持相对顺序。
  （错误方式：一次快排分区0放首，二次快排分区1放尾，这样会导致乱序）
  （错误方式：一次遍历记录0的个数，以及非0/1值个数，然后把非0/1值搬移到目标位置，再填充前后的0/1，错误因为目标位置和当前位置重叠）
  （暴力方式：快排分区，把非0/1值有序搬移到前半部分，记录长度以及0值长度，此时0/1值在后但是乱序，但不影响搬移，从最后一个搬移）
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        最优思路：双指针，快排分区
        """
        if nums == []:
            return []
        start = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                start += 1
                nums[i], nums[start] = nums[start], nums[i]
        return nums
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        思路一：
        冒泡
        """
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] == 0 and nums[j + 1] != 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        思路二：
        快排不行，因为不稳定，不能保证原始的顺序
        可以使用插排
        """
        for i in range(1, len(nums)):
            curr = nums[i]
            j = i - 1
            while j >= 0 and nums[j] == 0:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = curr