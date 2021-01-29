class Solution {
public:
    bool judgeSquareSum(int c) {
        if (c < 0) {
            return false;
        }
        
        long l = 0, h = pow(c, 0.5) + 1; // 防止溢出
        while (l <= h) {
            long tmp = l * l + h * h; // 防止溢出
            if (tmp == c) {
                return true;
            } else if (tmp < c) {
                l += 1;
            } else {
                h -= 1;
            }
        }
        return false;
    }
};