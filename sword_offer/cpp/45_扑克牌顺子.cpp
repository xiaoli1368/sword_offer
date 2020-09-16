#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 第一次解法
    // 这个版本有问题，不能处理含有重复的情况
    bool IsContinuous1(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }

        int min = 14;
        int max = 0;
        int zero_cnt = 0;

        for (auto i : numbers) {
            if (i < 0 && i > 13) {
                return false;
            } else if (i == 0) {
                zero_cnt++;
                continue;
            }
            
            // 位于[1, 13]
            if (i < min) {
                min = i;
            }
            if (i > max) {
                max = i;
            }
        }

        if (zero_cnt == 4 || (max - min <= 4 && min != max)) {
            return true;
        } else {
            return false;
        }
    }

    // 个人解法
    // 修复版，使用map处理重复情况
    bool IsContinuous2(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }

        int min = 14;
        int max = 0;
        std::map<int, int> map;

        for (auto i : numbers) {
            if (i == 0) {
                continue;
            }
            if (++map[i] == 2) { // 非0重复性判断
                return false;
            }
            if (i < min) { // 更新最小值 
                min = i;
            }
            if (i > max) { // 更新最大值
                max = i;
            }
        }

        // 在无非0重复的情况下
        return max - min <= 4;
    }

    // 参考答案解法
    bool IsContinuous(std::vector<int> numbers) {
        if (numbers.size() != 5) {
            return false;
        }
        sort(numbers.begin(), numbers.end());

        int cnt = 0;
        for (auto i : numbers) {
            if (i == 0) {
                cnt++;
            }
        }

        // 从没有癞子的地方开始，使用癞子去补全顺子
        for (int i = cnt; i < numbers.size() - 1; i++) {
            if (numbers[i] == numbers[i + 1]) {
                return false;
            }
            // 差值为n，则使用n个癞子进行补全
            cnt -= numbers[i + 1] - numbers[i] - 1;
        }

        return cnt >= 0;
    }

    // 测试函数
    void test(std::vector<int>& numbers) {
        bool result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(numbers);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::IsContinuous1,
                                       &Solution::IsContinuous2,
                                       &Solution::IsContinuous};
};

int main(int argc, char* argv[])
{
    std::vector<std::vector<int>> numbers = {{1, 2, 3, 4, 5},
                                             {1, 1, 1, 1, 1},
                                             {1, 3, 0, 5, 0},
                                             {1, 1, 0, 0, 5},
                                             {3, 5, 2, 0, 0},
                                             {0, 0, 0, 0, 9},
                                             {3, 9, 1, 0, 0},
                                             {9, 4, 2, 5, 6}};
    Solution s;
    for (auto nums : numbers) {
        s.test(nums);
    }
    return 0;
}