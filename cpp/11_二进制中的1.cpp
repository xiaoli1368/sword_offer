#include <iostream>

class Solution {
public:
    int NumberOf1(int n) {
        // c++需要转换类型
        unsigned int tmp = n;
        int result = 0;
        while (tmp > 0) {
            if (tmp & 1 == 1) {
                result++;
            }
            tmp >>= 1;
        }
        return result;
    }

    int NumberOf1_easy(int n) {
        // 这种方式不需要转换符号
        int cnt = 0;
        while (n != 0) {
            cnt++;
            n &= (n - 1);
        }
        return cnt;
    }
};

int main(int argc, char* [])
{
    Solution s;
    std::cout << s.NumberOf1(8) << std::endl;
    std::cout << s.NumberOf1(-7) << std::endl;

    std::cout << s.NumberOf1_easy(8) << std::endl;
    std::cout << s.NumberOf1_easy(-7) << std::endl;
    return 0;
}