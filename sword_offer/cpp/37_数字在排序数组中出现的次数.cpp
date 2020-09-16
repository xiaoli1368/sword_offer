#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举
    int GetNUmberOfK1(std::vector<int> data, int k) {
        if (data.empty()) {
            return 0;
        }

        int count = 0;
        for (auto i : data) {
            if (i == k) {
                count++;
            }
        }

        return count;
    }

    // 普通二分查找
    // 寻找特定值，然后左右遍历
    // 第一次的方式，存在封装优化空间
    int GetNumberOfK2(std::vector<int> data, int k) {
        if (data.empty()) {
            return 0;
        }
        
        // 二分查找是否存在，返回任意一个等于k的索引
        int l = 0;
        int h = data.size() - 1;
        int index = -1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (data[m] > k) {
                h = m - 1;
            } else if (data[m] < k) {
                l = m + 1;
            } else if (data[m] == k) {
                index = m;
                break;
            }
        }
        
        // 如果不存在k
        if (index == -1) {
            return 0;
        }
        
        // 如果存在，则从该位置向两端检测出现的次数
        l = index;
        h = index;
        while (data[l] == k || data[h] == k) {
            if (data[l] == k) {
                l--;
            }
            if (data[h] == k) {
                h++;
            }
        }
        
        return h - l - 1;
    }

    // 一次二分查找，优化版，将二分查找部分进行了封装
    int GetNumberOfK3(std::vector<int> data, int k) {
        if (data.empty()) {
            return 0;
        }

        int index = binarySearch_one(data, k);
        if (index == -1) {
            // 此时数组内不存在等于k的值
            return 0;
        }

        int first = index;
        int last = index;
        while (data[first] == k) {
            first--;
        }
        while (data[last] == k) {
            last++;
        }

        return last - first - 1;
    }

    // 高效思路，查找[k, k+1]，其中一种查找方式
    int GetNumberOfK4(std::vector<int> data, int k) {
        return binarySearch2(data, k + 1) - binarySearch2(data, k); 
    }

    // 高效思路，查找[k, k+1]
    int GetNumberOfK(std::vector<int> data, int k) {
        int first = binarySearch(data, k);
        int last = binarySearch(data, k + 1);
        return last - first;
    }

    // 需要调用的函数: 二分查找，左边界
    // 返回数组中第一个大于等于k的索引，注意大于整体数组时返回data.size()
    int binarySearch(std::vector<int> data, int k) {
        int l = 0;
        int h = data.size();
        while (l < h) {
            int m = l + (h - l) / 2;
            if (data[m] >= k) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    // 另外一种二分查找的形式，左边界
    // 注意大于整体数组时返回data.size()
    int binarySearch2(std::vector<int> data, int k) {
        int l = 0;
        int h = data.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (data[m] < k) {
                l = m + 1;
            } else {
                h = m;
            }
        }

        return (l == data.size() - 1 && data[l] != k ? l + 1 : l);
    }

    // 二分查找某一值的索引，不存在返回-1
    int binarySearch_one(std::vector<int> data, int k) {
        int l = 0;
        int h = data.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (data[m] == k) {
                return m;
            } else if (data[m] < k) {
                l = m + 1;
            } else {
                h = m - 1;
            }
        }

        if (data[l] != k) {
            return -1;
        }

        return l;
    }


    // 测试函数
    void test(std::vector<int>& nums, int k) {
        int result = 0;
        struct timeval start, end;
        for (auto func : this->func_vec_) {
            gettimeofday(&start, 0);
            result = (this->*func)(nums, k);
            gettimeofday(&end, 0);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(std::vector<int>, int);
    std::vector<func_ptr> func_vec_ = {&Solution::GetNUmberOfK1,
                                       &Solution::GetNumberOfK2,
                                       &Solution::GetNumberOfK3,
                                       &Solution::GetNumberOfK4,
                                       &Solution::GetNumberOfK};
};

// 获取range(first, last)形式的数组
void get_range_vec(std::vector<int>& vec, int first, int last) {
    while (first < last) {
        vec.push_back(first);
        first++;
    }
}

int main(int argc, char* argv[])
{
    std::vector<int> vec = {1, 2, 3, 3, 3, 3, 4, 5, 6, 7};
    std::vector<int> vec2;
    get_range_vec(vec2, 0, 1000);

    Solution s;
    s.test(vec, 3);
    std::cout << "=====" << std::endl;
    s.test(vec2, 36);

    return 0;
}