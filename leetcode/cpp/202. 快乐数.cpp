class Solution {
public:
    // 获取各个数位元素的平方和
    int getSum(int n) {
        int sum = 0;
        while (n) {
            int tmp = n % 10;
            sum += tmp * tmp;
            n /= 10;
        }
        return sum;
    }

    // 双指针法
    bool isHappy(int n) {
        int p = n;
        int q = n;
        while (1) {
            p = getSum(p);
            q = getSum(getSum(q));
            if (p == 1 or q == 1) {
                return true;
            } else if (p == q) {
                return false;
            }
        }
    }
};