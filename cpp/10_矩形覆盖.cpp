#include <iostream>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    int jumpFloot(int n) {
        if (n < 3) {
            return n;
        }

        int a = 1, b = 2, c = 3;
        for (int i = 0; i < n - 2; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    // 测试函数
    void test(int n) {
        int result = 0;
        struct timeval start, end;

        gettimeofday(&start, nullptr);
        result = this->jumpFloot(n);
        gettimeofday(&end, nullptr);
        printf("time(us): %ld, input: %2d, result: %d\n", end.tv_usec - start.tv_usec, n, result);
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    for (int i = 0; i <= 40; i += 10) {
        s.test(i);
    }

    return 0;
}