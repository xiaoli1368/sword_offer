#!/bin/bash python
"""
42. 接雨水

核心要点：明确当前位置能接到的雨水和什么有关，与两端最侧最大值有关
ret[i] = min(leftmax - height[i], rightmax - height[i])

思路一：
暴力遍历，每个位置都分别向左和向右找到最大值
根据大小情况，判断当前位置的存水量

思路二：
提起存储下来每个位置的左侧最大值和右侧最大值（需要两个数组）
然后遍历，直接根据左右两侧最大值的情况，判断存水量

思路三：
双指针法，一次双指针遍历就能找到
来自labuladong的高效资料

思路四：
单调栈

根据对水的求和方式，两种思路：
1. 按层，横向求和，找到当前位置处左右最近的max，高度为二者的min
   单调递减栈，存储下标
2. 按列，竖向求和，找到左侧所有和右侧所有的max，高度为二者的min
   可以直接定位当前最低点，然后左右两侧遍历
   也可以双指针法，从左右两端来更新max，根据两个max的大小情况
   一定可以确定一端的高度，进行累加
"""

class Solution(object):
    def trap1(self, height):
        """
        暴力方法，对每个当前位置，暴力寻找左侧最大值和右侧最大值
        时间复杂度O(n^2)，空间复杂度O(1)
        """
        ret = 0
        for i in range(len(height)):
            lmax = rmax = height[i]
            for j in range(0, i):
                lmax = max(lmax, height[j])
            for j in range(i + 1, len(height)):
                rmax = max(rmax, height[j])
            ret += min(lmax, rmax) - height[i]
        return ret
    
    def trap2(self, height):
        """
        提前存储法，实现存储好左侧最大值和右侧最大值
        """
        if height == []:
            return 0
        ret, n = 0, len(height)
        llist, rlist = [height[0]], [height[n - 1]]
        for i in range(1, n):
            llist.append(max(height[i], llist[-1]))
        for i in range(n - 2, -1, -1):
            rlist.append(max(height[i], rlist[-1]))
        for i in range(n):
            ret += min(llist[i], rlist[n - i - 1]) - height[i]
        return ret

    def trap3(self, height):
        """
        双指针法
        需要体会，当时遍历的指针有两个，l和r，分别从左右两端遍历
        首先更新各自的最大值，lmax，rmax
        注意lmax，rmax表示的含义分别指：l指针左侧，r指针右侧，的最大值
        因此当lmax < rmax时，l位置处的雨水量必然纸盒lmax有关了，反之同理
        """
        ret, l, r = 0, 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        while l <= r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                ret += lmax - height[l]
                l += 1
            else:
                ret += rmax - height[r]
                r -= 1
        return ret

    def trap4(self, height):
        """
        单调栈，存储下标
        """
        ret, stack = 0, []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                    diff_height = min(height[i], height[stack[-1]]) - bottom
                    ret += width * diff_height
            stack.append(i)
        return ret

if __name__ == "__main__":
    s = Solution()
    vec = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap1(vec))
    print(s.trap2(vec))
    print(s.trap3(vec))
    print(s.trap4(vec))