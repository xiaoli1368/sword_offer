#include <iostream>
#include <vector>

class Solution {
public:
    // 暴力解法，复杂度过大
    int GetUglyNumber_Solution(int index) {
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

    // 定义求三个数中最小值的函数
    int min(int a, int b, int c) {
        int tmp = a < b ? a : b;
        return tmp < c ? tmp : c;
    }

    // 高效解法
    int GetUglyNumber_Solution2(int index) {
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
};

int main(int argc, char* argv[])
{
    Solution s;

    for (int i = 1; i < 20; i++) {
        std::cout << s.GetUglyNumber_Solution(i) << " "
                  << s.GetUglyNumber_Solution2(i) << std::endl;
    }
    return 0;
}