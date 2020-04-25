//个人解法1：
#include<cmath>
class Solution {
public:
    int cutRope(int n) {
        if (n <= 2) {
            return 1;
        }
        
        if (n == 3) {
            return 2;
        }
        
        long ret = 0;
        int cnt2 = (n % 2 == 0 ? n/2 : n/2-1);
        int cnt3 = (n % 2 == 0 ? 0 : 1);
        
        while (cnt2 >= 3) {
            cnt2 -= 3;
            cnt3 += 2;
        }
        
        ret = pow(2, cnt2) * pow(3, cnt3);
        return ret;
    }
};

//个人高度优化版：
#include<cmath>
class Solution {
public:
    int cutRope(int n) {
        if (n <= 3) return n - 1;
        int cnt3 = (n % 3 == 1 ? n / 3 - 1 : n / 3);
        int cnt2 = (n - cnt3 * 3) / 2;
        return pow(2, cnt2) * pow(3, cnt3);
    }
};