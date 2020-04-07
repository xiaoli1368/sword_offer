#include <iostream>

class Solution {
public:
    double Power(double base, int exponent) {
        if (exponent == 0) {
            return 1.0;
        }

        bool sign = false;
        if (exponent < 0) {
            sign = true;
            exponent = -exponent;
        }

        double result = 1.0;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }

        if (sign) {
            result = 1 / result;
        }

        return result;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.Power(2, 3) << std::endl;
    std::cout << s.Power(2, -3) << std::endl;
    
    return 0;
}