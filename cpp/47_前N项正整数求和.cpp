#include <iostream>
#include <cmath>

class Solution {
public:
    // 递归解法
    int Sum_Solution(int n) {
        int sum = n;
        bool tmp = n > 0 && (sum += Sum_Solution(n - 1)) > 0;
        return sum;
    }

    // 其它解法
    int Sum_Solution2(int n) {
        char tmp[n][n+1];
        return sizeof(tmp) >> 1;
    }

    int Sum_Solution3(int n) {
        return (int(pow(n, 2)) + n) >> 1;
    }

    // 自定义乘法
    int multiply(int a, int b) {
        int res = 0;
        (a&1) && (res += b);
        a >>= 1; b <<=1;
        a && (res += multiply(a, b));
        return res;
    }

    int Sum_Solution4(int n) {
        return multiply(n, n + 1) >> 1;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.Sum_Solution(10) << std::endl;
    std::cout << s.Sum_Solution2(10) << std::endl;
    std::cout << s.Sum_Solution4(10) << std::endl;

    return 0;
}