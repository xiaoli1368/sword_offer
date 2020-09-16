#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>

class Solution {
public:
    // 递归解法
    // 利用&&短路特性，代替if条件判断
    int Sum_Solution1(int n) {
        int sum = n;
        bool tmp = n > 0 && (sum += Sum_Solution1(n - 1)) > 0;
        return sum;
    }

    // 无脑sizeof法
    int Sum_Solution2(int n) {
        char tmp[n][n+1];
        return sizeof(tmp) >> 1;
    }

    // 库函数法
    int Sum_Solution3(int n) {
        return (int(pow(n, 2)) + n) >> 1;
    }

    // 快速乘法
    int Sum_Solution4(int n) {
        return multiply(n, n + 1) >> 1;
    }

    // 自定义乘法
    int multiply(int a, int b) {
        int res = 0;
        (a&1) && (res += b);
        a >>= 1; b <<=1;
        a && (res += multiply(a, b));
        return res;
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
    std::vector<func_ptr> func_vec_ = {&Solution::Sum_Solution1,
                                       &Solution::Sum_Solution2,
                                       &Solution::Sum_Solution3,
                                       &Solution::Sum_Solution4};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(10);

    return 0;
}