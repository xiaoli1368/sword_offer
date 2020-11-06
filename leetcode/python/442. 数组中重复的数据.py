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