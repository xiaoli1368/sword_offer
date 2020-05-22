#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>

class Solution {
public:
    // 第一次的解法，递归
    bool match1(char* str, char* pattern) {
        if (*str == '\0' && *pattern == '\0') {
            return true;
        }
        if (*str != '\0' && *pattern == '\0') {
            return false;
        }
        
        // 剩下的情况是 *pattern != '\0'
        // 此时考虑 *(pattern + 1) 是否为 '*'
        
        if (*(pattern + 1) != '*') { // 后一位不是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                return match1(str + 1, pattern + 1);
            } else {
                return false;
            }
        } else { // 后一位是 '*'
            if (*str == *pattern || (*str != '\0' && *pattern == '.')) {
                // 注意这里，不确定 * 会重复几次，因此需要 ||
                return match1(str + 1, pattern) || match1(str, pattern + 2);
            } else { // * 被当作空
                return match1(str, pattern + 2);
            }
        }
    }

    // 递归优化版
    bool match2(char* str, char* pattern) {
        if (*pattern == '\0') {
            return *str == '\0';
        }
        
        // 此时的情况是 *pattern != '\0'
        bool first_match = false;
        if (*str != '\0' && (*pattern == '.' || *pattern == *str)) {
            first_match = true;
        }
        
        // 此时考虑 *(pattern + 1) 是否为 '*'
        if (*(pattern + 1) == '\0' || *(pattern + 1) != '*') {
            return first_match && match2(str + 1, pattern + 1);
        } else {
            return match2(str, pattern + 2) || (first_match && match2(str + 1, pattern));
        }
    }

    /* 动态规划版本，来自leetcode，其实使用string作为形参更加方便
     * dp[m][n]的初始化：
     *     0. dp[][]初始全为false，表示不匹配
     *     1. dp[0][0]为true，表示两个空串匹配
     *     2. dp[1][1]仅与当前字符是否匹配相关
     *     3. dp[0]即第0行初始化，表示空s与p的匹配关系
     * 初始化实例如下：
     *       ""  a   *   a 
     *   ""  1   0   1   0
     *   a   0   1  
     *   a   0
     *   a   0
     * 求解dp[i+1][j+1]运算步骤：
     *     1. cmp(s, p)，当二者当前字符匹配时：dp[i+1][j+1] = dp[i][j]
     *     2. cmp('*', p)，当p为*时进行，cmp(s, p-1)
     *     3. 若仍不匹配，选择将*和之前的一个字符跳过，dp[i+1][j+1] = dp[i+1][j-1]
     *     4. 若匹配，选择将*和之前的一个字符跳过或者重复一次，dp[i+1][j+1] = dp[i+1][j-1] || dp[i][j+1]
     * 示例1：
     *       ""  a   *   a 
     *   ""  1   0   1   0
     *   a   0   1   1   1
     *   a   0   0   1   1
     *   a   0   0   1   1
     * 示例2：
     *       ""  a   *   a 
     *   ""  1   0   1   0
     *   a   0   1   1   1
     *   b   0   0   0   0
     *   a   0   0   0   0
     */
    bool match3(char* s, char* p) {
        if (*p == '\0') {
            return *s == '\0';
        }

        // 获取两个字符串的size
        int m = 0;
        int n = 0;
        while (*(s + m) != '\0') {
            m++;
        }
        while (*(p + n) != '\0') {
            n++;
        }
        // 初始化，dp[m][n]表示s的前m个元素能否与p的前m个元素匹配
        bool dp[m + 1][n + 1];
        memset(dp, false, (m + 1) * (n + 1));

        dp[0][0] = true; // (0, 0)表示两个空串匹配
        if (m != 0 && (p[0] == '.' || p[0] == s[0])) {
            dp[1][1] = true; // (1, 1)相等即匹配，包括'.'
        }
        if (p[0] == '*') {
            dp[0][1] == true;
        }
        for (int i = 0; i < n; i++) { // 初始化第0行，空s与p匹配关系
            if (p[i] == '*' && dp[0][i - 1] == true) {
                dp[0][i + 1] = true;
            }
        }

        // 主循环
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (s[i] == p[j] || p[j] == '.') {
                    dp[i + 1][j + 1] = dp[i][j];
                }
                if (p[j] == '*') { //如果是*
                    if (s[i] != p[j - 1] && p [j - 1] != '.')
                        //二者不相等的时候，就将这个*和前面的字符都跳过去看是否匹配
                        dp[i + 1][j + 1] = dp[i + 1][j - 1];
                    else {
                        //二者相等的时候,可以选择跳过或者选一个或多个
                        dp[i + 1][j + 1] = dp[i][j + 1] || dp[i + 1][j - 1];
                    }
                }
            }
        }

        return dp[m][n];
    }

    // 测试函数
    void test(char *s, char* p) {
        bool result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(s, p);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %d, str: %s, pat: %s\n", end.tv_usec - start.tv_usec, result, s, p);
        }
    }

private:
    typedef bool (Solution::*func_ptr)(char*, char*);
    std::vector<func_ptr> func_vec_ = {&Solution::match1,
                                       &Solution::match2,
                                       &Solution::match3};
};

int main()
{
    std::vector<std::pair<std::string, std::string>> map = {{"aaa", "a*a"},
                                                            {"bbb", "aaa"},
                                                            {"aaa", "a*"},
                                                            {"aab", "c*a*b"},
                                                            {"mississippi", "mis*is*p*."},
                                                            {"asjkldf", ".*"},
                                                            {"aaa", "*"}};

    Solution s;
    for (auto i : map) {
        s.test(const_cast<char*>(i.first.c_str()), const_cast<char*>(i.second.c_str()));
    }

    return 0;
}