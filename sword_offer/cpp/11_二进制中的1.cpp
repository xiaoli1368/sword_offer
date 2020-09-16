#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 循环移位法,注意需要转换类型
    // 时间复杂度为O(32)
    int NumberOf1(int n) {
        unsigned int tmp = n;
        int result = 0;
        while (tmp > 0) {
            if (tmp & 1 == 1) {
                result++;
            }
            tmp >>= 1;
        }
        return result;
    }

    // 依次找最后一位1,不需要转换类型
    // 时间复杂度:O(1的个数)
    int NumberOf1_easy(int n) {
        // 这种方式不需要转换符号
        int cnt = 0;
        while (n != 0) {
            cnt++;
            n &= (n - 1);
        }
        return cnt;
    }

    // 测试函数
    void test(int n) {
        int result= 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(n);
            gettimeofday(&end, nullptr);
            printf("result: %2d, times(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(int);
    std::vector<func_ptr> func_vec_ = {&Solution::NumberOf1, &Solution::NumberOf1_easy};
};

int main(int argc, char* [])
{
    Solution s;
    s.test(8);
    s.test(-7);
    s.test(-1);

    return 0;
}