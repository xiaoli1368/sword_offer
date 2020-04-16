#include <iostream>
#include <string>

class Solution {
public:
    std::string ReverseSentence(std::string str) {
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

    // 翻转字符串
    void str_reverse(std::string& str, int l, int h) {
        char tmp = '\0';
        while (l < h) {
            tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
            l++;
            h--;
        }
    }

    // 简化版
    std::string ReverseSentence2(std::string str) {
        if (str.empty()) {
            return str;
        }

        int l = 0;
        int h = 0;
        int length = str.size();

        // 开头是空格也可以处理
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
};

int main(int argc, char* argv[])
{
    Solution s;
    std::string str = "Student a am I";

    std::cout << str << std::endl;
    std::cout << s.ReverseSentence(str) << std::endl;
    std::cout << s.ReverseSentence2(str) << std::endl;
    
    return 0;
}