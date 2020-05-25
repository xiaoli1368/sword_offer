#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 递归实现
    int Add(int a, int b) {
        return b == 0 ? a : Add(a ^ b, (a & b) << 1);
    }

    // 循环实现
    // 注意强制负数向左移位需要类型转换
    int Add2(int a, int b) {
        int tmp = 0;
        while (b != 0) {
            tmp = a ^ b;
            b = (unsigned int)(a & b) << 1;
            a = tmp;
        }
        return a;
    }

    // 测试函数
    void test(int a, int b) {
        int result = 0;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(a, b);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(int, int);
    std::vector<func_ptr> func_vec_ = {&Solution::Add, &Solution::Add2};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(5, 7);
    s.test(-5, 7);

    return 0;
}