#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举法
    // 时间复杂度过大
    int NumberOf1Between1AndN_Solution1(int n) {
        if (n <= 0 ) {
            return 0;
        }

        int ret = 0;
        for (int i = 1; i <= n; i++) {
            int j = i;
            while (j != 0) {
                if (j % 10 == 1) {
                    ret++;
                }
                j /= 10;
            }
        }
        return ret;
    }

    // 高效解法：直接版，易于理解
    int NumberOf1Between1AndN_Solution2(int n) {
        if (n <= 0) {
            return 0;
        }

        int ret = 0;
        for (int digit = 1; digit <= n; digit *= 10) {
            // 分解数位
            int curr = (n / digit) % 10;
            int high = n / digit / 10;
            int low = n % digit;

            // 分类讨论
            if (curr == 0) {
                ret += high * digit;
            } else if (curr == 1) {
                ret += high * digit + low + 1;
            } else {
                ret += (high + 1) * digit;
            }
        }

        return ret;
    }

    // 高效解法：优化版，不易于理解
    int NumberOf1Between1AndN_Solution3(int n) {
        int cnt = 0;
        for (int m = 1; m <= n; m *= 10) {
            int a = n / m;
            int b = n % m;
            cnt += (a + 8) / 10 * m + (a % 10 == 1 ? b + 1 : 0);
        }
        return cnt;
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
    std::vector<func_ptr> func_vec_ = {&Solution::NumberOf1Between1AndN_Solution1,
                                       &Solution::NumberOf1Between1AndN_Solution2,
                                       &Solution::NumberOf1Between1AndN_Solution3};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(13);
    s.test(120);
    s.test(41206);
    s.test(5041608);

    return 0;
}