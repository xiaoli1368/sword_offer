#include <iostream>
#include <string>

class Solution {
public:
    // 利用stl求解
    std::string LeftRotateString(std::string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }
        return str.substr(n, str.size() - n) + str.substr(0, n);
    }

    // 高效解法：两部分分别翻转，然后整体翻转
    void str_reverse(std::string& str, int l, int h) {
        while (l < h) {
            char tmp = str[l];
            str[l] = str[h];
            str[h] = tmp;
            l++;
            h--;
        }
    }

    std::string LeftRotateString2(std::string str, int n) {
        if (str.empty() || n == 0) {
            return str;
        }

        str_reverse(str, 0, n - 1);
        str_reverse(str, n, str.size() - 1);
        str_reverse(str, 0, str.size() - 1);
        return str;
    }

};

int main(int argc, char* argv[])
{
    Solution s;
    std::string str = "abcXYZdef";

    std::cout << str << std::endl;
    std::cout << s.LeftRotateString(str, 3) << std::endl;
    std::cout << s.LeftRotateString2(str, 3) << std::endl;
    return 0;
}