#include <vector>
using namespace std;

class Solution {
public:
    // 交换函数
    void swap(vector<int>& ret, int a, int b) {
        int tmp = ret[a];
        ret[a] = ret[b];
        ret[b] = tmp;
    }

    // 二重循环方法
    vector<int> sortArrayByParityII(vector<int>& a) {
        if (a.empty() || a.size() % 2 != 0) {
            return;
        }
        for (int i = 0; i < a.size(); i++) {
            if (i % 2 == a[i] % 2) { // 满足奇偶性质
                continue;
            }
            for (int j = i + 1; j < a.size(); j++) { // 找到下一个同i性质的
                if (i % 2 == a[j] % 2) { // 交换
                    swap(a, i, j);
                }
            }
        }
        return a;
    }
 
    // 新数组
    vector<int> sortArrayByParityII(vector<int>& a) {
        if (a.empty() || a.size() % 2 != 0) {
            return a;
        }

        int even = 0; // 偶数指针
        int odd = 1;  // 奇数指针
        std::vector<int> ret(a.size(), 0);
        for (auto & i : a) {
            int& index = (i % 2 == 0 ? even : odd);
            ret[index] = i;
            index += 2;
        }

        return ret;
    }

    // 双指针，同时从左向右遍历
    vector<int> sortArrayByParityII(vector<int>& a) {
        if (a.empty() || a.size() % 2 != 0) {
            return a;
        }
        int n = a.size();
        int even = 0, odd = 1;
        while (even < n && odd < n) {
            // 找到指向奇数的even指针
            while (even < n && a[even] % 2 == 0) {
                even += 2;
            }
            // 找到指向偶数的odd指针
            while (odd < n && a[odd] % 2 == 1) {
                odd += 2;
            }
            // 如果没有越界则交换
            if (even < n && odd < n) {
                swap(a, even, odd);
            }
        }
        return a;
    }
};