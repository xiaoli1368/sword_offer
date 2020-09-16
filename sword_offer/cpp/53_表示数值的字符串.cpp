#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

class Solution {
public:
    // 牛客网版本，已经AC
    bool isNumeric(char* str) {
        if (str == nullptr) {
            return false;
        }
        
        // 处理首位的符号位
        if (*str == '+' || *str == '-') {
            str++;
        }
        
        // 辅助参数
        int e_cnt = 0;
        int dot_cnt = 0;
        bool has_value = false;
        
        // 为了简化代码
        str--;
        while (*(++str) != '\0') {
            if (*str >= '0' && *str <= '9') {
                has_value = true;
            } else { // 以下不会出现数值
                has_value = false;
                if (*str == '.' && e_cnt == 0) { // 注意不能在先有e的情况下出.小数点
                    dot_cnt++;
                } else if (*str == 'e' || *str == 'E') {
                    e_cnt++;
                } else if ((*str == '+' || *str == '-') && (*(str - 1) == 'e' || *(str - 1) == 'E')) { // 再次出现符号位时，前一位必须为e
                    continue;
                } else {
                    return false;
                }
                
                // 合法性判断
                if (e_cnt >= 2 || dot_cnt >= 2) { // 两个e或者两个.出现时，即为false
                    return false;
                }
            }
        }
        return has_value;
    }

    // leetcode版本，已经AC，复杂的多
    bool isNumber(std::string s) {
        if (s.empty()) {
            return false;
        }

        // 跳过开头和结尾的空格
        int start = 0;
        int end = s.size() - 1;
        while (start < s.size() && s[start] == ' ') start++;
        while (end >= 0 && s[end] == ' ') end--;

        // 用来计数的变量
        int numCnt = 0;
        int signCnt = 0;
        int dotCnt = 0;
        int eCnt = 0;

        // 遍历数字串，排除非法结果
        for (int i = start; i <= end; i++) {
            if (isNum(s[i])) { // 数字
                numCnt++;
            } else if (isE(s[i])) {// e符号
                eCnt++;
                // e不能多于1个，不能位于开头，不能位于结尾
                if (eCnt > 1 || i == start || i == end) {
                    return false;
                }
            } else if (isSign(s[i])) { // 符号位
                signCnt++;
                // 符号位必须在开头或者在e后边
                if (i != start && !isE(s[i - 1])) {
                    return false;
                }
                // 符号位不能多于2个，不能在末尾，后边不能为e
                if (signCnt > 2 || i == end || isE(s[i + 1])) {
                    return false;
                }
            } else if (isDot(s[i])) {  // 小数点
                dotCnt++;
                // 小数点不能多于1个，且不能在e出现后再出现
                if (dotCnt > 1 || (dotCnt == 1 && eCnt >= 1)) {
                    return false;
                }
                // 小数点后边只能是数字或者e
                if (i != end && !isNum(s[i + 1]) && !isE(s[i + 1])) {
                    return false;
                }
                // 小数点前后不能都没有数字
                if ((i == start || !isNum(s[i - 1])) && (i == end || !isNum(s[i + 1]))) {
                    return false;
                }
            } else { // 非法字符
                return false;
            }
        }

        // 结果中必须含有数字
        return numCnt > 0;
    }

    // ===== 工具函数 =====

    bool isNum(char& ch) {
        return ch >= '0' && ch <= '9';
    }

    bool isE(char& ch) {
        return ch == 'e' || ch == 'E';
    }

    bool isDot(char & ch) {
        return ch == '.';
    }

    bool isSign(char & ch) {
        return ch == '+' || ch == '-';
    }

    // 测试函数
    void test(std::string& str) {
        bool result1, result2;
        struct timeval start, end;
        result1 = this->isNumeric(const_cast<char*>(str.c_str()));
        result2 = this->isNumber(str);
        printf("result1: %d, result2: %d, string: %s\n", result1, result2, str.c_str());
    }
};

int main(int argc, char* argv[])
{
    std::vector<std::string> strs = {"+100", "5e2", "-123", "3.1416", "0123",
                                     "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4",
                                     "0", " 0.1", "abc", "1 a", "2e10", " -90e3",
                                     " 1e", "e3", " 6e-1", " 99e2.5", "53.5e93",
                                     " --6", "-+3", "95a54e53"};

    Solution s;
    for (auto str : strs) {
        s.test(str);
    }

    return 0;
}