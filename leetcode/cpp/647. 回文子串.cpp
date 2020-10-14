#include <stdio.h>
#include <string>
#include <vector>

class Solution {
public:
    // ===== 工具函数 =====
    // 判断是否为回文串
    bool judge(std::string& s, int l, int r) {
        while (l <= r) {
            if (s[l] != s[r]) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }

    // 获取以l,r为中心的回文子串个数，就是最长子串的一半
    int getLength(std::string& s, int l, int r) {
        if (s[l] != s[r]) {
            return 0;
        }
        while (l - 1 >= 0 && r + 1 < s.size() && s[l - 1] == s[r + 1]) {
            l -= 1;
            r += 1;
        }
        return (r - l) / 2 + 1;
    }

    // 暴力法
    int countsubString(std::string& s) {
        int ret = 0;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                if (judge(s, i, j)) {
                    ret += 1;
                }
            }
        }
        return ret;
    }

    // 中心匹配法
    int countsubString2(std::string& s) {
        int ret = 0;
        for (int i = 0; i < 2 * s.size() - 1; i++) {
            int center = i / 2;
            if (i % 2 == 0) {
                ret += getLength(s, center, center);
            } else {
                ret += getLength(s, center, center + 1);
            }
        } 
        return ret;
    }

    // 动态规划
    int countsubString3(std::string& s) {
        if (s.empty()) {
            return 0;
        }

        int ret = 0, n = s.size();
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                if (i <= j && s[i] == s[j]) {
                    dp[i][j] = i + 1 <= j - 1 ? dp[i + 1][j - 1] : true;
                }
                if (dp[i][j]) {
                    ret += 1;
                }
            }
        }
        return ret;
    }
};

int main(int argc, char* argv[])
{
    Solution s;
    std::string ss = "aaabbbccc";
    printf("%d\n", s.countsubString(ss));
    printf("%d\n", s.countsubString2(ss));
    printf("%d\n", s.countsubString3(ss));
    return 0;
}