#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 两个额外数组，一次遍历，使用stl完成拼接
    void reOrderArray1(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        std::vector<int> tmp1, tmp2;
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp1.push_back(i);
            } else {
                tmp2.push_back(i);
            }
        }
        tmp1.insert(tmp1.end(), tmp2.begin(), tmp2.end());
        array = tmp1;
    }

    // 一个额外数组，两次遍历，首先插入奇数，之后插入偶数
    void reOrderArray2(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        std::vector<int> tmp;
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp.push_back(i);
            }
        }
        for (auto i : array) {
            if (i % 2 == 0) {
                tmp.push_back(i);
            }
        }
        array = tmp;
    }

    // 一个额外数组，两次遍历，首先确定奇偶分界索引，之后分别插入
    void reOrderArray3(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        int odd_index = 0;
        int even_index = 0;
        std::vector<int> tmp(array.size());

        for (auto i : array) {
            if (i % 2 == 1) {
                even_index++;
            }
        }
        for (auto i : array) {
            if (i % 2 == 1) {
                tmp[odd_index++] = i;
            } else {
                tmp[even_index++] = i;
            }
        }
        array = tmp;
    }

    // 二重循环，冒泡方式，将偶数放到最右边
    // 未优化，时间复杂度较大
    void reOrderArray4(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        int len = array.size();
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len - 1; j++) {
                if (array[j] % 2 == 0 && array[j+1] % 2 == 1) {
                    int tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        }
    }

    // 二重循环，冒泡方式，部分优化
    // 依次需要将当前偶数放到最右侧，次右侧...
    void reOrderArray5(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        for (int i = array.size() - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (array[j] % 2 == 0 && array[j+1] % 2 == 1) {
                    int tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        }
    }

    // 辅助函数
    bool static isOdd(int n) {
        return n % 2 == 1;
        // return n & 1 == 1
    }

    // 一种利用stl的取巧方式
    void reOrderArray6(std::vector<int>& array) {
        std::stable_partition(array.begin(), array.end(), Solution::isOdd);
    }

    // 高效方式，类似插入排序，不借助额外数组，两层遍历
    // 外层遍历依次找到各个奇数，内层遍历实现找到该奇数前的几个偶数，交换当前奇数与该偶数段的位置
    void reOrderArray7(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }

        for (int i = 0; i < array.size(); i++) {
            if (array[i] % 2 == 1) {
                // 确定上一个奇数的位置（或者为首元素之前的-1索引）
                // 寻找到相邻两个奇数之间的偶数段
                // 当前分段：[last_odd], [last_odd + 1, i - 1], [i]
                // 交换[i]与[last_odd + 1, i - 1]
                int curr_odd = array[i];
                int last_odd = i - 1;

                while (last_odd >= 0 && array[last_odd] % 2 == 0) {
                    last_odd--;
                }

                for (int j = i - 1; j >= last_odd + 1; j--) {
                    array[j + 1] = array[j];
                }
                array[last_odd + 1] = curr_odd;
            }
        }
    }

    // 双指针法，更加快速，但是破坏了内部的顺序
    void reOrderArray(std::vector<int>& array) {
        if (array.empty()) {
            return;
        }
        int odd = 0, even = array.size() - 1;
        while (odd < even) {
            // 找到指向偶数的odd指针
            while (odd < even && array[odd] % 2 == 1) {
                odd += 1;
            }
            // 找到指向奇数的even指针
            while (odd < even && array[even] % 2 == 0) {
                even -= 1;
            }
            // 如果不越界则交换
            if (odd < even) {
                int tmp = array[odd];
                array[odd] = array[even];
                array[even] = tmp;
            }
        }
        return;
    }
    
    // 输入要打印的vec数据
    void print_vector(std::vector<int>& array) {
        for (auto i : array) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    // 测试函数
    void test(std::vector<int>& array) {
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            // 每个函数都需要申请一个临时变量
            std::vector<int> tmp_array = array;
            gettimeofday(&start, 0);
            (this->*func)(tmp_array);
            gettimeofday(&end, 0);
            printf("time(us): %2ld, result: ", end.tv_usec - start.tv_usec);
            print_vector(tmp_array);
        }
    }

private:
    typedef void (Solution::*func_ptr)(std::vector<int>&);
    std::vector<func_ptr> func_vec_ = {&Solution::reOrderArray1,
                                       &Solution::reOrderArray2,
                                       &Solution::reOrderArray3,
                                       &Solution::reOrderArray4,
                                       &Solution::reOrderArray5,
                                       &Solution::reOrderArray6,
                                       &Solution::reOrderArray7,
                                       &Solution::reOrderArray};
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {1, 3, 8, 2, 4, 5, 9, 7, 6};

    Solution s;
    s.test(array);
    
    return 0;
}