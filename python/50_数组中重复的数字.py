#!/bin/python3
#-*- coding:utf-8 -*-

class solution():
    def duplicate1(self, numbers, duplication):
        """
        第一次的解法
        需要赋值到duplication[0]
        函数返回bool
        """
        i = 0
        while (i < len(numbers)):
            if numbers[i] == i:
                i += 1
            elif numbers[i] != numbers[numbers[i]]:
                index = numbers[i]
                numbers[i], numbers[index] = numbers[index], numbers[i]
            else:
                duplication[0] = numbers[i]
                return True
        return False

    def duplicate2(self, nums, duplication):
        """
        单层循环优化版
        """
        i = 0
        while (i < len(nums)):
            if nums[i] == i:
                i += 1
            elif nums[i] == nums[nums[i]]:
                duplication[0] = nums[i]
                return True
            else:
                # 注意顺序不能改变
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return False

    def duplicate3(self, nums, duplication):
        """
        hash版
        """
        tmp = []
        for i in nums:
            if tmp.count(i) == 0: # 或者使用 if i in tmp:
                tmp.append(i)
            else:
                duplication[0] = i
                return True
        return False

    def duplicate4(self, nums, duplication):
        """
        dict版
        """
        tmp = {}
        for i in nums:
            if i not in tmp:
                tmp[i] = i
            else:
                duplication[0] = i
                return True
        return False

    def duplicate(self, nums, duplication):
        """
        双层循环优化版，最终版
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    duplication[0] = nums[i]
                    return True
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return False

    def test(self, nums, duplication):
        """
        测试函数
        """
        func_vec = [self.duplicate1,
                    self.duplicate2,
                    self.duplicate3,
                    self.duplicate4,
                    self.duplicate]
        for func in func_vec:
            # 注意不能传递引用
            tmp_nums = nums[:]
            tmp_dupl = duplication[:]
            print(func(tmp_nums, tmp_dupl), tmp_dupl[0])


def main():
    nums = [2, 3, 1, 0, 2, 5, 3]
    duplication = [0]
    s = solution()
    s.test(nums, duplication)


if __name__ == "__main__":
    main()