#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 暴力解法，复杂度过大
    int GetUglyNumber_Solution1(int index) {
        int cnt = 0;
        int result = 0;

        while (cnt < index) {
            int num = ++result;

            while (num % 5 == 0) num /= 5;
            while (num % 3 == 0) num /= 3;
            while (num % 2 == 0) num /= 2;

            if (num == 1) cnt++;
        }

        return result;
    }

    // 堆（优先级队列）模拟法
    // 时间复杂度在数据量较大时显示优越性
    // 算法流程：
    //     1. 起始 result = 1
    //     2. 后续每次使用result * (2, 3, 5)获取待选元素
    //     3. 经过 set 去除重复后，push进入小顶堆
    //     4. 最小元素即为下一次的 result
    int GetUglyNumber_Solution2(int index) {
        if (index <= 0) {
            return 1;
        }

        int result = 1;
        std::set<int> s; // 使用set保证添加时无重复
        std::vector<int> mask = {2,3,5}; // 定义质数因子的数组
        std::priority_queue <int, std::vector<int>, std::greater<int>> q; // 定义升序队列（看作小顶堆）

        for (int i = 1; i < index; i++) {
            for (auto & m : mask) {
                int tmp = result * m;
                if (s.find(tmp) == s.end()) { // 如果在s中未出现
                    s.insert(tmp);
                    q.push(tmp); // 插入 *2 *3 *5的结果，最小值上浮到堆顶
                }
            }
            result = q.top();
            s.erase(result);
            q.pop();
        }
        return result;
    }

    // 高效解法：三指针
    int GetUglyNumber_Solution3(int index) {
        int t2 = 0, t3 = 0, t5 = 0;
        std::vector<int> result(index, 1);

        for (int i = 1; i < index; i++) {
            result[i] = min(result[t2] * 2, result[t3] * 3, result[t5] * 5);
            if (result[i] == 2 * result[t2]) t2++;
            if (result[i] == 3 * result[t3]) t3++;
            if (result[i] == 5 * result[t5]) t5++;
        }

        return result[index - 1];
    }

    // ===== 工具函数 =====
    // 定义求三个数中最小值的函数
    int min(int a, int b, int c) {
        int tmp = a < b ? a : b;
        return tmp < c ? tmp : c;
    }

    // 测试函数
    void test(int index) {
        int result = 0;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(index);
            gettimeofday(&end, nullptr);
            printf("number: %d, result: %d, time(us): %ld\n", index, result, end.tv_usec - start.tv_usec);
        }
    }

private:
    typedef int (Solution::*func_ptr)(int);
    std::vector<func_ptr> func_vec_ = {&Solution::GetUglyNumber_Solution1,
                                       &Solution::GetUglyNumber_Solution2,
                                       &Solution::GetUglyNumber_Solution3};
};

int main(int argc, char* argv[])
{
    Solution s;

    for (int i = 10; i <= 1000; i += 100) {
        s.test(i);
    }

    return 0;
}