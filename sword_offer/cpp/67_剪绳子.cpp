#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>

class Solution {
public:
    // 递归法，时间复杂度O(n^2)
    // 递推关系为：f(n) = max(i*(n-i), i*f(n-i))
    // 表示长为n的绳子，分出i为一段，剩下的可以继续分或者不分
    // 注意i需要遍历1到n
    int cutRope1(int n) {
        if (n <= 3) {
            return n - 1;
        }

        int ret = 0;
        for (int i = 2; i <= n / 2 + 1; i++) {
            ret = max(ret, max(i * (n - i), i * cutRope3(n - i)));
        }

        return ret;
    }

    // 动态规划
    // 时间复杂度O(n^2)，空间复杂度O(n)
    int cutRope2(int n) {
        int dp[n + 1] = {0, 1, 2};
        for (int i = 3; i <= n; i++) {
            for (int j = 2; j <= i / 2 + 1; j++) {
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
            }
        }

        return dp[n];
    }

    // 个人解法（其实是贪心）
    // 时间复杂度O(1)，空间复杂度O(1)
    int cutRope3(int n) {
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

    // 个人高度优化版（贪心）
    // 时间复杂度O(1)，空间复杂度O(1)
    int cutRope4(int n) {
        if (n <= 3) return n - 1;
        int cnt3 = (n % 3 == 1 ? n / 3 - 1 : n / 3);
        int cnt2 = (n - cnt3 * 3) / 2;
        return pow(2, cnt2) * pow(3, cnt3);
    }

    // ===== 工具函数 =====

    inline int max(int a, int b) {
        return a > b ? a : b;
    }

    // 测试函数
    void test(int n) { 
        int result = 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(n);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(int);
    std::vector<func_ptr> func_vec_ = {&Solution::cutRope1,
                                       &Solution::cutRope2,
                                       &Solution::cutRope3,
                                       &Solution::cutRope4};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(10);
    s.test(50);
    s.test(56);

    return 0;
}