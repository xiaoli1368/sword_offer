#!/bin/bash python
"""
925. 长按键入

思路：双指针法
"""

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        双指针
        """
        p = q = 0
        while p < len(name) and q < len(typed):
            if name[p] == typed[q]:
                q += 1
                p = min(p + 1, len(name) - 1)
            elif p - 1 >= 0 and name[p - 1] == typed[q]:
                q += 1
            else:
                return False
        return p == len(name) - 1 and q == len(typed) and name[p] == typed[q - 1]

if __name__ == "__main__":
    name = "pyplrz"
    typed = "ppyypllr"
    s = Solution()
    print(s.isLongPressedName(name, typed))