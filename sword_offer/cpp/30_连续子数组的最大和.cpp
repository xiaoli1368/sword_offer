#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举，双层循环，借助stl排序
    int FindGreatestSumOfSubArray1(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        std::vector<int> ret;
        for (int i = 0; i < array.size(); i++) {
            int tmp = array[i];
            ret.push_back(tmp);
            for (int j = i + 1; j < array.size(); j++) {
                tmp += array[j];
                ret.push_back(tmp);
            }
        }
        sort(ret.begin(), ret.end());

        return ret.back();
    }

  
    // 暴力枚举，双层循环
    int  FindGreatestSumOfSubArray2(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int max = array[0];
        for (int i = 0; i < array.size(); i++) {
            int sum = array[i];
            for (int j = i + 1; j < array.size(); j++) {
                sum += array[j];
                if (max < sum) {
                    max = sum;
                }
            }
        }

        return max;
    }

    // 第一次解法，动态规划
    int FindGreatestSumOfSubArray3(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }
        
        int length = array.size();
        if (length == 1) {
            return array[0];
        }

        int curr_sum = array[0];
        int curr_max = array[0];
        for (int i = 1; i < length; i++) {
            if (curr_sum >= 0) {
                curr_sum += array[i];
            } else {
                curr_sum = array[i];
            }

            if (curr_sum > curr_max) {
                curr_max = curr_sum;
            }
        }

        return curr_max;
    }

    // 动态规划，高效版
    int FindGreatestSumOfSubArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int curr_sum = -1;
        int curr_max = array[0];
        for (auto i : array) {
            curr_sum = i + (curr_sum > 0 ? curr_sum : 0);
            if (curr_max < curr_sum) {
                curr_max = curr_sum;
            }
        }

        return curr_max;
    }

    // 测试函数
    void test(std::vector<int>& array) {
        int result = 0;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(array);
            gettimeofday(&end, 0);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::FindGreatestSumOfSubArray1,
                                       &Solution::FindGreatestSumOfSubArray2,
                                       &Solution::FindGreatestSumOfSubArray3,
                                       &Solution::FindGreatestSumOfSubArray};
 
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {6, -3, -2, 7, -15, 1, 2, 2};

    Solution s;
    s.test(array);
    return 0;
}