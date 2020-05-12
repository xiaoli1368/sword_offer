#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 常规思路：暴力枚举
    std::vector<int> FindNumbersWithSum1(std::vector<int> array, int sum) {
        std::vector<int> result;
        for (int i = 0; i < array.size() - 1; i++) {
            for (int j = i + 1; j < array.size(); j++) {
                if (array[i] + array[j] == sum) {
                    result.push_back(array[i]);
                    result.push_back(array[j]);
                }
            }
        }

        return result;
    }

    // 其它思路：map
    std::vector<int> FindNumbersWithSum2(std::vector<int> array, int sum) {
        std::vector<int> result;
        std::map<int, int> map;

        for (auto i : array) {
            map[i]++; // 默认初始化为0
        }

        for (auto i : array) {
            if (map[sum - i]) {
                result.push_back(i);
                result.push_back(sum - i);
                break;
            }
        }

        return result;
    }

    // 高效思路：双指针
    std::vector<int> FindNumbersWithSum(std::vector<int> array, int sum) {
        int l = 0;
        int h = array.size() - 1;
        std::vector<int> result;

        while (l < h) {
            int currSum = array[l] + array[h];
            if (currSum == sum) {
                result.push_back(array[l]);
                result.push_back(array[h]);
                break;
            } else if (currSum < sum) {
                l++;
            } else if (currSum > sum) {
                h--;
            }
        }

        return result;
    }

    // 测试函数
    void test(std::vector<int>& array, int sum) {
        std::vector<int> result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(array, sum);
            gettimeofday(&end, nullptr);
            printf("result: [%d, %d], time(us): %ld\n", result[0], result[1], end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(std::vector<int>, int);
    std::vector<func_ptr> func_vec_ = {&Solution::FindNumbersWithSum1,
                                       &Solution::FindNumbersWithSum2,
                                       &Solution::FindNumbersWithSum};
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {1, 2, 3, 4, 5, 6, 7}; 
    std::vector<int> array2 = {1, 1, 2, 2, 3, 5, 6, 9, 10, 12, 14, 15, 19, 20};

    Solution s;
    s.test(array, 6);
    s.test(array2, 19);

    return 0;
}