#include <iostream>

class Solution {
public:
    int jumpFloorII(int n) {
        if (n == 0) {
            return n;
        } else {
            int tmp = 1;
            for (int i = 0; i < n - 1; i++) {
                tmp *= 2;
            }
            return tmp;
        }
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.jumpFloorII(9) << std::endl;
    
    return 0;
}