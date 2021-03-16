class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        原地hash
        """
        if nums == []:
            return
        
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                curr = nums[i]
                nums[i], nums[curr - 1] = nums[curr - 1], nums[i]
        
        ret = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ret.append(nums[i])
        return ret

    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        正常的原地hash需要两次遍历
        可以进行标签修改来实现O(n)，即将已经遍历过的元素，标记为相反数
        4 3 2 7 8 2 3 1
        7 3 2 4 8 2 3 1
        3 3 2 4 8 2 7 1
        2 3 3 4 8 2 7 1
        3 2 3 4 8 2 7 1
        -3 2 3 4 8 2 7 1 -> 3
        -3 2 3 4 1 2 7 8
        1 2 3 4 -3 2 7 8 -> 2
        1 2 3 4 -3 -2 7 8
        """
        ret = []
        for i in range(len(nums)):
            while nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if nums[i] > 0 and nums[i] != i + 1:
                ret.append(nums[i])
                nums[i] = -nums[i]
        return ret