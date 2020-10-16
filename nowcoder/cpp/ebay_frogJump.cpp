#include <stdio.h>
#include <math.h>

class Solution {
public:
    int jump(int n) {
        if (n <= 1) {
            return 0;
        }
        int* dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = (i == 1 ? 1 : 0);
            for (int j = 0; i - pow(2, j) >= 1; j++) {
                dp[i] += dp[i - int(pow(2, j))];
            }
        }
        return dp[n];
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    printf("%d\n", s.jump(5));
    return 0;
}