"""
关键在于对空字符串的处理
当检测到空字符串的时候，无法进行区间的缩小
此时，需要使用线性检索来确认一个区间，这里检测的是右区间
其它方面需要注意边界条件
"""

class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        l = 0
        h = len(words) - 1

        while l <= h:
            m = l + (h - l) // 2

            # 如果为空，则向右线性查找一个非空值
            while m < h and words[m] == "":
                m += 1
            if m == h and words[m] != s:
                h = m - 1
                continue
        
            if words[m] == s:
                return m
            elif words[m] > s:
                h = m - 1
            elif words[m] < s and words[m] != "":
                l = m + 1
        
        return -1