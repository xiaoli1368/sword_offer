#include <iostream>
#include <vector>

class Solution {
public:
    // 暴力枚举
    // 寻找数组中由大变小的值，若不存在则说明所有数据相同，输出首元素即可
    int minNumberInRotateArray1(std::vector<int> array) {
        if (array.empty()) {
            return -1;
        }

        int length = array.size();
        for (int i = 0; i < length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return array[i + 1];
            }
        }
        return array[0];
    }

    // 二分查找，[l, m]区间待优化版
    int minNumberInRotateArray2(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int l = 0;
        int h = array.size() - 1;
        while (l < h) {
            int m = h - (h - l) / 2;
            if (array[l] == array[m] && array[m] == array[h]) {
                return minNumber(array, l, h);
            } else if (array[l] <= array[m]) {
                l = m;
            } else {
                // 需要特殊处理
                if (l + 1 == m) {
                    l++;
                }
                h = m; // 这里不使用m-1
            }
        }
        return array[l];

    }

    // 二分查找，高效思路，最终版
    // 以下使用 l m h 分别代替 low middle high
    // 优先使用[m, h]区间判断
    int minNumberInRotateArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int l = 0;
        int h = array.size() - 1;
        while (l <= h) {
            int m = (l + h) / 2;
            if (array[l] == array[m] && array[m] == array[h]) {
                return minNumber(array, l, h);
            } else if (array[m] <= array[h]) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return array[l];
    }

    // 查找最小值，用于处理特殊情况
    int minNumber(std::vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = low; i <= high; i++) {
            if (tmp > array[i]) {
                tmp = array[i];
            }
        }
        return tmp;
    }

    // ===== 以下用来测试二分查找的区间划分 =====

    // 借助二分查找来查找最大值的索引，返回最大值右侧的值即为最小值
    int minNumberInRotateArray3(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int length = array.size();
        int maxIndex = maxIndexInRotateArray(array);

        // 修正最大值为与最小值相邻的那个（有可能是末尾元素）
        while (maxIndex < length - 1 && array[maxIndex] == array[maxIndex + 1]) {
            maxIndex++;
        }

        // 其它情况，需要检测最大值后方是否存在一个最小值
        return array[(maxIndex + 1) % length];
    }

    // 二分查找，查找旋转数组的最大值（用来测试二分查找算法）
    // 优先使用[l, m]区间判断（这个区间划分适合找最大值）
    // 详细思路：
    //    [1] 使用array[l]与array[m]来判断，待求目标即最大值位于前半段
    //    [2] 更新区间的方式为：l = m, h = m - 1（l不能等于m+1，因为有可能丢失结果）
    //    [3] 考虑到 l = m，则m的计算方式不能偏左，否则会无限循环（所以 m = h - (h - l) / 2）
    //    [4] 循环条件，如果是包括等号，则要考虑l=m=h的情况下，再迭代一次的结果
    int maxNumberInRotateArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int l = 0;
        int h = array.size() - 1;
        while (l <= h) {
            int m = h - (h - l) / 2;
            if (array[l] == array[m] && array[m] == array[h]) {
                return maxNumber(array, l, h);
            } else if (array[l] <= array[m]) {
                l = m;
            } else {
                h = m - 1;
            }
        }
        return array[l];
    }

    // 二分查找，查找旋转数组的最大值（返回下标索引）
    // 优先使用[l, m]区间判断（这个区间划分）
    int maxIndexInRotateArray(std::vector<int> array) {
        if (array.empty()) {
            return 0;
        }

        int l = 0;
        int h = array.size() - 1;
        while (l <= h) {
            int m = h - (h - l) / 2;
            if (array[l] == array[m] && array[m] == array[h]) {
                return maxIndex(array, l, h);
            } else if (array[l] <= array[m]) {
                l = m;
            } else {
                h = m - 1;
            }
        }
        return l;
    }

    // 查找最大值，用于处理特殊情况
    int maxNumber(std::vector<int> array, int low, int high) {
        int tmp = array[low];
        for (int i = low; i <= high; i++) {
            if (tmp < array[i]) {
                tmp = array[i];
            }
        }
        return tmp;
    }

    // 查找最大值索引，用于处理特殊情况
    int maxIndex(std::vector<int> array, int low, int high) {
        int tmp = low;
        for (int i = low; i <= high; i++) {
            if (array[tmp] < array[i]) {
                tmp = i;
            }
        }
        return tmp;
    }

    // 测试函数
    void test(std::vector<int>& array) {
        int i = 1;
        for (auto func : this->func_vec_) {
            std::cout << "Function : " << i++
                      << " , result: " << (this->*func)(array)
                      << std::endl;
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::vector<int>);
    std::vector<func_ptr> func_vec_ = {&Solution::minNumberInRotateArray1,
                                       &Solution::minNumberInRotateArray2,
                                       &Solution::minNumberInRotateArray3,
                                       &Solution::minNumberInRotateArray,
                                       &Solution::maxNumberInRotateArray};
};

int main(int argc, char* argv[])
{
    std::vector<int> array = {3, 4, 5, 1, 2};
    //std::vector<int> array2 = {1, 3, 5};
    std::vector<int> array2 = {1, 1, 1, 0, 1};

    Solution s;
    s.test(array);
    std::cout << "==========" << std::endl;
    s.test(array2);

    return 0;
}