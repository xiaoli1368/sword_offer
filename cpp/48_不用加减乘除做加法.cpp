#include <iostream>

class Solution {
public:
    // 递归实现
    int Add(int a, int b) {
        return b == 0 ? a : Add(a ^ b, (a & b) << 1);
    }

    // 循环实现
    int Add2(int a, int b) {
        int tmp = 0;
        while (b != 0) {
            tmp = a ^ b;
            b = (a & b) << 1;
            a = tmp;
        }
        return a;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.Add(12, 10) << std::endl;
    std::cout << s.Add2(12, 10) << std::endl;

    return 0;
}