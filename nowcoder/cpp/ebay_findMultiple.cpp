#include <stdio.h>
#include <vector>

class Solution {
public:
    bool findMultiple(int n, int m, int k, std::vector<int> lst) {
        if (m == 1) {
            return false;
        }
        if (m == 2) {
            // 是否存在两数之和
            int l = 0, h = n - 1;
            while (l < h) {
                if ((lst[l] + lst[h]) % k == 0) {
                    return true;
                }
            }
            return false;
        }
        // 正常情况
        int cnt = 0;
        for (auto & i : lst) {
            if (i % k == 0) {
                cnt += 1;
            }
        }
        return cnt >= m;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    printf("%d\n", s.findMultiple(5, 4, 3, std::vector<int>{3, 3, 6, 9, 3}));
    printf("%d\n", s.findMultiple(5, 4, 3, std::vector<int>{3, 2, 6, 9, 2}));
    printf("%d\n", s.findMultiple(2, 2, 3, std::vector<int>{1, 2}));
    return 0;
}