#include <iostream>

class Solution {
public:
    // 暴力枚举
    int LastRemaining_Solution(int n, int m) {
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

    // 其它方法
    int LastRemaining_Solution2(int n, int m) {
        if (n == 0) {
            return -1;
        }

        int s = 0;
        for (int i = 2; i <= n; i++) {
            // 这个公式可以由递归得到
            s = (s + m) % i;
        }
        return s;
    }

    // 其它方法
    int LastRemaining_Solution3(int n, int m) {
        if (n == 0) {
            return -1;
        }
        if (n == 1) {
            return 0;
        }

        return (LastRemaining_Solution3(n - 1, m) + m) % n;
    }

    // 需补充单向循环链表方法
    int LastRemaining_Solution4(int n, int m) {}
};

int main(int argc, char* argv[])
{
    Solution s;

    std::cout << s.LastRemaining_Solution(10, 4) << std::endl;
    std::cout << s.LastRemaining_Solution2(10, 4) << std::endl;
    std::cout << s.LastRemaining_Solution3(10, 4) << std::endl;
    return 0;
}