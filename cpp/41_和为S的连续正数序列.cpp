#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 常规解法
    // 利用等差序列性质，这种方法更加高效
    // midTwice * num = sum * 2
    std::vector<std::vector<int>> FindContinuousSequence1(int sum) {
        std::vector<std::vector<int>> result;
        if (sum < 3) {
            return result;
        }

        int l = 0;
        int h = 0;
        int midTwice = 0;      // 目标序列中间值的二倍
        int num = sum / 2 + 1; // 目标序列的数量（长度）

        while (num >= 2) {
            if ((sum * 2) % num == 0) { // 存在约数
                midTwice = (sum * 2) / num;
                if (num % 2 == 1 && midTwice % 2 == 0) {
                    l = midTwice / 2 - num / 2;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                } else if (num % 2 == 0 && midTwice % 2 == 1) {
                    l = midTwice / 2 - num / 2 + 1;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                }
            }
            num--;
        }
        return result;
    }

    // 常规解法（优化版）
    // midTwice * num = sum * 2
    std::vector<std::vector<int>> FindContinuousSequence2(int sum) {
        int l = 0;
        int h = 0;
        int midTwice = 0;      // 目标序列中间值的二倍
        int num = sum / 2 + 1; // 目标序列的数量（长度）
        std::vector<std::vector<int>> result;

        while (num >= 2) {
            if ((sum * 2) % num == 0) { // 存在约数
                midTwice = (sum * 2) / num;
                if ((num + midTwice) % 2 == 1) { // 确保一奇一偶
                    l = midTwice / 2 - num / 2 + midTwice % 2;
                    h = midTwice / 2 + num / 2;
                    add_vec(result, l, h);
                }
            }
            num--;
        }
        return result;
    }

    // 双指针解法
    // 效率一般
    std::vector<std::vector<int>> FindContinuousSequence(int sum) {
        if (sum < 3) {
            return std::vector<std::vector<int>>{};
        }

        int l = 1;
        int h = 2;
        int currSum = 3;
        std::vector<std::vector<int>> result;
 

        while (h <= sum / 2 + 1) {
            currSum = (l + h) * (h - l + 1) / 2;
            if (currSum > sum) {
                l++;
            } else if (currSum < sum) {
                h++;
            } else { // 此时相等
                add_vec(result, l, h);
                l++;
            }
        }
        
        return result;
    }

    // 用于添加的函数
    void add_vec(std::vector<std::vector<int>>& vec, int& l, int& h) {
        // 注意要去除l为负数的情况
        if (l <= 0) {
            return;
        }

        std::vector<int> tmp;
        for (int i = l; i <= h; i++) {
            tmp.push_back(i);
        }
        vec.push_back(tmp);
    }

    // 打印二维数组
    void print_2d_vec(std::vector<std::vector<int>>& vec) {
        for (auto i : vec) {
            for (auto j : i) {
                std::cout << j << " ";
            }
            std::cout << ", ";
        }
        std::cout << std::endl;
    }

    // 测试函数
    void test(int sum) {
        std::vector<std::vector<int>> result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(sum);
            gettimeofday(&end, nullptr);
            printf("time(us): %2ld, result: ", end.tv_usec - start.tv_usec);
            this->print_2d_vec(result);
        }
    }

private:
    typedef std::vector<std::vector<int>> (Solution::*func_ptr)(int);
    std::vector<func_ptr> func_vec_ = {&Solution::FindContinuousSequence1,
                                       &Solution::FindContinuousSequence2,
                                       &Solution::FindContinuousSequence};
};

int main(int argc, char* argv[])
{
    Solution s;
    //s.test(0);
    s.test(15);
    //s.test(77);
    //s.test(100);

    return 0;

}