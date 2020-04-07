#include <iostream>

class Solution {
public:
    int jumpFloot(int n) {
        if (n < 3) {
            return n;
        }

        int a = 1, b = 2, c = 3;
        for (int i = 0; i < n - 2; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.jumpFloot(15) << std::endl;

    return 0;
}