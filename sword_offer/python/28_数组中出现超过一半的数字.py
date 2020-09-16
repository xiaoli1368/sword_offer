#!/bin/bash python3 
#-*- coding:utf-8 -*-

import time

class Solution():
    def MoreThanHalfNum_Solution1(self, nums):
        """
        排序法，直接输出索引为length//2的元素
        没有考虑：不存在超过一半的数字
        """
        if nums == []:
            return 0
        
        nums.sort()
        return nums[len(nums) // 2]
 
    def MoreThanHalfNum_Solution2(self, nums):
        """
        排序法
        实际检测了是否存在长度超过一半的数字
        """
        if nums == []:
            return 0

        nums.sort()
        length = len(nums)
        first = 0
        end = first + length // 2

        while end < length:
            if nums[first] == nums[end]:
                return nums[first]
            first += 1
            end += 1
        
        return 0

    def MoreThanHalfNum_Solution3(self, nums):
        """
        dict法
        """
        if nums == []:
            return 0
        
        dic = dict()
        for i in nums:
            if dic.get(i) == None:
                dic[i] = 1
            elif dic[i] == len(nums) // 2:
                return i
            else:
                dic[i] += 1
        
        return 0

    def MoreThanHalfNum_Solution(self, nums):
        """
        高效方法
        多数投票法，复杂度是O(n)
        """
        if nums == []:
            return 0
        
        curr_val = 0
        curr_cnt = 0

        for i in nums:
            if curr_cnt == 0:
                curr_cnt = 1
                curr_val= i
            else:
                curr_cnt += 1 if curr_val == i else -1
        
        # 此时有可能不存在大于一半的数字
        if curr_cnt == 0:
            return 0
        
        return curr_val
    
    def test(self, nums):
        """
        测试函数
        """
        func_vec = [self.MoreThanHalfNum_Solution1,
                    self.MoreThanHalfNum_Solution2,
                    self.MoreThanHalfNum_Solution3,
                    self.MoreThanHalfNum_Solution]
        for func in func_vec:
            tmp_nums = nums[:]
            start = time.time()
            result = func(tmp_nums)
            end = time.time()
            print("result: {}, time(us): {:>5.2f}".format(result, (end - start)*10**6))


def main():
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    s.test(nums)


if __name__ == "__main__":
    main()