#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 常规思路：使用map，时间复杂度O(2n)，空间复杂度O(n)
    void FindNumsAppearOnce1(std::vector<int> data, int* num1, int* num2) {
        if (data.empty()) {
            return;
        }

        std::map<int, int> map;
        for (auto i : data) {
            if (map.count(i) == 0) {
                map[i] = 1;
            } else {
                map[i]++;
            }
        }

        std::vector<int> tmp;
        for (auto i : data) {
            if (map[i] == 1) {
                tmp.push_back(i);
            }
        }

        *num1 = tmp[0];
        *num2 = tmp[1];
    }

    // 高效方式：使用异或，时间复杂度O(2n)，空间复杂度O(1)
    void FindNumsAppearOnce(std::vector<int> data, int* num1, int* num2) {
        if (data.empty()) {
            return;
        }

        int diff = 0;
        for (auto i : data) {
            diff ^= i;
        }
        diff &= -diff;

        *num1 = 0;
        *num2 = 0;
        for (auto i : data) {
            if ((i & diff) == 0) { // 注意运算符优先级
                *num1 ^= i;
            } else {
                *num2 ^= i;
            }
        }
    }

    // 测试函数
    void test(std::vector<int>& data) {
        int num1, num2;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            (this->*func)(data, &num1, &num2);
            gettimeofday(&end, nullptr);
            printf("result: [%d, %d], time(us): %ld\n", num1, num2, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef void (Solution::*func_ptr)(std::vector<int>, int*, int*);
    std::vector<func_ptr> func_vec_ = {&Solution::FindNumsAppearOnce1,
                                       &Solution::FindNumsAppearOnce};
};

int main(int argc, char* argv[])
{
    std::vector<int> data = {2, 4, 3, 6, 3, 2, 5, 5};
    std::vector<int> data2 = {1, 2};

    Solution s;
    s.test(data);
    s.test(data2);

    return 0;
}