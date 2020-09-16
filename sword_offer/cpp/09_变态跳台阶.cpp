#include <iostream>
#include <cmath>

class Solution {
public:
    // 常规解法
    int jumpFloorII(int n) {
        if (n == 0) {
            return n;
        }
        
        int tmp = 1;
        for (int i = 0; i < n - 1; i++) {
            tmp *= 2;
        }
        return tmp;
    }

    // 库函数解法
    int jumpFloorII2(int n) {
        if (n == 0) {
            return n;
        }

        return pow(2, n);
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.jumpFloorII(9) << std::endl;
    std::cout << s.jumpFloorII2(9) << std::endl;
    
    return 0;
}