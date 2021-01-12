#!/bin/bash python
"""
牛客. 回文数字

思路：
1. 转换为字符串，然后进行字符串的比较
2. 转换为int数组，保存各个数位上的数字，然后比较
3. 直接循环依次取出left/right数字进行比较
4. 直接循环操作，获取翻转后的数字（注意溢出问题）
"""

# @param x int整型 
# @return bool布尔型
#
class Solution:
    def isPalindrome(self , x):
        # write code here
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
	
    def isPalindrome(self , x):
        # write code here
        # 处理负数
        if x < 0:
            return False
        # 获取当前x的位数
        cnt = 1
        while x > 10**cnt:
            cnt += 1
        # 从左右两端依次取数字，直到剩余中间一位数字或者空
        while cnt > 1:
            # 获取右端数字
            right = x % 10
            x = (x - right) // 10
            cnt -= 1
            # 获取左端数字
            left = x // 10**(cnt-1)
            x = x - left * 10**(cnt-1)
            cnt -= 1
            # 进行判断
            if left != right:
                return False
        return True
	
    def isPalindrome(self , x):
        # write code here
        if x < 0:
            return False
        curr, y = x, 0
        while curr > 0:
            right = curr % 10
            curr = (curr - right) // 10
            y = y * 10 + right
        return x == y