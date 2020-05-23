#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>
#include <cmath>

class Solution {
public:
    // 暴力循环法
    // 无法处理exponent为最小负数的情况
    // 没有进行特殊情况判断，如0^0
    double Power1(double base, int exponent) {
        if (exponent == 0) {
            return 1.0;
        }

        bool sign = false;
        if (exponent < 0) {
            sign = true;
            exponent = -exponent;
        }

        double result = 1.0;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }

        if (sign) {
            result = 1 / result;
        }

        return result;
    }

    // 暴力循环法，优化版
    // 考虑exponent为最小负数，但这种情况时间复杂度过大
    double Power2(double base, int exponent) {
        // 处理特殊情况
        if (ifEquel(base, 0)) {
            return 0;
        }
        if (ifEquel(base, 1) || exponent == 0) {
            return 1;
        }

        // 处理符号位
        int sign = 1;
        long e = exponent;
        if (e < 0) {
            sign = -1;
            e = -e;
        }

        // 获取结果
        double ret = 1.0;
        for (int i = 0; i < e; i++) {
            ret *= base;
        }

        return sign == 1 ? ret : 1 / ret;
    }

    // 快速幂方法
    // 时间复杂度为o(logn)，不用考虑符号问题
    double Power3(double base, int exponent) {
        if (base == 0) {
            return 0;
        }

        int e = exponent;
        double ret = 1.0;
        while (e != 0) {
            if (e & 1 == 1) { // 奇数无法二分，需要向结果中凑一个base
                ret *= base;
            }
            base *= base;     // base增长为2倍
            //e >>= 1;        // 指数二分，这种方式要保证符合位，因此结果可能永远为负
            e /= 2;           // 这种方式不用考虑符号
        }

        return exponent < 0 ? 1 / ret : ret;
    }

    // 库函数法
    double Power4(double base, int exponent) {
        return pow(base, exponent);
    }

    // 工具函数，判断两个double是否相等
    bool ifEquel(double a, double b) {
        return -1e-6 < a - b && a - b < 1e-6;
    }

    // 测试函数
    void test(double base, int exponent) {
        double result = 0.0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(base, exponent);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %e\n", end.tv_usec - start.tv_usec, result);
        }
    }

private:
    typedef double (Solution::*func_ptr)(double, int);
    std::vector<func_ptr> func_vec_ = {&Solution::Power1,
                                       &Solution::Power2,
                                       &Solution::Power3,
                                       &Solution::Power4};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(0, 0);
    s.test(0, 2);
    s.test(2, 0);
    s.test(1, 10086);
    s.test(2, 3);
    s.test(2, -3);
    s.test(3, 500);
    s.test(4, 5000);
    s.test(5, 6000000);
    //s.test(2, 0x80000000); // 运算时间过长
    
    return 0;
}