#include <iostream>

class Solution {
public:
    int NumberOf1Between1AndN_Solution(int n) {
        int cnt = 0;
        for (int m = 1; m <= n; m *= 10) {
            int a = n / m;
            int b = n % m;
            cnt += (a + 8) / 10 * m + (a % 10 == 1 ? b + 1 : 0);
        }
        return cnt;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::cout << s.NumberOf1Between1AndN_Solution(12345) << std::endl;

    return 0;
}