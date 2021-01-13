#!/bin/bash python
"""
128. 最长连续序列

牛客网有同样的题目：
https://www.nowcoder.com/practice/eac1c953170243338f941959146ac4bf?tpId=117&&tqId=35017&rp=1&ru=/ta/job-code-high&qru=/ta/job-code-high/question-ranking

思路：
1. 暴力思路：排序，然后依次遍历，O(nlogn) + O(1)
2. 优化思路：哈希，先用set去重，然后任选一个num开始，左右开始扫描，依次判断num+1, num-1是否位于set中
            复杂度是，O(n^2) + O(n)
3. 高效思路：哈希， 在方法二的基础上，思考O(n^2)的冗余在于，每个都要向两端扫描，例如对[1,2,3,4,5]，
            在外层选择2或者3时，会出现重复扫描，因此高效思路是每次只从首端扫描，也就是每个扫描前判断
            num-1是否存在，只要num-1不存在时，说明遇到了首端，此时进入内部循环，复杂度是，O(n) + O(n)
4. 高效思路：哈希，key=(num, dire)，value=length，使用hash来统计数组内每个元素的信息
            分布表示以num为端点，向左/向右延申的最大连续序列长度，依次进行更新，复杂度是，O(n) + O(n)
5. 高效思路：哈希，在方法二的基础上，发现不需要区分方向，直接记录以num为端点的最大连续区间长度即可
            例如对num，left=d[num-1]，可以明确d[num-1]中一定不包含向右延申的情况，
            如果包含了则说明num已经被遍历过了。所以内部循环中需要在字典中添加num，其val可以是任意值
            只要表明已经遍历过即可，复杂度是，O(n) + O(n)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序扫描法
        """
        ret = 0
        nums.sort()

        # 双指针滑窗，cnt统计窗口内重复的数字个数
        i = j = cnt = 0
        while j < len(nums):
            if j + 1 < len(nums):
                if nums[j] == nums[j + 1]:
                    cnt += 1
                elif nums[j] + 1 < nums[j + 1]:
                    ret = max(ret, j + 1 - i - cnt)
                    cnt = 0
                    i = j + 1
            j += 1

        return max(ret, j - i - cnt)

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序扫描法，优化版
        """
        if nums == []:
            return 0
        
        vec = list(set(nums))
        vec.sort()

        # 双指针滑窗，[l, h)
        l, h, ret, n = 0, 1, 1, len(vec)
        while h < n:
            # 移动右指针
            while h < n and vec[h] == vec[h - 1] + 1:
                h += 1
            # 获取结果
            ret = max(ret, h - l)
            # 移动左右指针
            l = h
            h += 1
        return ret

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        哈希，暴力扫描
        """
        if nums == []:
            return 0
        
        ret = 0
        d = set(nums)
        vec = list(set(nums))

        for i in vec:
            # 当前长度
            length = 1
            left = right = i
            # 扫描左侧长度
            while left - 1 in d:
                left -= 1
                length += 1
            # 扫描右侧长度
            while right + 1 in d:
                right += 1
                length += 1
            # 更新
            ret = max(ret, length)
        return ret

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        哈希，只寻找首端位置进行扫描，高效思路
        """
        if nums == []:
            return 0
        
        ret = 0
        d = set(nums)
        vec = list(set(nums))

        for i in vec:
            if i - 1 not in d: # 保证首端位置，扫描右侧长度
                length = 1
                while i + 1 in d:
                    i += 1
                    length += 1
                ret = max(ret, length)
        return ret

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        哈希，确定每个元素的左右延申长度
        """
        if nums == []:
            return 0
        
        left, right = 0, 1
        vec = list(set(nums))
        ret, d = 0, dict()

        for i in vec:
            if (i, left) not in d and (i, right) not in d:
                l = d.get((i - 1, left), 0)
                r = d.get((i + 1, right), 0)
                length = 1 + l + r
                ret = max(ret, length)
                # 添加
                d[(i, left)] = 1 + l
                d[(i, right)] = 1 + r
                d[(i - l, right)] = length
                d[(i + r, left)] = length
        return ret

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        哈希，确定每个元素的左右延申长度
        """
        if nums == []:
            return 0
        
        vec = list(set(nums))
        ret, d = 0, dict()

        for i in vec:
            if i not in d:
                left = d.get(i - 1, 0)
                right = d.get(i + 1, 0)
                length = 1 + left + right
                ret = max(ret, length)
                # 注意以下[i]只是为了包括i为key，取值无所谓
                # 但是不能最后对d[i]赋值，否则有可能会影响d[i-left]和d[i+right]
                # 高效写法 d[i] = d[i - left] = d[i + right] = length
                d[i] = length
                d[i - left] = length
                d[i + right] = length
        return ret