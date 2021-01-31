class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        m是满足 m^2 <= x 的最大整数
        """
        if x <= 0:
            return 0
        
        l, h = 0, x
        while l < h:
            m = (l + h + 1) // 2
            if m**2 > x:
                h = m - 1
            elif m**2 <= x:
                l = m
        return l