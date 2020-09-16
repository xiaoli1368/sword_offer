#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 利用stl求解
    std::string LeftRotateString1(std::string str, int n) {
        if (str.empty() || n <= 0 || n >= str.size()) {
            return str;
        }
        return str.substr(n, str.size() - n) + str.substr(0, n);
    }

    // 高效解法：两部分分别翻转，然后整体翻转
    std::string LeftRotateString2(std::string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }

        str_reverse(str, 0, n - 1);
        str_reverse(str, n, str.size() - 1);
        str_reverse(str, 0, str.size() - 1);
        return str;
    }

    // 其它思路，两个相同字符串拼接，然后取自串
    std::string LeftRotateString3(std::string str, int n) {
        if (str.empty() || n <= 0 || n >= str.size()) {
            return str;
        }

        std::string tmp = str + str;
        return tmp.substr(n, str.size());
    }

    // 工具函数，实现翻转（对称）
    void str_reverse(std::string& str, int l, int h) {
        for (; l < h; l++, h--) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
        }
    }

    // 测试函数
    void test(std::string& str, int n) {
        std::string result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(str, n);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %s\n", end.tv_usec - start.tv_usec, result.c_str());
        }
    }

private:
    typedef std::string (Solution::*func_ptr)(std::string, int);
    std::vector<func_ptr> func_vec_ = {&Solution::LeftRotateString1,
                                       &Solution::LeftRotateString2,
                                       &Solution::LeftRotateString3};
};

int main(int argc, char* argv[])
{
    std::string str1 = "abcdefg";
    std::string str2 = "abcXYZdef";
    std::string str3 = "lrloseumgh";
 
    Solution s;
    s.test(str1, 2);
    s.test(str2, 3);
    s.test(str3, 6);

    return 0;
}