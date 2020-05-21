#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 参考答案
    // 没有考虑溢出
    int StrToInt1(std::string str) {
        if (str.empty()) {
            return 0;
        }

        int ret = 0;
        bool isNegative = str[0] == '-';

        for (int i = 0; i < str.size(); i++) {
            char c = str[i];
            if (i == 0 && (c == '+' || c == '-')) {
                continue;
            }
            if (c < '0' || c > '9') {
                return 0;
            }
            ret = ret * 10 + (c - '0');
        }
        
        return isNegative ? -ret : ret;
    }

    // 个人答案，防止溢出
    int StrToInt2(std::string str) {
        if (str.empty()) {
            return 0;
        }
        
        int sign = 1;
        long sum = 0;
        for (int i = 0; i < str.size(); i++) {
            if (i == 0 && str[i] == '-') {
                sign = -1;
                continue;
            }
            if (i == 0 && str[i] == '+') {
                continue;
            }
            if (str[i] < '0' || str[i] > '9') {
                return 0;
            }
            sum = sum * 10 + int(str[i] - '0');
        }
        sum *= sign;

        // 考虑int溢出
        if (sum >= pow(2, 31) || sum < -pow(2, 31)) {
            return 0;
        } else {
            return sum;
        }
    }

    // 个人答案，优化版，不使用pow函数
    int StrToInt3(std::string str) {
        if (str.empty()) {
            return 0;
        }
        
        int sign = 1;
        long sum = 0;
        int maxInt = 0x7fffffff;
        int minInx = 0x80000000;

        for (int i = 0; i < str.size(); i++) {
            if (i == 0 && str[i] == '-') {
                sign = -1;
                continue;
            }
            if (i == 0 && str[i] == '+') {
                continue;
            }
            if (str[i] < '0' || str[i] > '9') {
                return 0;
            }
            sum = sum * 10 + int(str[i] - '0');
        }
        sum *= sign;

        // 考虑int溢出
        if (sum > maxInt || sum < minInx) {
            return 0;
        } else {
            return sum;
        }
    }

    // 测试函数
    void test(std::string& str) {
        int result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(str);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %d\n", end.tv_usec - start.tv_usec, result);
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::string);
    std::vector<func_ptr> func_vec_ = {&Solution::StrToInt1,
                                       &Solution::StrToInt2,
                                       &Solution::StrToInt3};
};

int main(int argc, char* argv[])
{
    std::vector<std::string> strs = {"-123",
                                     "+456",
                                     "54354",
                                     "-2147483649",
                                     "-2147483648",
                                     "+2147483647",
                                     "+2147483648"};
    Solution s;
    for (auto str : strs) {
        s.test(str);
    }

    return 0;
}