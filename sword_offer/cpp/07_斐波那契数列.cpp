#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 递归的方式
    int Fibonacci(int n) {
        if (n < 2) {
            return n;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);
    }

    // 动态规划：数组存储
    int Fibonacci2(int n) {
        if (n < 2) {
            return n;
        }
        std::vector<int> vec = {0, 1};
        for (int i = 0; i < n-1; i++) {
            vec.push_back(vec.back() + vec.at(vec.size() - 2));
        }
        return vec.back();
    }

    // 动态规划：临时变量
    int Fibonacci3(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 0;
        for (int i = 0; i < n-1; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    // 动态规划：处理溢出的大数，考虑求余
    // 求余规则：(a + b) % c = (a % c + b % c) % c
    // c可以自行规定，如1000000007
    int Fibonacci4(int n) {
        if (n < 2) {
            return n;
        }
        int a = 0, b = 1, c = 0;
        for (int i = 0; i < n-1; i++) {
            c = (a + b) % 1000000007;
            a = b;
            b = c;
        }
        return c;
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
    std::vector<func_ptr> func_vec_ = {&Solution::Fibonacci,
                                       &Solution::Fibonacci2,
                                       &Solution::Fibonacci3,
                                       &Solution::Fibonacci4};

};

int main(int argc, char* argv[])
{
    Solution s;
    for (int i = 0; i <= 40; i += 10) {
        s.test(i);
    }

    return 0;
}