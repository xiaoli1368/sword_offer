#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <sys/time.h>

class Solution {
public:
    // 第一版：存在较大优化空间
    std::string ReverseSentence1(std::string str) {
        if (str.empty()) {
            return str;
        }

        int l = 0;
        int h = 0;
        while (l <= h && h <= str.size() - 1) {
            if (str[l] == ' ') { // 可能开头是空格
                l++;
                h++;
                continue;
            }
            
            if (str[h] == ' ') {
                str_reverse(str, l, h - 1);
                l = h;
            } else if (h == str.size() - 1) {
                str_reverse(str, l, h);
                break;
            } else {
                h++;
            }
        }
        str_reverse(str, 0, str.size() - 1);

        return str;
    }

    // 第二版：简化版
    // 不能去除尾部空格
    std::string ReverseSentence2(std::string str) {
        if (str.empty()) {
            return str;
        }

        int l = 0;
        int h = 0;
        int length = str.size();

        while (l <= h && h <= length) {
            if (h == length || str[h] == ' ') {
                str_reverse(str, l, h - 1);
                l = h + 1; // 跳过了每次的空格
            }
            h++;
        }
        str_reverse(str, 0, length - 1);

        return str;
    }

    // 第三版：来自leetcode的相似题型
    // 增加功能：去除前后所有空格，并保证相邻两个单词之间只有一个空格
    std::string ReverseSentence3(std::string s) {
        if (s.empty()) {
            return s;
        }

        // 第一次遍历，所有单词完成翻转
        int i, j;
        for (i = 0; i < s.size(); i++) {
            // 确定单词的左边界
            if (s[i] == ' ') { continue;}

            // 确定单词的右边界
            for (j = i; j < s.size(); j++) {
                if (s[j] == ' ') {
                    break;
                }
            }

            // 完成当前单词的寻传，并更新索引
            str_reverse(s, i, j - 1);
            i = j;
        }

        // 第二次遍历，找到前后不是空格的索引
        int l = 0;
        int h = s.size() - 1;
        while (l < s.size() && s[l] == ' ') {l++;}
        while (h >= 0 && s[h] == ' ') {h--;}

        // 第三次遍历，按照反序添加，同时控制空格数量
        std::string ret;
        while (h >= l) {
            ret += s[h];
            if (s[h] != ' ') {
                h--;
            } else {
                while (h >= l && s[h] == ' ') {
                    h--;
                }
            }
        }
        return ret;
    }

    // 工具函数：翻转字符串
    void str_reverse(std::string& str, int l, int h) {
        for (; l < h; l++, h--) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
        }
    }

    // 测试函数
    void test(std::string& str) {
        std::string result;
        struct timeval start, end;
        printf("=====\n");
        for (auto func : this->func_vec_) {
            gettimeofday(&start, nullptr);
            result = (this->*func)(str);
            gettimeofday(&end, nullptr);
            printf("time(us): %ld, result: %s\n", end.tv_usec - start.tv_usec, result.c_str());
        }
    }

private:
    typedef std::string (Solution::*func_ptr)(std::string);
    std::vector<func_ptr> func_vec_ = {&Solution::ReverseSentence1,
                                       &Solution::ReverseSentence2,
                                       &Solution::ReverseSentence3};
};

int main(int argc, char* argv[])
{
    std::vector<std::string> strs = {"",
                                     " ",
                                     "Student. a am I",
                                     "the sky is blue",
                                     "  hello world! ",
                                     "a good   example"};

    Solution s;
    for (auto str : strs) {
        s.test(str);
    }

    return 0;
}