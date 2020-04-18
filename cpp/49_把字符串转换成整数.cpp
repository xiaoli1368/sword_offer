#include <iostream>
#include <string>
#include <cmath>

class Solution {
public:
    // 个人答案
    int StrToInt(std::string str) {
        if (str.empty()) {
            return 0;
        }
        
        int sign = 1;
        long sum = 0;
        for (int i = 0; i < str.size(); i++) {
            if (i == 0 && str[i] == '-') {
                sign = -1;
                continue;
            }
            if (i == 0 && str[i] == '+') {
                continue;
            }
            if (str[i] < '0' || str[i] > '9') {
                return 0;
            }
            sum = sum * 10 + int(str[i] - '0');
        }
        sum *= sign;

        // 考虑int溢出
        if (sum >= pow(2, 31) || sum < -pow(2, 15)) {
            return 0;
        } else {
            return sum;
        }
    }

    // 参考答案
    // 没有考虑溢出
    int StrToInt2(std::string str) {
        if (str.empty()) {
            return 0;
        }

        int ret = 0;
        bool isNegative = str[0] == '-';

        for (int i = 0; i < str.size(); i++) {
            char c = str[i];
            if (i == 0 && (c == '+' || c == '-')) {
                continue;
            }
            if (c < '0' || c > '9') {
                return 0;
            }
            ret = ret * 10 + (c - '0');
        }
        
        return isNegative ? -ret : ret;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.StrToInt("-2147483649") << std::endl;
    std::cout << s.StrToInt("+456") << std::endl;
    std::cout << s.StrToInt("-123") << std::endl;
    
    std::cout << s.StrToInt2("-2147483649") << std::endl;
    std::cout << s.StrToInt2("+456") << std::endl;
    std::cout << s.StrToInt2("-123") << std::endl;

    return 0;
}