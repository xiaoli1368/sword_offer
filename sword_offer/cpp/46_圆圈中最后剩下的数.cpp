#include <iostream>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力枚举，初始版
    int LastRemaining_Solution1(int n, int m) {
        if (n <= 0 || m <= 0) {
            return -1;
        }

        int sign[n] = {0};
        int count = n;
        int index = -1;
        int step = 0;

        while (count > 0) { // 全部删除，则最后一个就是待求
            index++;
            if (index >= n) { // 确保环形遍历
                index = 0;
            }
            if (sign[index] == 1) { // 跳过删除的元素
                continue;
            }
            step++;
            if (step == m) { // 确定找到了下一个元素
                sign[index] = 1;
                count--;
                step = 0;
            }
        }

        return index;
    }

    // 暴力枚举，优化版
    // 代码简洁了，但是好像时间复杂度更大了
    int LastRemaining_Solution2(int n, int m) {
        if (n <= 0 || m <= 0) {
            return -1;
        }

        int ret = 0;            // 结果索引
        int cnt = n;            // 当前剩余元素个数
        int step = 0;           // 报数计数变量
        bool sign[n] = {false}; // 是否被选中的标志

        for (int i = 0; cnt > 0; i = (i + 1) % n) {
            if (sign[i]) { // 跳过已经被选中的元素
                continue;
            }

            step++; // 报数+1
            if (step == m) { // 确定找到了下一个元素
                cnt--;
                ret = i;
                step = 0;
                sign[i] = true;
            }
        }

        return ret;
    }
    
    // 递归法
    // s(n)表示还剩下n个元素没有选中时的解
    // 递推公式： s(n) = (s(n-1) + m) % n 
    // 初始情况： s(2) = (s(1) + m) % 2
    int LastRemaining_Solution3(int n, int m) {
        if (n == 0) {
            return -1;
        }
        if (n == 1) {
            return 0;
        }

        return (LastRemaining_Solution3(n - 1, m) + m) % n;
    }

    // 动态规划，反向迭代，反向的递推公式
    int LastRemaining_Solution4(int n, int m) {
        if (n == 0) {
            return -1;
        }

        int s = 0;
        for (int i = 2; i <= n; i++) {
            s = (s + m) % i;
        }
        return s;
    }

    // 单向循环链表，需补充
    int LastRemaining_Solution5(int n, int m) {
        return 0;
    }

    // 测试函数
    void test(int n, int m) {
        int result = 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto & func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(n, m);
            gettimeofday(&end, nullptr);
            printf("result: %d, time(us): %ld\n", result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(int, int);
    std::vector<func_ptr> func_vec_ = {&Solution::LastRemaining_Solution1,
                                       &Solution::LastRemaining_Solution2,
                                       &Solution::LastRemaining_Solution3,
                                       &Solution::LastRemaining_Solution4};
};

int main(int argc, char* argv[])
{
    Solution s;
    s.test(5, 3);
    s.test(10, 17);
    s.test(500, 300);
    s.test(2000, 4000);

    return 0;
}