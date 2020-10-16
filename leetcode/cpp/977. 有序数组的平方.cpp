#include <stdio.h>
#include <vector>
#include <algorithm>

class Solution {
public:
    // 暴力法
    std::vector<int> sortedSquares(std::vector<int>& a) {
        std::vector<int> ret;
        for (auto & i : a) {
            ret.push_back(i * i);
        }
        sort(ret.begin(), ret.end());
        return ret;
    }

    // 二分返回负数和非负数的切分点
    int divideIndex(std::vector<int>& a) {
        int l = 0;
        int h = a.size() - 1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (a[m] < 0) {
                l = m + 1;
            } else if (a[m] >= 0) {
                h = m;
            }
        }
        return (a[l] < 0 ? l + 1 : l);
    }

    // 二分 + 归并
    std::vector<int> sortedSquares2(std::vector<int>& a) {
        int m = divideIndex(a);
        int p = m - 1;
        int q = m;
        std::vector<int> ret(a.size(), 0);
        for (int i = 0; i < ret.size(); i++) {
            if (p >= 0 && (q > a.size() - 1 || a[p]*a[p] < a[q]*a[q])) {
                ret[i] = a[p] * a[p];
                p -= 1;
            } else {
                ret[i] = a[q] * a[q];
                q += 1;
            }
        }
        return ret;
    }

    // 直接从两端归并
    std::vector<int> sortedSquares3(std::vector<int>& a) {
        int p = 0;
        int q = a.size() - 1;
        std::vector<int> ret(a.size(), 0);
        for (int i = ret.size() - 1; i >= 0; i--) {
            if (p <= q && a[p]*a[p] >= a[q]*a[q]) {
                ret[i] = a[p] * a[p];
                p += 1;
            } else {
                ret[i] = a[q] * a[q];
                q -= 1;
            }
        }
        return ret;
    }

    // 打印一维数组
    void printf_1d_vec(std::vector<int>& a) {
        for (auto & i : a) {
            printf("%d, ", i);
        }
        printf("\n");
    }

    // 测试函数
    void test(std::vector<std::vector<int>>& lst) {
        for (auto & a : lst) {
            printf("=====\n");
            printf("input data: ");
            printf_1d_vec(a);
            for (auto & func : this->func_vec_) {
                std::vector<int> result = (this->*func)(a);
                printf_1d_vec(result);
            }
        }
    }

private:
    typedef std::vector<int> (Solution::*func_ptr)(std::vector<int>&);
    std::vector<func_ptr> func_vec_ = {&Solution::sortedSquares,
                                       &Solution::sortedSquares2,
                                       &Solution::sortedSquares3};
};

int main(int argc, char* argv[])
{
    std::vector<std::vector<int>> lst = {
        {-4,-1,0,3,10},
        {-7,-3,2,3,11},
        {-7,-3,-2},
        {2,3,11}
    };
    Solution s;
    s.test(lst);
    return 0;
}